# A função recebe um inteiro entre 1 e 12 e retorna o mês correspondente por extenso. Caso o mês informado não esteja entre 1 e 12, deverá ser retornado "Mês Inexistente"
# Ex: input: 1 	- output: "Janeiro"
# Ex: input: 13 	- output: "Mês Desconhecido"
 
#  param int $month
#  return string


mesesAno = {1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}  # Aqui estou criando um dicionário que em php seria igual um array onde chaves recebem valores 

def mesCorrespondente(numero):      # Aqui estou criando uma função com o (def)
    if numero in mesesAno:
      return mesesAno[numero]
    else:
      return "Mês Desconhecido"


numero1 = int(input("Coloque um número entre 1 e 12 para saber qual o mês correspondente: "))  # Variável (numero1) que recebera um inteiro do input

mes = mesCorrespondente(numero1)   # Variável (mês) que recebera o retorno da função (mesCorrespondente)

print(f"O mês correspondente ao número {numero1} é: ",mes)   # Mensagem de saída como resposta com o número e o mês correspondente