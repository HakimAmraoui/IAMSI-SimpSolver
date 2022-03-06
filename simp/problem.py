import random
from itertools import combinations

# EXERCICE 2

# Le nombre de variables propositionnelles peut est exprimer par
# nb_var_prop =  factorial(ne) * nj
var = []



def coding(ne, nj, j, x, y):
    return j * (ne ** 2) + x * ne + y + 1

def decoding(k, ne):

    j = k / ne**2

    x = (k - j*ne**2) / ne
    y = ((k % ne**2) % ne) - 1
    return j, x, y

k = coding(1, 2, 3, 3, 1)



### EXERCICE 3

## Cardinalite
def au_moins(lst):
    ## on return toute la list avec le 0
    clauses = ' '.join(map(str, lst + [0]))
    return clauses

def au_plus(lst):
    ## On fait pair par pair et on inverses les numeros d'equipe
    clauses = [[-i, -j] for i, j in combinations(lst, 2)]
    return [' '.join(map(str, clause + [0])) for clause in clauses]



print(au_moins([4, 3, 2, -5]))
print(au_plus([4, 3, 2, -5]))

## Traduction

def encoderC1(ne, nj):
    sum = 0
    for j in range(nj):
        for e in range(ne):
            sum += var[ coding(ne, nj, j, e, x) ] + var[ coding(ne, nj, j, x, e) ]
    return sum <= 1