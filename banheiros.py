import pandas as pd

planilha_df = pd.read_csv("D:/Users/henrique.moscoso/data.vs/Banheiro+sabonete.csv")                    # "D:/Users/henrique.moscoso/data.vs/ : endereço dell
planilha_df.to_csv('teste.csv')                                                                         

planilha_dic = planilha_df.to_dict('list')            # DataFrame para dicionário

data_sel = input("Qual data deseja verificar o consumo? Separe por / (i.e 01/09/2009): ")
data_sel = data_sel.replace("/","-")
x = data_sel[:2]
data_sel = data_sel.replace(data_sel[:2],data_sel[6:])
data_sel = data_sel[:8] + x                                 # Deixar a data no padrão do DataFrame















