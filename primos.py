"""

Calcular mcm entre dos numeros

proximamente 3

"""

mcm_1 = int(input())
mcm_2 = int(input())

def es_primo(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #de lo contrario devuelve Verdadero


n_primos = [] # numeros primos en la lista

for iss in range(10000):
    r = es_primo(iss)
    if r == True:
        n_primos.append(iss) # busca los numeros primos entre 0 10000 y los pone en n_primos
    else:
        continue

def primo():
    return n_primos

