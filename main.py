def repetir(n, texto):
  vetor = []
  for i in range(0,n):
    vetor.append(texto)
  return vetor
  

n = int(input("Digite um numero : "))
texto = input("Digite algo : ")

palavras = repetir(n, texto)

print(palavras)