# segundo ejercicio calcular las notas promediales
nota1 = float(input("igresa la nota aclificar:"))
nota2 = float(input("igresa la nota aclificar:"))
nota3 = float(input("igresa la nota aclificar:"))

peso1 = 0.20
peso2 = 0.35
peso3 = 0.45

#obtener el promedio de notas
promedio = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)

# imprimir el resultado  final
print("promedio total del estudiante en la asignatura:",promedio)
