from datetime import datetime, timedelta


class Datas:

    def __init__(self):
        self.momento_do_cadastro = datetime.today()

    def __str__(self):
        return self.formatado_data()

    def mes_cadastro(self):
        meses_do_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
                        'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                        'Outubro', 'Novembro']

        mes_cada = self.momento_do_cadastro.month - 1
        return meses_do_ano[mes_cada]

    def dia_semana(self):
        dia_da_semana = ['Segunda', 'Terça',
                         'Quarta', 'Quinta', 'Sexta', 'Sábado'
                         'Domingo']

        dia_cada = self.momento_do_cadastro.weekday()
        return dia_da_semana[dia_cada]

    def formatado_data(self):
        data_formatada = self.momento_do_cadastro.strftime('%d/%m/%y - %H:%M')
        return data_formatada

    def tempo_cadastro(self):
        tempo_cada = (datetime.today() + timedelta(days=30)) - self.momento_do_cadastro
        return tempo_cada


