#  Recebe um array de inteiros maiores que zero e retorna a quantidade de números pares existentes no array
#  Ex: input: [1,2,3,4,5] - output: 2
 
#  param array $array
#  return int

def parOuImpar(listaNum):     
  numerosPares = []      
  for numero in listaNum:
    if numero % 2 == 0:
      numerosPares.append(numero)
  return numerosPares


listaNum1 = [1, 2, 20, 5, 11, 4]

quanti = len(parOuImpar(listaNum1))

print("A quantidade de números pares: ",quanti)