# A função deverá receber uma string e retornar a mesma invertida.
#  Ex: input: "bar" - output: "rab"
 
#  param string $string
#  return string


def inverterString(palavra):
  return palavra[::-1]    # Aqui o papel da notação [::-1] e trazer de forma invertida o que esta dentro da variavel


palavra1 = "ola"

invertida = inverterString(palavra1)

print(f"A palavra {palavra1}, na forma invertida fica: ",invertida)