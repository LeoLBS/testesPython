# A função deverá receber um array com pelo menos 3 itens e retornar a média simples de todos os itens do array.
# Caso o array recebido possua menos que 3 itens, deverá ser retornado o boleano false.
# Ex: input: [4,6,8] - output 6
# Ex: input: [1,2] - output false

# param array  notas
# return int|bool


def mediaSimples(array):     # Função para fazer um calculo de média simples
  if len(array) >= 3:        # Aqui o papel do len() é descobrir qual o comprimento do array igual um count()
    return sum(array) / len(array)     # Realizando o calculo da média simples com o sum() onde seu papel é fazer a soma dos números dentro do array
  else:
    return False    


array1 = [70, 80, 90]     

media = mediaSimples(array1)

print("A media simples é de: ",media)