import sqlite3
import sys

from PySide6.QtCore import QDate, QPoint, QRegularExpression, Qt, QTimer
from PySide6.QtGui import QColor, QRegularExpressionValidator
from PySide6.QtWidgets import (QApplication, QGraphicsDropShadowEffect,
                               QMainWindow, QMessageBox, QTableWidgetItem)

from database.dbAppointment import Appointment
from database.dbClients import DeleteDB, WriteDB
from database.dbCreator import CreateDB
from modules.input_verification import (CheckAppointment, CheckRegister,
                                        InputVerify)
from modules.ui_main import Ui_MainWindow
from modules.ui_splash_screen import Ui_SplashScreen
from widgets.circular_progress import CircularProgress

DB_LOCATION = 'database/data/db.sqlite3'


class SplashScreen(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.db = CreateDB()
        self.ui.setupUi(self)

        # Remove Title bar
        self.setWindowFlags(Qt.FramelessWindowHint)  # type: ignore
        self.setAttribute(Qt.WA_TranslucentBackground)  # type: ignore

        self.progress = CircularProgress()
        self.progress.width = 270  # type: ignore
        self.progress.height = 270  # type: ignore
        self.progress.value = 50
        self.progress.setFixedSize(self.progress.width,  # type: ignore
                                   self.progress.height)
        self.progress.move(15, 15)
        self.progress.font_size = 20
        self.progress.addShadow(True)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        self.show()

        # Add SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        self.counter = 0

    # Update progress bar
    def update(self):
        # Set value to progress bar
        self.progress.setValue(self.counter)

        if self.counter == 30:
            self.db.makeDataFolder()

        if self.counter == 50:
            self.db.makeDataBase()

        # Stop counter
        if self.counter >= 100:
            self.timer.stop()

            # Open a new Window
            self.main = MainWindow()
            self.main.show()

            # Close Splash Screen
            self.close()

        # Increases counter
        self.counter += 1


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widgets = self.ui

        self.setWindowFlags(Qt.FramelessWindowHint)  # type: ignore
        self.setAttribute(Qt.WA_TranslucentBackground)  # type: ignore

        # Connect buttons with buttonClick function.
        self.widgets.homeBtn.clicked.connect(self.buttonClick)
        self.widgets.clientsBtn.clicked.connect(self.buttonClick)
        self.widgets.appointmentBtn.clicked.connect(self.buttonClick)
        self.widgets.logoutBtn.clicked.connect(self.buttonClick)

        self.widgets.minimizeAppBtn.clicked.connect(self.buttonClick)
        self.widgets.maximizeRestoreAppBtn.clicked.connect(self.buttonClick)
        self.widgets.closeAppBtn.clicked.connect(self.buttonClick)

        self.widgets.addBtn.clicked.connect(self.buttonClick)
        self.widgets.delBtn.clicked.connect(self.buttonClick)
        self.widgets.editBtn.clicked.connect(self.buttonClick)
        self.widgets.reloadBtn.clicked.connect(self.buttonClick)

        self.widgets.searchBox.textChanged.connect(self.searchTable)

        self.widgets.confirmRegisterBtn.clicked.connect(self.tryRegister)
        self.widgets.appointmentConfirmBtn.clicked.connect(self.tryAppointment)

        self.widgets.lineName.setValidator(
            QRegularExpressionValidator(QRegularExpression('[a-zA-Z]*')))
        self.widgets.lineSurname.setValidator(
            QRegularExpressionValidator(QRegularExpression('^[a-zA-Z\s]+$')))
        self.widgets.lineCel.setValidator(
            QRegularExpressionValidator(QRegularExpression('\d+')))
        self.widgets.lineCPF.setValidator(
            QRegularExpressionValidator(QRegularExpression('\d+')))

        self.widgets.appointmentName.setValidator
        (QRegularExpressionValidator(QRegularExpression('[a-zA-Z]*')))
        self.widgets.appointmentCPF.setValidator(
            QRegularExpressionValidator(QRegularExpression('\d+')))

        # Conectando o sinal textChanged() para formatar o número de telefone.
        self.widgets.lineCel.textChanged.connect(
            lambda text: self.widgets.lineCel.setText(
                InputVerify.format_cel_number(text))
            )
        self.widgets.lineCPF.textChanged.connect(
            lambda text: self.widgets.lineCPF.setText(
                InputVerify.format_cpf(text))
            )
        self.widgets.appointmentCPF.textChanged.connect(
            lambda text: self.widgets.appointmentCPF.setText(
                InputVerify.format_cpf(text))
            )
        
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.homePage)
        self.attTableWidget()

# /////////////////////////////////////////////////////////////////////////////
# Register functions to get, verify and write on database.
# /////////////////////////////////////////////////////////////////////////////

    def getInputRegister(self):
        """ Get inputs from the register page. """
        inputName = self.widgets.lineName.text()
        inputSurname = self.widgets.lineSurname.text()
        inputGender = self.widgets.genderSelect.currentText()
        inputCPF = self.widgets.lineCPF.text()
        inputCel = self.widgets.lineCel.text()
        inputBirth = self.widgets.dateSelect.date().toString(("dd/MM/yyyy"))
        inputEmail = self.widgets.lineEmail.text()

        dados = (inputName, inputSurname, inputGender, inputCPF, inputCel,
                 inputBirth, inputEmail)
        return dados

    def tryRegister(self):
        clientInput = self.getInputRegister()
        verification = CheckRegister()

        if not verification.isFilled(clientInput):
            return QMessageBox.warning(self,
                                       'Cadastro', 'Preencha todos os campos.')

        if not verification.isCpfValid(clientInput):
            return QMessageBox.warning(self, 'CPF invalido',
                                       'Informe um CPF valido.')

        if not verification.isPhoneValid(clientInput):
            return QMessageBox.warning(self, 'Telefone incompleto.',
                                       'Informe um Celular ou Telefone.')

        if verification.isCpfInDB(clientInput):
            return QMessageBox.warning(self, 'CPF Cadastrado.',
                                       'CPF informado já está em registrado.')

        try:
            self.proceedRegister(clientInput)
            QMessageBox.information(self, 'Concluído.',
                                    'A cadastro efetuado.')
        except Exception as e:
            return QMessageBox.warning(self, f'ERRO: {exc_type.__name__}',
                                       f'Descrição: {e}.')
        finally:
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.clientPage)
            self.clearRegisterLines()
            self.attTableWidget()

    def proceedRegister(self, clientInput):
        write = WriteDB()
        write.writeUser(*clientInput)

# /////////////////////////////////////////////////////////////////////////////
# Appointment functions to get, verify and write on database.
# /////////////////////////////////////////////////////////////////////////////

    def getAppointment(self):
        """ Get inputs from the Appointment page. """
        inputName = self.widgets.appointmentName.text()
        inputCPF = self.widgets.appointmentCPF.text()
        inputDat = self.widgets.appointmentDate.date().toString(("dd/MM/yyyy"))
        inputHour = self.widgets.appointmentHour.text()

        dados = (inputName, inputCPF, inputDat, inputHour)
        return dados

    def tryAppointment(self):
        """ Write inputs in the data base if True."""
        clientInput = self.getAppointment()
        verification = CheckAppointment()

        if not verification.isFilled(clientInput):
            return QMessageBox.warning(self,
                                       'Consulta', 'Preencha todos os campos.')

        if not verification.isCpfValid(clientInput):
            return QMessageBox.warning(self,
                                       'Consulta', 'CPF invalido.')

        if not verification.isCpfInDB(clientInput):
            return QMessageBox.warning(self, 'CPF não encontrado.',
                                       'CPF não esta cadastrado.')
        try:
            self.proceedAppointment(clientInput)
            QMessageBox.information(self, 'Concluído.',
                                    'A consulta foi agendada')
        except Exception as e:
            return QMessageBox.warning(self, f'ERRO: {exc_type.__name__}',
                                       f'Descrição: {e}.')
        finally:
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.clientPage)
            self.attTableWidget()
            self.clearAppointmentLines()

    def proceedAppointment(self, clientInput):
        makeAppointment = Appointment()
        makeAppointment.makeAppointment(*clientInput)

# /////////////////////////////////////////////////////////////////////////////
# Updates the table from data in db.sqlite3.
# /////////////////////////////////////////////////////////////////////////////

    def attTableWidget(self):
        conn = sqlite3.connect(DB_LOCATION)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        results = cursor.fetchall()

        self.widgets.clientsTable.clearContents()
        self.widgets.clientsTable.setRowCount(len(results))

        for row, text in enumerate(results):
            for column, data in enumerate(text):
                self.widgets.clientsTable.setItem(
                    row, column, QTableWidgetItem(str(data)))

        cursor.close()

# /////////////////////////////////////////////////////////////////////////////
# Function that dynamically looks up things in the table.
# /////////////////////////////////////////////////////////////////////////////

    def searchTable(self):
        # Recupera o texto inserido na QLineEdit
        search_text = self.widgets.searchBox.text()

        # Percorre todas as células da QTableWidget
        for row in range(self.widgets.clientsTable.rowCount()):
            row_hidden = True  # Define a linha como oculta
            for column in range(self.widgets.clientsTable.columnCount()):
                # Recupera o texto da célula
                cell_text = self.widgets.clientsTable.item(row, column).text()

                # Verifica se o texto pesquisado está contido no texto da célula
                if search_text in cell_text:
                    # Define a linha como visível
                    row_hidden = False
                    # Seleciona a célula
                    self.widgets.clientsTable.setCurrentCell(row, column)

            # Oculta ou exibe a linha de acordo com o resultado da pesquisa
            self.widgets.clientsTable.setRowHidden(row, row_hidden)

# /////////////////////////////////////////////////////////////////////////////
# Return a CPF string from Client Table
# /////////////////////////////////////////////////////////////////////////////

    def getCpfFromClientsTable(self):
        selected_items = self.widgets.clientsTable.selectedItems()
        if selected_items:
            current_item = selected_items[3]
            cpf = current_item.text()
            return cpf

# /////////////////////////////////////////////////////////////////////////////
# Allows the application to be dragged around the screen
# /////////////////////////////////////////////////////////////////////////////

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(
                self.pos() + QPoint(event.scenePosition().x(),
                                    event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

# /////////////////////////////////////////////////////////////////////////////
# Clear QLineEdit after use.
# /////////////////////////////////////////////////////////////////////////////
    def clearRegisterLines(self):
        date = QDate(1950, 1, 1)
        self.widgets.dateSelect.setDate(date)
        self.widgets.lineName.clear()
        self.widgets.lineSurname.clear()
        self.widgets.lineCPF.clear()
        self.widgets.lineCel.clear()
        self.widgets.lineEmail.clear()
        self.widgets.genderSelect.setCurrentIndex(0)

    def clearAppointmentLines(self):
        date = QDate(1950, 1, 1)
        self.widgets.appointmentDate.setDate(date)
        self.widgets.appointmentHour.clear()
        self.widgets.appointmentName.clear()
        self.widgets.appointmentCPF.clear()

# /////////////////////////////////////////////////////////////////////////////
# Execute something if any button was pressed.
# /////////////////////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "homeBtn":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.homePage)

        if btnName == "clientsBtn":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.clientPage)

        if btnName == "appointmentBtn":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.queriesPage)

        if btnName == "logoutBtn":
            sys.exit()

        if btnName == "addBtn":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.registerPage)

        if btnName == "delBtn":
            cpf = self.getCpfFromClientsTable()
            if cpf is not None:
                msg = QMessageBox()
                msg.setWindowTitle('Excluir')
                msg.setText('Esta ação é irreversivel!')
                msg.setInformativeText('Deseja continuar?')
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                answer = msg.exec()
                if answer == QMessageBox.Yes:
                    DeleteDB.deleteUser(cpf)
                    self.attTableWidget()
            else:
                return QMessageBox.information(self, 'Nada selecionado.',
                                               'Selecione um usuario.')

        if btnName == "editBtn":
            QMessageBox.warning(
                self, 'Clientes', 'Você não tem permissão para editar.')

        if btnName == "reloadBtn":
            self.attTableWidget()

        if btnName == "minimizeAppBtn":
            if self.isMinimized():
                self.showNormal()
            else:
                self.showMinimized()

        if btnName == "maximizeRestoreAppBtn":
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

        if btnName == "closeAppBtn":
            sys.exit()


if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec())