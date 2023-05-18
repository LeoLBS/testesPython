# A função irá receber um array de inteiros e retornar o primeiro elemento não repetido.
#  Ex: input: [2,2,3,1,1,6] - output: 3
 
#  param array $array - Array contendo inteiros
#  return int


def primeiroValorNaoRepetido(array):
  for item in array:
    if array.count(item) == 1:
      return item

array1 = [2,2,4,3,2,1,6,1]

numeroNaoRepetido = primeiroValorNaoRepetido(array1)

print("O valor não repetido da lista é: ", numeroNaoRepetido)