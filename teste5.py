# A função deverá receber um array de inteiros como parâmetro e deverá retornar o mesmo array ordenado em ordem crescente.
# Ex: Input: [5,1,0,7,3,3] - Output: [0,1,3,3,5,7]
 
# param array $array - Array a ser ordenado
# return array

# function ordenarArray(array $array):array{}

 
def ordenarArray(array):
  ordemCrescente = []

  while array:
    numero = min(array)
    ordemCrescente.append(numero)
    array.remove(numero)
  
  array = [ordemCrescente]
  return array

array1 = [4, 6, 7, 3, 20, 1]
array1 = [ordenarArray(array1)]

print("A ordem crescente ficou: ",array1)