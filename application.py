import random #Se importa la función random

aleatorio = random.randint(1,20) #genera un número aleatorio de 1 a 20
guess = input("Welcome, guess the number: ") #Le pide al usuario que ingrese un número

if guess > aleatorio: #compara los valores del usuario y el aleatorio y asume que la respuesta es mayor
	print "you guessed to high, please try again"
elif guess < aleatorio: #compara la respuesta del usuario y el aleatorio, asumiendo que la del usuario es menor
	print "you guessed to low, please try again"
elif guess == aleatorio: #compara ambos valores dados, y asume que ambos son el mismo número
	print "you win"

print aleatorio #me sirve para verificar que el aleatorio efectivamente es menor o mayor (este es temporal)
