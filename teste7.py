#A função deverá receber uma string e substituir todas as vogais da mesma pelo sinal '?'
# Ex: input: 'Bar' - output: 'B?r'

# param string $string
# return string


def substituirCaracteres(string):
  vogais = "aeiou"
  palavraNova = ""

  for letra in string:
    if letra in vogais:
      palavraNova += "?"

    else:
      palavraNova += letra

  return palavraNova


string1 = "ola tudo bem"

resultado = substituirCaracteres(string1)


print(f"A palavra {palavra1}, ficou da forma nova: ",resultado)