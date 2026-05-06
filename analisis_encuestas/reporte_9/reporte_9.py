import csv

# q10_calidad_internet: id(0) carrera(1) semestre(2) jornada(3) trabaja(4) promedio(5)
# q01(6) q02(7) q03(8) q04(9) q05(10) q06(11) q07(12) q08(13) q09(14) q10(15)
INDICE_INTERNET = 15

# estructura: [nivel, cantidad]
niveles = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
total = 0

with open(
    "../encuesta_ingenieria_10000_respuestas.csv", "r", encoding="utf-8"
) as estudiante:
    encuesta = csv.reader(estudiante)
    next(encuesta)

    for fila in encuesta:
        calidad = int(fila[INDICE_INTERNET].strip())
        total += 1

        for n in niveles:
            if n[0] == calidad:
                n[1] += 1
                break

etiquetas = {1: "Muy mala", 2: "Mala", 3: "Regular", 4: "Buena", 5: "Muy buena"}

for n in niveles:
    print(
        f"Nivel {n[0]} - {etiquetas[n[0]]:<10}: {n[1]:>6}  ({n[1] / total * 100:.2f}%)"
    )

aceptable = sum(n[1] for n in niveles if n[0] >= 3)
print(f"\nCon internet aceptable (>=3): {aceptable}  ({aceptable / total * 100:.2f}%)")
