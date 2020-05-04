
# Llamar al metodo sumar del archivo operaciones
import operaciones
fileRef = open('resultados.txt', 'a+')
# r=read, w=write, a=append

resultadoSuma = operaciones.sumar(4,8)
operaciones.resultados.append(resultadoSuma)
sumaCadena = str(4)+'+'+str(6)+'='+str(resultadoSuma)+'\n'
fileRef.write(sumaCadena)


print('Resultado de la suma es: '+str(resultadoSuma))

resultadoResta = operaciones.restar(6,4)
operaciones.resultados.append(resultadoResta)
restaCadena = str(4)+'-'+str(6)+'='+str(resultadoResta)+'\n'
fileRef.write(restaCadena)

print('Resultado de la resta es: '+str(resultadoResta))
print(str(operaciones.resultados))