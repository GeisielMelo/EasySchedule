import re

from database.dbSearch import SearchDB


def checkThisCPF(self, cpf: str):
    cpf = cpf.replace(".", "").replace("-", "")
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum([int(cpf[i]) * (10 - i) for i in range(9)])
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Verifica o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = sum([int(cpf[i]) * (11 - i) for i in range(10)])
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verifica o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    return True


class InputVerify:
    @staticmethod
    def format_cel_number(text):
        # Remove os caracteres que não são dígitos e salva o tamanho original.
        original_length = len(text)
        text = re.sub(r'\D', '', text)

        # Verifica se o número de telefone tem pelo menos 10 dígitos
        if len(text) == 11:
            text = text[:2] + ' ' + text[2:3] + text[3:7] + '-' + text[7:]
        elif len(text) == 10:
            text = text[:2] + ' ' + text[2:6] + '-' + text[6:]

        # Adiciona qualquer caractere removido à direita do número
        if len(text) < original_length:
            text += ' ' + text[original_length - 1:]

        return text

    @staticmethod
    def format_cpf(text):
        # Remove todos os caracteres que não são dígitos
        text = re.sub(r'\D', '', text)

        # Verifica se o número digitado tem 11 dígitos
        if len(text) == 11:
            # Insere os caracteres de formatação nas posições corretas
            text = (
                text[:3] + '.' + text[3:6] + '.' + text[6:9] + '-' + text[9:])
        return text


class CheckAppointment:
    def isFilled(self, user_input: tuple) -> bool:
        for item in user_input:
            if item == '':
                return False
        return True

    def isCpfValid(self, user_input: tuple) -> bool:
        cpf = user_input[1]
        if not checkThisCPF(self, cpf):
            return False
        return True

    def isCpfInDB(self, user_input: tuple):
        cpf = user_input[1]
        if SearchDB.searchCPF(cpf):
            return True
        return False


class CheckRegister:
    def isFilled(self, user_input: tuple) -> bool:
        for item in user_input:
            if item == '':
                return False
        return True

    def isCpfValid(self, user_input: tuple) -> bool:
        cpf = user_input[3]
        if not checkThisCPF(self, cpf):
            return False
        return True

    def isPhoneValid(self, user_input: tuple) -> bool:
        phone = user_input[4]
        if len(phone) < 12:
            return False
        return True

    def isCpfInDB(self, user_input: tuple):
        cpf = user_input[3]
        if SearchDB.searchCPF(cpf):
            return True
        return False
