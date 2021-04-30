#LIBRERIAS

#Importamos las librerias necesarias, que son la de turtle para poder dibujar y random para los numeros aleatorios
import random						
from turtle import Screen, Turtle


'''

#COFIGURACION DE LOS PARAMETROS DE CREACION DEL ARBOL
print('Para generar el arbol, deberá configurar los parametros iniciales que se muestran a continuación')

#Configuracion de la profundida del fractal
print('\n\nNUMERO DE ITERACIONES (Recomendable un numero entre 8 para mas realismo, en caso de ser mayor que 10 puede tardar mucho más)')	
while True:
	print('Por favor, introduce valores entre 2 y 10')
	PROFUND = int(input('Defina el numero de iteraciones que desea: '))
	if PROFUND >= 2 and PROFUND <= 10:
		break




#Configuracion del grosor
print('\n\nGROSOR INICIAL (Recomendable utilizar 10 para un mayor realismo)')
while True:
	print('Por favor, introduce valores entre 5 y 20')
	SIZE = int(input('Defina el grosor que desea: '))
	if SIZE >= 5 and SIZE <= 20:
		break




#Configuracion del CAOS
print('\n\nPARAMETRO DE ALEATORIEDAD (Recomendable utilizar 1 para un mayor realismo)')		
while True:
	print('Por favor, introduce valores entre 0 y 1')
	CAOS = float(input('Defina el CAOS que desea: '))
	if CAOS >= 0 and CAOS <= 1:
		break



#Configuracion del angulo minimo
print('\n\nANGULO MINIMO (Recomendable utilizar 3 para un mayor realismo)')	
while True:
	print('Por favor, introduce valores entre 2 y 15')
	Angle_min = int(input('Defina el angulo minimo en grados que desea: '))
	if Angle_min >= 2 and Angle_min <= 15:
		break



#Configuracion de la distancia minima
print('\n\nDISTANCIA MINIMA (Recomendable utilizar 5 si ya tiene el CAOS en 1 para un mayor realismo, si no, 30 es recomendable)')	
while True:
	print('Por favor, introduce valores entre 1 y 100')	
	DISTANCE_min = int(input('Defina el angulo minimo que desea: '))
	if DISTANCE_min >= 1 and DISTANCE_min <= 100:
		break

		
'''


PROFUND        = 8
SIZE        = 10
CAOS         = 1
RELACION     = 1.3


DISTANCE = 150
ANGLE_ALPHA = 24
ANGLE_BETHA = 24








#CONDICIONES INICIALES

pen = Turtle()		      #Le ponemos nombre a nuestra tortuga
screen = Screen()		  #Esta condicion es necesaria para la grama cromatica en las hojas
random.seed()			  #Inicializamos el generador de numeros aleatorios

screen.colormode(255)	  #Esta condicion es necesaria para poder pasarle a la gama cromatica los colores RGB

#Posicion inicial 
pen.penup()
pen.goto(0,-375)
pen.pendown()
pen.left(90)
pen.speed(10)

#Color inicial
#random.uniform(a, b) nos devuelve un valor entre a y b
#pen.pencolor recibe 3 parametros de los tres intervalos. Este conjunto de intervalos dos cambia a una gama cromatica marron
#pen.pencolor(int(random.uniform(60, 80)), int(random.uniform(30, 50)),int(random.uniform(10, 30)))	
pen.pencolor(int(random.uniform(50, 80)), int(random.uniform(20, 50)),int(random.uniform(20, 50)))





def rama(SIZE, PROFUND, CAOS, ANGLE_ALPHA, RELACION, DISTANCE, ANGLE_BETHA):
	








	if PROFUND > 0:
		ANGLE_ALPHA   = int(random.uniform(6, 30)) #random.randint(6, 20)   #int(random.uniform((Angle_min+(CAOS*1.5)*PROFUND), (Angle_min+(CAOS*3)*PROFUND)))
		ANGLE_BETHA   = int(random.uniform(6,30))#random.randint(6, 20)   #int(random.uniform((Angle_min+(CAOS*1.5)*PROFUND), (Angle_min+(CAOS*3)*PROFUND)))
		DISTANCE     = int(random.uniform(DISTANCE*0.7, DISTANCE*0.9)) #int(random.uniform((DISTANCE_min+(CAOS*3)*PROFUND), (DISTANCE_min+(CAOS*18)*PROFUND)))
		
		











		pen.pensize(SIZE)
		pen.forward(DISTANCE)
		pen.left(ANGLE_ALPHA) 
		rama(SIZE/RELACION, PROFUND-1, CAOS, ANGLE_ALPHA, RELACION, DISTANCE, ANGLE_BETHA) #Llamada a la recursión
		pen.right(ANGLE_ALPHA + ANGLE_BETHA)
		rama(SIZE/RELACION, PROFUND-1, CAOS, ANGLE_ALPHA, RELACION, DISTANCE, ANGLE_BETHA) #Llamada a la recursión
		pen.left(ANGLE_BETHA)
		pen.backward(DISTANCE)
	
		
	if PROFUND == 0:
		pen.pencolor(0, int(random.uniform(130, 180)),int(random.uniform(70, 140)))	#Cambio de color a gama cromatica aleatoria similar al verde cuando se encuentra en el ultimo nivel ('hojas')
		#pen.color(0, int(random.uniform(130, 180)),int(random.uniform(70, 140)))
		#pen.begin_fill()
		#pen.circle(int(random.uniform(2, 6)))
		#pen.end_fill()
		#pen.pencolor(int(random.uniform(50, 80)), int(random.uniform(20, 50)),int(random.uniform(20, 50)))
	elif PROFUND != 0:
		pen.pencolor(int(random.uniform(50, 80)), int(random.uniform(20, 50)),int(random.uniform(20, 50))) #Cambio de color a gama cromatica aleatoria similar al verde cuando se encuentra en el tronco
		
		
		
		


#Llamada a la recursion
rama(SIZE,PROFUND,CAOS, ANGLE_ALPHA, RELACION, DISTANCE, ANGLE_BETHA)
rama(SIZE-2,PROFUND-2,CAOS, ANGLE_ALPHA+3, RELACION, DISTANCE-50, ANGLE_BETHA+3)


#Espera que el usuario acabe
input()