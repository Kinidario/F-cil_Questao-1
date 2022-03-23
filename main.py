#Função
def repetir(n, texto):
#Criando a variável local
  vetor = []
#Estrutura de repetição para adicionar a string no vetor
  for i in range(0,n):
    vetor.append(texto)
 #Retornando o vetor
  return vetor
  
#Corpo principal do código
#Recebendo as variáveiis
n = int(input("Digite um numero : "))
texto = input("Digite algo : ")
#A variável palavras receberá o vetor retornado na função
palavras = repetir(n, texto)

print(palavras)
