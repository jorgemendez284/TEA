texto = "X-DSPAM-Confidence:0.8475"
inicio = texto.find(":") + 1
final = len(texto)
numero = texto [inicio :final]
print(inicio, final)
print(numero)
print(type(numero))