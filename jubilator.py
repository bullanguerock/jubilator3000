#jubilator 3000
                
import variables
# print(variables.EV)

print('Ejecutable de calculo de pension sistema previcional')
print('Ingrese su edad')
e = float(input())

print('Ingrese su sexo(m=masculino, f=femenino)')
s = input()

print('Ingrese su remuneracion mensual mensual')
rm = float(input())

print('Ingrese monto ahorrado en su cuenta previsional')
aa = float(input())

#Calculos
#años restantes para jubilar
#años de vida esperados para recibir jubilacion
if (s == 'm'):
    ar = variables.EJ[0] - e
    av = variables.EV[0] - variables.EJ[0] 
else:
    ar = varibales.EJ[1] - e
    av = variables.EV[1] - variables.EJ[1] 
print('años restantes para jubilar: ',ar)

#Ahorro total
at = (((rm*12*ar)*0.1)+aa)
print(at)

#ahorro  rentabilidad
atr = at * variables.RP
print(atr)

#calculo pension
p = ((atr/av)/12)
print(int(p))

