import json
from statistics import mean


with open('dados.json') as f:
    raw_data = json.load(f)

faturamento_diario = []
faturamento_diario_cleaned =[]

for i in range(len(raw_data)):
    faturamento_diario.append(raw_data[i]['valor'])

print("Faturamento mensal: ", faturamento_diario)

for i in faturamento_diario:
    if i>0:
        faturamento_diario_cleaned.append(i)

print("Faturamento mensal dos dias úteis: ", faturamento_diario_cleaned)


print("Menor faturamento: ",min(faturamento_diario_cleaned))
print("Maior faturamento: ",max(faturamento_diario_cleaned))

count_days = 0

for value in faturamento_diario_cleaned:

    if value > mean(faturamento_diario_cleaned):
        count_days = count_days + 1

print("Média mensal: ",mean(faturamento_diario_cleaned))
print(f"O faturamento foi maior do que média mensal em {count_days} dias")