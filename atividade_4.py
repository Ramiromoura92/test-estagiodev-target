faturamento_por_estado = {"SP":67836.43,"RJ":36678.66,"MG":29229.88,"ES":27165.48,"Outros":19849.53}

total = sum(faturamento_por_estado.values())

print("Faturamento total mensal: ",total)

faturamento_por_estado_percent = {"SP":0,"RJ":0,"MG":0,"ES":0,"Outros":0}

for key in faturamento_por_estado.keys():

    faturamento_por_estado_percent[key] = faturamento_por_estado[key]/total*100

print("Faturamento percentual mensal por estado (em %): ",faturamento_por_estado_percent)
