# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainqqWPPx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox,
                               QApplication, QComboBox, QDateEdit, QFrame,
                               QGridLayout, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QSpacerItem, QStackedWidget,
                               QTableWidget, QTableWidgetItem, QTimeEdit,
                               QVBoxLayout, QWidget)

from modules import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1239, 771)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"/* ////////////////////////////////////////////////////////////////////////////////////////////*/\n"
"#contentBox{\n"
"	background-color: rgb(68, 71, 90);\n"
"}\n"
"\n"
"#contentTopBg{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-bottom: 1px solid black;\n"
"}\n"
"\n"
"#topLogoInfo{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-bottom: 1px solid black;\n"
"}\n"
"/* ////////////////////////////////////////////////////////////////////////////////////////////*/\n"
"#leftMenuBg .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"\n"
"#leftMenuBg .QPushButton:hover { background-color: rgb(68, 71, 90); }\n"
""
                        "#leftMenuBg .QPushButton:pressed { background-color: rgb(98, 114, 164); color: rgb(255, 255, 255);}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////*/\n"
"\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////*/\n"
"\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////*/\n"
"\n"
"#page_1{background-color: rgb(68, 71, 90); borde"
                        "r: 1px solid }\n"
"#clientPage{background-color: rgb(68, 71, 90);}\n"
"#registerPage{background-color: rgb(68, 71, 90);}\n"
"#queriesPage {background-color: rgb(68, 71, 90); border: 1px solid }\n"
"\n"
"/* /////////////////////////////////////CLIENTS PAGE/////////////////////////////////////////////////*/\n"
"\n"
"#clientMenu .QPushButton {background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px;}\n"
"#clientMenu .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#addBtn:hover {background-color: rgb(80, 250, 123);}\n"
"#delBtn:hover {background-color: rgb(255, 85, 85);}\n"
"#editBtn:hover {background-color: rgb(98, 114, 164);}\n"
"#markBtn:hover {background-color: rgb(98, 114, 164);}\n"
"\n"
"#searchBtn{background-color: rgb(98, 114, 164); border: none;  border-radius: 5px;}\n"
"#searchBtn:hover {background-color: rgb(139, 163, 234);}\n"
"#searchBtn:pressed { background-color: rgb(67, 78, 112); border-style: solid; border-radius: 4px"
                        "; }\n"
"\n"
"#searchBox{border-bottom: 1px solid black; color: rgb(40, 44, 52);}\n"
"#searchBox {border: none; border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"\n"
"/* ////////////////////////////////////////REGISTER PAGE/////////////////////////////////////////////*/\n"
"#inputBox{	background-color: rgb(68, 71, 90); border: 2px solid rgb(248, 248, 242); border-radius: 4px;}\n"
"#registerTitle{font: 18pt \"Segoe UI\";}\n"
"\n"
"/* INPUT LINE*/\n"
"#registerPage .QLineEdit{border: none; border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"\n"
"#registerPage .QComboBox{border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"#registerPage .QComboBox::item {color: rgb(40, 44, 52);}\n"
"\n"
"#registerPage .QPushButton{background-color: rgb(98, 114, 164); border: none;  border-radius: 5px;}\n"
"#registerPage .QPushButton:hover {background-color: rgb(80, 250, 123);}\n"
"#registerPage .QPushButton:pressed { background-color: rgb(23, 2"
                        "6, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#dateSelect{border: none; border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"/* ////////////////////////////////////////EDIT PAGE/////////////////////////////////////////////*/\n"
"#inputBox2{	background-color: rgb(68, 71, 90); border: 2px solid rgb(248, 248, 242); border-radius: 4px;}\n"
"#editTitle{font: 18pt \"Segoe UI\";}\n"
"#editPage {background-color: rgb(68, 71, 90);}\n"
"\n"
"/* INPUT LINE*/\n"
"#editPage .QLineEdit{border: none; border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"\n"
"#editPage .QComboBox{border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"#editPage .QComboBox::item {color: rgb(40, 44, 52);}\n"
"\n"
"#editPage .QPushButton{background-color: rgb(98, 114, 164); border: none;  border-radius: 5px;}\n"
"#editPage .QPushButton:hover {background-color: rgb(80, 250, 123);}\n"
"#editPage .QPushButton:pressed { background-color: rgb(23, 26, 30); bo"
                        "rder-style: solid; border-radius: 4px; }\n"
"\n"
"#lineBornDateEdit{border: none; border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"/* ////////////////////////////////////////QUERIES PAGE/////////////////////////////////////////////*/\n"
"#queriesPage .QFrame{	background-color: rgb(68, 71, 90); border: 2px solid rgb(248, 248, 242); border-radius: 4px;}\n"
"#appointmentTitle{font: 18pt \"Segoe UI\";}\n"
"\n"
"#appointmentHour{border: none; border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"#appointmentDate{border: none; border-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}\n"
"\n"
"#appointmentConfirmBtn{background-color: rgb(48, 150, 74); border: none;  border-radius: 5px;}\n"
"#appointmentConfirmBtn:hover {background-color: rgb(80, 250, 123);}\n"
"#appointmentConfirmBtn:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* INPUT LINE*/\n"
"#queriesPage .QLineEdit{border: none; bord"
                        "er-bottom: 1px solid black; border-radius: 4px; color: rgb(40, 44, 52);}")
        self.verticalLayout_5 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.topLogoInfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.logoFrame = QFrame(self.topLogoInfo)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setMinimumSize(QSize(45, 50))
        self.logoFrame.setStyleSheet(u"image: url(:/images/images/images/bigLogo.png);")
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.logoFrame)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.homeBtn = QPushButton(self.leftMenuBg)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setMinimumSize(QSize(0, 45))
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.clientsBtn = QPushButton(self.leftMenuBg)
        self.clientsBtn.setObjectName(u"clientsBtn")
        sizePolicy.setHeightForWidth(self.clientsBtn.sizePolicy().hasHeightForWidth())
        self.clientsBtn.setSizePolicy(sizePolicy)
        self.clientsBtn.setMinimumSize(QSize(0, 45))
        self.clientsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clientsBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clientsBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.clientsBtn)

        self.appointmentBtn = QPushButton(self.leftMenuBg)
        self.appointmentBtn.setObjectName(u"appointmentBtn")
        sizePolicy.setHeightForWidth(self.appointmentBtn.sizePolicy().hasHeightForWidth())
        self.appointmentBtn.setSizePolicy(sizePolicy)
        self.appointmentBtn.setMinimumSize(QSize(0, 45))
        self.appointmentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.appointmentBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-calendar-check.png);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-calendar-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointmentBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.appointmentBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logoutBtn = QPushButton(self.leftMenuBg)
        self.logoutBtn.setObjectName(u"logoutBtn")
        sizePolicy.setHeightForWidth(self.logoutBtn.sizePolicy().hasHeightForWidth())
        self.logoutBtn.setSizePolicy(sizePolicy)
        self.logoutBtn.setMinimumSize(QSize(0, 45))
        self.logoutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.logoutBtn)

        self.leftGrip = QFrame(self.leftMenuBg)
        self.leftGrip.setObjectName(u"leftGrip")
        self.leftGrip.setMinimumSize(QSize(0, 22))
        self.leftGrip.setFrameShape(QFrame.StyledPanel)
        self.leftGrip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.leftGrip)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topGrip = QFrame(self.leftBox)
        self.topGrip.setObjectName(u"topGrip")
        self.topGrip.setMaximumSize(QSize(20, 16777215))
        self.topGrip.setFrameShape(QFrame.StyledPanel)
        self.topGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.topGrip)

        self.label = QLabel(self.leftBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon6)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"image: url(:/images/images/images/bigLogo.png);")
        self.stackedWidget.addWidget(self.homePage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.verticalLayout_9 = QVBoxLayout(self.registerPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame = QFrame(self.registerPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.inputBox = QFrame(self.frame)
        self.inputBox.setObjectName(u"inputBox")
        self.inputBox.setMinimumSize(QSize(0, 0))
        self.inputBox.setMaximumSize(QSize(550, 500))
        self.inputBox.setFrameShape(QFrame.StyledPanel)
        self.inputBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.inputBox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.registerTitle = QLabel(self.inputBox)
        self.registerTitle.setObjectName(u"registerTitle")

        self.verticalLayout_10.addWidget(self.registerTitle, 0, Qt.AlignHCenter)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(30)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.lineCPF = QLineEdit(self.inputBox)
        self.lineCPF.setObjectName(u"lineCPF")
        self.lineCPF.setMinimumSize(QSize(150, 25))
        self.lineCPF.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.lineCPF, 4, 1, 1, 1)

        self.labelName = QLabel(self.inputBox)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout_4.addWidget(self.labelName, 1, 0, 1, 1)

        self.labelEmail = QLabel(self.inputBox)
        self.labelEmail.setObjectName(u"labelEmail")

        self.gridLayout_4.addWidget(self.labelEmail, 7, 0, 1, 1)

        self.dateSelect = QDateEdit(self.inputBox)
        self.dateSelect.setObjectName(u"dateSelect")
        self.dateSelect.setMinimumSize(QSize(150, 26))
        self.dateSelect.setMaximumSize(QSize(150, 26))
        self.dateSelect.setAlignment(Qt.AlignCenter)
        self.dateSelect.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.dateSelect, 6, 1, 1, 1)

        self.confirmRegisterBtn = QPushButton(self.inputBox)
        self.confirmRegisterBtn.setObjectName(u"confirmRegisterBtn")
        self.confirmRegisterBtn.setMinimumSize(QSize(0, 25))
        self.confirmRegisterBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirmRegisterBtn.setStyleSheet(u"image: url(:/icons/images/icons/cil-check.png);")

        self.gridLayout_4.addWidget(self.confirmRegisterBtn, 8, 0, 1, 2)

        self.labelBornDate = QLabel(self.inputBox)
        self.labelBornDate.setObjectName(u"labelBornDate")

        self.gridLayout_4.addWidget(self.labelBornDate, 6, 0, 1, 1)

        self.lineSurname = QLineEdit(self.inputBox)
        self.lineSurname.setObjectName(u"lineSurname")
        self.lineSurname.setMinimumSize(QSize(0, 25))
        self.lineSurname.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.lineSurname, 2, 1, 1, 1)

        self.labelPhone = QLabel(self.inputBox)
        self.labelPhone.setObjectName(u"labelPhone")

        self.gridLayout_4.addWidget(self.labelPhone, 5, 0, 1, 1)

        self.lineName = QLineEdit(self.inputBox)
        self.lineName.setObjectName(u"lineName")
        self.lineName.setMinimumSize(QSize(300, 25))
        self.lineName.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.lineName, 1, 1, 1, 1)

        self.genderSelect = QComboBox(self.inputBox)
        self.genderSelect.addItem("")
        self.genderSelect.addItem("")
        self.genderSelect.addItem("")
        self.genderSelect.setObjectName(u"genderSelect")
        self.genderSelect.setMinimumSize(QSize(150, 25))
        self.genderSelect.setMaximumSize(QSize(150, 16777215))
        self.genderSelect.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.genderSelect, 3, 1, 1, 1, Qt.AlignLeft)

        self.lineCel = QLineEdit(self.inputBox)
        self.lineCel.setObjectName(u"lineCel")
        self.lineCel.setMinimumSize(QSize(150, 25))
        self.lineCel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.lineCel, 5, 1, 1, 1)

        self.labelCPF = QLabel(self.inputBox)
        self.labelCPF.setObjectName(u"labelCPF")

        self.gridLayout_4.addWidget(self.labelCPF, 4, 0, 1, 1)

        self.labelSurname = QLabel(self.inputBox)
        self.labelSurname.setObjectName(u"labelSurname")

        self.gridLayout_4.addWidget(self.labelSurname, 2, 0, 1, 1)

        self.labelGender = QLabel(self.inputBox)
        self.labelGender.setObjectName(u"labelGender")

        self.gridLayout_4.addWidget(self.labelGender, 3, 0, 1, 1)

        self.lineEmail = QLineEdit(self.inputBox)
        self.lineEmail.setObjectName(u"lineEmail")
        self.lineEmail.setMinimumSize(QSize(150, 25))
        self.lineEmail.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.lineEmail, 7, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.horizontalLayout_13.addWidget(self.inputBox)


        self.verticalLayout_9.addWidget(self.frame)

        self.stackedWidget.addWidget(self.registerPage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.verticalLayout_20 = QVBoxLayout(self.editPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.inputBox2 = QFrame(self.editPage)
        self.inputBox2.setObjectName(u"inputBox2")
        self.inputBox2.setMaximumSize(QSize(550, 500))
        self.inputBox2.setFrameShape(QFrame.StyledPanel)
        self.inputBox2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.inputBox2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.inputBox_2 = QFrame(self.inputBox2)
        self.inputBox_2.setObjectName(u"inputBox_2")
        self.inputBox_2.setMinimumSize(QSize(500, 500))
        self.inputBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.inputBox_2.setFrameShape(QFrame.StyledPanel)
        self.inputBox_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.inputBox_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 20, -1, 20)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_8)

        self.editTitle = QLabel(self.inputBox_2)
        self.editTitle.setObjectName(u"editTitle")

        self.verticalLayout_19.addWidget(self.editTitle, 0, Qt.AlignHCenter)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(30)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.lineEmailEdit = QLineEdit(self.inputBox_2)
        self.lineEmailEdit.setObjectName(u"lineEmailEdit")
        self.lineEmailEdit.setMinimumSize(QSize(150, 25))
        self.lineEmailEdit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.lineEmailEdit, 7, 1, 1, 1)

        self.confirmeditBtn = QPushButton(self.inputBox_2)
        self.confirmeditBtn.setObjectName(u"confirmeditBtn")
        self.confirmeditBtn.setMinimumSize(QSize(0, 25))
        self.confirmeditBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirmeditBtn.setStyleSheet(u"image: url(:/icons/images/icons/cil-pencil.png);\n"
"")

        self.gridLayout_5.addWidget(self.confirmeditBtn, 12, 0, 1, 2)

        self.labelGenderEdit = QLabel(self.inputBox_2)
        self.labelGenderEdit.setObjectName(u"labelGenderEdit")

        self.gridLayout_5.addWidget(self.labelGenderEdit, 3, 0, 1, 1)

        self.lineCPFEdit = QLineEdit(self.inputBox_2)
        self.lineCPFEdit.setObjectName(u"lineCPFEdit")
        self.lineCPFEdit.setMinimumSize(QSize(150, 25))
        self.lineCPFEdit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.lineCPFEdit, 4, 1, 1, 1)

        self.lineSurnameEdit = QLineEdit(self.inputBox_2)
        self.lineSurnameEdit.setObjectName(u"lineSurnameEdit")
        self.lineSurnameEdit.setMinimumSize(QSize(0, 25))
        self.lineSurnameEdit.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.lineSurnameEdit, 2, 1, 1, 1)

        self.genderSelectEdit = QComboBox(self.inputBox_2)
        self.genderSelectEdit.addItem("")
        self.genderSelectEdit.addItem("")
        self.genderSelectEdit.addItem("")
        self.genderSelectEdit.setObjectName(u"genderSelectEdit")
        self.genderSelectEdit.setMinimumSize(QSize(150, 25))
        self.genderSelectEdit.setMaximumSize(QSize(150, 16777215))
        self.genderSelectEdit.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.genderSelectEdit, 3, 1, 1, 1, Qt.AlignLeft)

        self.labelPhoneEdit = QLabel(self.inputBox_2)
        self.labelPhoneEdit.setObjectName(u"labelPhoneEdit")

        self.gridLayout_5.addWidget(self.labelPhoneEdit, 5, 0, 1, 1)

        self.labelEmailEdit = QLabel(self.inputBox_2)
        self.labelEmailEdit.setObjectName(u"labelEmailEdit")

        self.gridLayout_5.addWidget(self.labelEmailEdit, 7, 0, 1, 1)

        self.lineNameEdit = QLineEdit(self.inputBox_2)
        self.lineNameEdit.setObjectName(u"lineNameEdit")
        self.lineNameEdit.setMinimumSize(QSize(300, 25))
        self.lineNameEdit.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.lineNameEdit, 1, 1, 1, 1)

        self.__grip = QLabel(self.inputBox_2)
        self.__grip.setObjectName(u"__grip")

        self.gridLayout_5.addWidget(self.__grip, 8, 1, 1, 1)

        self.linePhoneEdit = QLineEdit(self.inputBox_2)
        self.linePhoneEdit.setObjectName(u"linePhoneEdit")
        self.linePhoneEdit.setMinimumSize(QSize(150, 25))
        self.linePhoneEdit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.linePhoneEdit, 5, 1, 1, 1)

        self.labelCPFEdit = QLabel(self.inputBox_2)
        self.labelCPFEdit.setObjectName(u"labelCPFEdit")

        self.gridLayout_5.addWidget(self.labelCPFEdit, 4, 0, 1, 1)

        self.labelNameEdit = QLabel(self.inputBox_2)
        self.labelNameEdit.setObjectName(u"labelNameEdit")

        self.gridLayout_5.addWidget(self.labelNameEdit, 1, 0, 1, 1)

        self.consultSelectEdit = QComboBox(self.inputBox_2)
        self.consultSelectEdit.addItem("")
        self.consultSelectEdit.addItem("")
        self.consultSelectEdit.setObjectName(u"consultSelectEdit")
        self.consultSelectEdit.setMinimumSize(QSize(150, 26))
        self.consultSelectEdit.setMaximumSize(QSize(150, 26))

        self.gridLayout_5.addWidget(self.consultSelectEdit, 9, 1, 1, 1)

        self.labelSurnameEdit = QLabel(self.inputBox_2)
        self.labelSurnameEdit.setObjectName(u"labelSurnameEdit")

        self.gridLayout_5.addWidget(self.labelSurnameEdit, 2, 0, 1, 1)

        self.lineBornDateEdit = QDateEdit(self.inputBox_2)
        self.lineBornDateEdit.setObjectName(u"lineBornDateEdit")
        self.lineBornDateEdit.setMinimumSize(QSize(150, 26))
        self.lineBornDateEdit.setMaximumSize(QSize(150, 26))
        self.lineBornDateEdit.setAlignment(Qt.AlignCenter)
        self.lineBornDateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_5.addWidget(self.lineBornDateEdit, 6, 1, 1, 1)

        self.labelConsultEdit = QLabel(self.inputBox_2)
        self.labelConsultEdit.setObjectName(u"labelConsultEdit")

        self.gridLayout_5.addWidget(self.labelConsultEdit, 9, 0, 1, 1)

        self.labelBornDateEdit = QLabel(self.inputBox_2)
        self.labelBornDateEdit.setObjectName(u"labelBornDateEdit")

        self.gridLayout_5.addWidget(self.labelBornDateEdit, 6, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_5)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.verticalLayout_19.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_6)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)


        self.horizontalLayout_14.addWidget(self.inputBox_2)


        self.verticalLayout_20.addWidget(self.inputBox2, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.editPage)
        self.queriesPage = QWidget()
        self.queriesPage.setObjectName(u"queriesPage")
        self.horizontalLayout_9 = QHBoxLayout(self.queriesPage)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.appointmentNew = QFrame(self.queriesPage)
        self.appointmentNew.setObjectName(u"appointmentNew")
        self.appointmentNew.setMaximumSize(QSize(550, 500))
        self.appointmentNew.setFrameShape(QFrame.StyledPanel)
        self.appointmentNew.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.appointmentNew)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.appointmentTitle = QLabel(self.appointmentNew)
        self.appointmentTitle.setObjectName(u"appointmentTitle")

        self.verticalLayout_16.addWidget(self.appointmentTitle, 0, Qt.AlignHCenter)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(30)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.appointmentLabelName = QLabel(self.appointmentNew)
        self.appointmentLabelName.setObjectName(u"appointmentLabelName")

        self.verticalLayout_12.addWidget(self.appointmentLabelName)

        self.appointmentLabelCPF = QLabel(self.appointmentNew)
        self.appointmentLabelCPF.setObjectName(u"appointmentLabelCPF")

        self.verticalLayout_12.addWidget(self.appointmentLabelCPF)

        self.appointmenLabelDate = QLabel(self.appointmentNew)
        self.appointmenLabelDate.setObjectName(u"appointmenLabelDate")

        self.verticalLayout_12.addWidget(self.appointmenLabelDate)

        self.appointmentLabelHour = QLabel(self.appointmentNew)
        self.appointmentLabelHour.setObjectName(u"appointmentLabelHour")

        self.verticalLayout_12.addWidget(self.appointmentLabelHour)

        self.labelGrip = QLabel(self.appointmentNew)
        self.labelGrip.setObjectName(u"labelGrip")

        self.verticalLayout_12.addWidget(self.labelGrip)


        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.appointmentName = QLineEdit(self.appointmentNew)
        self.appointmentName.setObjectName(u"appointmentName")
        self.appointmentName.setMinimumSize(QSize(290, 25))
        self.appointmentName.setMaximumSize(QSize(290, 16777215))

        self.verticalLayout_4.addWidget(self.appointmentName)

        self.appointmentCPF = QLineEdit(self.appointmentNew)
        self.appointmentCPF.setObjectName(u"appointmentCPF")
        self.appointmentCPF.setMinimumSize(QSize(290, 25))
        self.appointmentCPF.setMaximumSize(QSize(290, 16777215))
        self.appointmentCPF.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_4.addWidget(self.appointmentCPF)

        self.appointmentDate = QDateEdit(self.appointmentNew)
        self.appointmentDate.setObjectName(u"appointmentDate")
        self.appointmentDate.setMinimumSize(QSize(150, 26))
        self.appointmentDate.setMaximumSize(QSize(150, 16777215))
        self.appointmentDate.setAlignment(Qt.AlignCenter)
        self.appointmentDate.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.appointmentDate.setDateTime(QDateTime(QDate(2023, 1, 15), QTime(0, 0, 0)))
        self.appointmentDate.setDate(QDate(2023, 1, 15))

        self.verticalLayout_4.addWidget(self.appointmentDate, 0, Qt.AlignLeft)

        self.appointmentHour = QTimeEdit(self.appointmentNew)
        self.appointmentHour.setObjectName(u"appointmentHour")
        self.appointmentHour.setMinimumSize(QSize(150, 26))
        self.appointmentHour.setMaximumSize(QSize(150, 25))
        self.appointmentHour.setAutoFillBackground(False)
        self.appointmentHour.setAlignment(Qt.AlignCenter)
        self.appointmentHour.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_4.addWidget(self.appointmentHour, 0, Qt.AlignLeft)

        self.appointmentConfirmBtn = QPushButton(self.appointmentNew)
        self.appointmentConfirmBtn.setObjectName(u"appointmentConfirmBtn")
        self.appointmentConfirmBtn.setMinimumSize(QSize(290, 25))
        self.appointmentConfirmBtn.setMaximumSize(QSize(290, 25))
        self.appointmentConfirmBtn.setStyleSheet(u"image: url(:/icons/images/icons/cil-check.png);")

        self.verticalLayout_4.addWidget(self.appointmentConfirmBtn)


        self.horizontalLayout_11.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.verticalLayout_16.addLayout(self.horizontalLayout_11)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)


        self.horizontalLayout_9.addWidget(self.appointmentNew)

        self.stackedWidget.addWidget(self.queriesPage)
        self.clientPage = QWidget()
        self.clientPage.setObjectName(u"clientPage")
        self.verticalLayout_8 = QVBoxLayout(self.clientPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.clientMenu = QFrame(self.clientPage)
        self.clientMenu.setObjectName(u"clientMenu")
        self.clientMenu.setMinimumSize(QSize(0, 70))
        self.clientMenu.setFrameShape(QFrame.StyledPanel)
        self.clientMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.clientMenu)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addBtn = QPushButton(self.clientMenu)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(75, 50))
        self.addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addBtn.setStyleSheet(u"image: url(:/icons/images/icons/cil-user-follow.png);")

        self.horizontalLayout_7.addWidget(self.addBtn)

        self.delBtn = QPushButton(self.clientMenu)
        self.delBtn.setObjectName(u"delBtn")
        self.delBtn.setMinimumSize(QSize(75, 50))
        self.delBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delBtn.setStyleSheet(u"image: url(:/icons/images/icons/cil-user-unfollow.png);")

        self.horizontalLayout_7.addWidget(self.delBtn)

        self.editBtn = QPushButton(self.clientMenu)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setMinimumSize(QSize(75, 50))
        self.editBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editBtn.setStyleSheet(u"image: url(:/icons/images/icons/cil-pencil.png);\n"
"")

        self.horizontalLayout_7.addWidget(self.editBtn)

        self.reloadBtn = QPushButton(self.clientMenu)
        self.reloadBtn.setObjectName(u"reloadBtn")
        self.reloadBtn.setMinimumSize(QSize(75, 50))
        self.reloadBtn.setStyleSheet(u"image: url(:/icons/images/icons/cil-loop-circular.png);")

        self.horizontalLayout_7.addWidget(self.reloadBtn)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addWidget(self.clientMenu)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.searchBox = QLineEdit(self.clientPage)
        self.searchBox.setObjectName(u"searchBox")
        self.searchBox.setMinimumSize(QSize(375, 26))
        self.searchBox.setMaximumSize(QSize(375, 16777215))

        self.horizontalLayout_6.addWidget(self.searchBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.clientsTable = QTableWidget(self.clientPage)
        if (self.clientsTable.columnCount() < 11):
            self.clientsTable.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.clientsTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.clientsTable.setObjectName(u"clientsTable")
        self.clientsTable.setStyleSheet(u"color: rgb(40, 44, 52);")
        self.clientsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.clientsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.clientsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.clientsTable.setTextElideMode(Qt.ElideNone)
        self.clientsTable.setShowGrid(True)
        self.clientsTable.setGridStyle(Qt.SolidLine)
        self.clientsTable.horizontalHeader().setVisible(True)
        self.clientsTable.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.clientsTable)

        self.stackedWidget.addWidget(self.clientPage)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(False)
        font2.setItalic(False)
        self.creditsLabel.setFont(font2)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_5.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeBtn.setText("")
        self.clientsBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.appointmentBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"My first beautiful interface :)", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.registerTitle.setText(QCoreApplication.translate("MainWindow", u"Dados cadastrais", None))
        self.lineCPF.setText("")
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.labelEmail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.confirmRegisterBtn.setText("")
        self.labelBornDate.setText(QCoreApplication.translate("MainWindow", u"Nascimento", None))
        self.labelPhone.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.genderSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"----------", None))
        self.genderSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.genderSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.labelCPF.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.labelSurname.setText(QCoreApplication.translate("MainWindow", u"Sobrenome", None))
        self.labelGender.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.editTitle.setText(QCoreApplication.translate("MainWindow", u"Editando dados", None))
        self.confirmeditBtn.setText("")
        self.labelGenderEdit.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.lineCPFEdit.setText("")
        self.genderSelectEdit.setItemText(0, QCoreApplication.translate("MainWindow", u"----------", None))
        self.genderSelectEdit.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.genderSelectEdit.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.labelPhoneEdit.setText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.labelEmailEdit.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.__grip.setText("")
        self.labelCPFEdit.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.labelNameEdit.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.consultSelectEdit.setItemText(0, QCoreApplication.translate("MainWindow", u"NAO", None))
        self.consultSelectEdit.setItemText(1, QCoreApplication.translate("MainWindow", u"SIM", None))

        self.labelSurnameEdit.setText(QCoreApplication.translate("MainWindow", u"Sobrenome", None))
        self.labelConsultEdit.setText(QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.labelBornDateEdit.setText(QCoreApplication.translate("MainWindow", u"Nascimento", None))
        self.appointmentTitle.setText(QCoreApplication.translate("MainWindow", u"Marcar consulta", None))
        self.appointmentLabelName.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.appointmentLabelCPF.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.appointmenLabelDate.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.appointmentLabelHour.setText(QCoreApplication.translate("MainWindow", u"Hora", None))
        self.labelGrip.setText("")
        self.appointmentDate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.appointmentConfirmBtn.setText("")
        self.addBtn.setText("")
        self.delBtn.setText("")
        self.editBtn.setText("")
        self.reloadBtn.setText("")
        self.searchBox.setText("")
        ___qtablewidgetitem = self.clientsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.clientsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.clientsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sobrenome", None));
        ___qtablewidgetitem3 = self.clientsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem4 = self.clientsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nascimento", None));
        ___qtablewidgetitem5 = self.clientsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem6 = self.clientsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Consulta", None));
        ___qtablewidgetitem7 = self.clientsTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Dia", None));
        ___qtablewidgetitem8 = self.clientsTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem9 = self.clientsTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem10 = self.clientsTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: GeisielMelo", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"version 0.1 Beta", None))
    # retranslateUi

