import pandas as pd
from datetime import datetime
import os

class GerenciarDados:
    arquivo_dados = 'historico_credito.csv'

    def __criar_arquivo(self):
        df = pd.DataFrame(columns=
                          ['Idade',
                           'Salario',
                           'Valor Solicitado',
                           'Nome Limpo',
                           'Status',
                           'Data']
                          )
        df.to_csv(self.arquivo_dados, index=False)

    def salvar_novo_dado(self, idade:int, salario:float, valor:float, nome_limpo:int, status:str):
        if not os.path.exists(self.arquivo_dados):
            self.__criar_arquivo()
        data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        nova_linha = pd.DataFrame([{'Idade': idade, 'Salario': salario, 'Valor Solicitado': valor,
                      'Nome Limpo': nome_limpo, 'Status': status, 'Data': data}])
        nova_linha.to_csv(self.arquivo_dados, mode='a', index=False, header=False)
        print('Salvo com sucesso!')
