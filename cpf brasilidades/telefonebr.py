import re


class Telefone:
    def __init__(self,telefone):
        if self.validatell(telefone):
            self.numero = telefone
        else:
            raise ValueError("Digite um numero de telefone correto")

    def __str__(self):
        return self.num_formatado()

    def validatell(self,telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resp = re.findall(padrao,telefone)
        if resp:
            return True
        else:
            return False

    def num_formatado(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resp = re.search(padrao, self.numero)
        numero_formatado = f'+{resp.group(1)} ({resp.group(2)}) {resp.group(3)}-{resp.group(4)}'
        return numero_formatado


