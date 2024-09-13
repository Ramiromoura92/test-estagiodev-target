n1 = 0
n2 = 1
fibonnaci = [0,1]

try:
    n = int(input("Digite um valor inteiro:"))
except:
    print("O número precisa ser inteiro")    

while True:
    next_number = n1+n2
    n1, n2 = n2, next_number
    fibonnaci.append(next_number)

    if next_number >= n:
        break

if n in fibonnaci:
    print(f"O número {n} pertence a sequencia")
else:
    print(f"O número {n} não pertence a sequencia")    