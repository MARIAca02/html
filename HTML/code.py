
nota_primer_corte = float(input("ingrese la nota de primwer corte:3,6"))
peso_primer_corte = float(input("ingreseel peso del primer corte (en porcentaje):20%"))

nota_segundo_corte = float(input("ingrese la nota de primwer corte:2.9"))
peso_segundo_corte = float(input("ingreseel peso del primer corte (en porcentaje):35%"))

nota_tercero_corte = float(input("ingrese la nota de primwer corte:3,33"))
peso_tercero_corte = float(input("ingreseel peso del primer corte (en porcentaje):45%"))

resultado_primer_corte = nota_primer_corte * (peso_primer_corte /100)
resultado_segundo_corte = nota_segundo_corte * (peso_primer_corte /100)
resultado_tercero_corte = nota_tercero_corte * (peso_primer_corte /100)

suma_resultados = resultado_primer_corte + resultado_segundo_corte + resultado_tercero_corte
promedio_final = suma_resultados
print("promedio de la asignatura->nota final:",promedio_final)

