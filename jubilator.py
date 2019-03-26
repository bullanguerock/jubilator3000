#jubilator 3000
                
import variables
from datetime import date

print('Ejecutable de calculo de pension sistema previcional')

print('Mes de nacimiento')
mes = 3 #input()
print('Año de nacimiento')
ano = 1993 #input()

#calculo edad
hoy = date.today()
if (mes <= hoy.month):
    e =  hoy.year - ano #float(input())
else:
    e = hoy.year - ano - 1

print('Ingrese su sexo(m=masculino, f=femenino)')
s = 'm' #input()

print('Ingrese su remuneracion mensual')
rm = 500000 #float(input())

print('Ingrese monto ahorrado en su cuenta previsional')
aa = 0 #float(input())

#Calculos
#años restantes para jubilar
#años de vida esperados para recibir jubilacion
if (s == 'm'):
    ar = variables.EJ[0] - e
    av = float(variables.EV[0] - variables.EJ[0]) 
else:
    ar = varibales.EJ[1] - e
    av = float(variables.EV[1] - variables.EJ[1]) 
print('años restantes para jubilar: ',ar)

#Ahorro total
at = (((rm*12*ar)*0.1)+aa)
#print(at)

#ahorro * rentabilidad
atr = at * variables.RP
#print(atr)

#calculo pension
p = ((atr/av)/12)
print('Pension total', int(p))

print('Ingrese APV ya ahorrado en pesos:')
apva = 0 #float(input())

print('Ingrese APV mensual en pesos:')
apv = 50000 #float(input())

#calculo APV
#ahorro apv * rentabilidad
aapv = ((apv*12*ar)+apva)*variables.RP
#print(aapv)
#comisiom afp apv
caapv = (aapv *(1 - variables.CAPV ))
#print(caapv)
papv = ((caapv/av)/12.00)
#print(papv)
tapv = p + papv
print('Pension total con APV', int(tapv))

#Jubilacion esperada
print('Ingrese jubilacion esperada:')
je = 500000 #input()

rest = je-p
apvj = (((((rest*12*av)/ variables.RP)*1.005)/12)/39)
print(apvj)
print('Para tener una jubilacion esperada de: ', je, ', debes ahorrar mensualmente, ', apvj,' pesos.') 


