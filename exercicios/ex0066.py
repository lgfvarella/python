#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = contador = 0
while True:
    numeros = int(input('Digite 999 para sair ou um número: '))
    if numeros == 999:
        break
    soma += numeros
    contador += 1
print(f'Você digitou {contador} números e a soma deles é {soma}')