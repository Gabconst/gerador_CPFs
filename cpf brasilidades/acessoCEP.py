import requests


class BuscaCep:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP Inválido!')

    def __str__(self):
        return self.formatado_CEP()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formatado_CEP(self):
        return f'{self.cep[:5]}-{self.cep [5:]}'

    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )






