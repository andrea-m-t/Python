#CALCULADORA DE AREA SEGUN LA FORMA
import math

# Mensaje de Bienvenida
print ("¡Bienvenido a la Calculadora de Área!")

#Seleccione la forma geométrica
print ("Por favor, seleccione la Forma a calcular.\nA.Triángulo\nB.Cuadrado\nC.Rectángulo\nD.Rombo\nE.Círculo")

entrada=(input()).capitalize()

#Proceso de forma
def proceso (entrada):

    if True:
            if entrada == ("A"):
                print("Ingrese el valor de la Base.")
                base=float(input())
                print("Ingrese el valor de la Altura.")
                altura=float(input())
                calculo=((base*altura)/2)
                print ("El área es " + str(calculo) +".")
            
            if entrada == ("B" or "C"):
                print("Ingrese el valor de la Base.")
                base=float(input())
                print("Ingrese el valor de la Altura.")
                altura=float(input())
                calculo=base*altura
                print ("El área es " + str(calculo) +".")
            
            if entrada == ("D"):
                print("Ingrese el valor del 1er Diámetro.")
                d_1=float(input())
                print("Ingrese el valor del 2do Diámetro.")
                d_2=float(input())
                calculo=((d_1*d_2)/2)
                print ("El área es " + str(calculo) +".")
            
            if entrada == ("E"):
                print("Ingrese el valor del Radio")
                radio=float(input())
                calculo=math.pi*(radio)**2
                print ("El área es " + str(calculo) +".")
    else:
        print("Figura no contemplada.")
    
proceso (entrada)
