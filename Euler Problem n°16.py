def solve(n):
    "Solve the 16th Euler Problem - Nombre de digits du nombre n"
    S=0
    N=str(n)
    #On transforme le nombre en chaine de caractère
    for k in range(0,len(N)):
        S+=int(N[k])
    return(S)
    
assert(solve(2**15)==26)
print("La somme des digits de 2**1000 est",solve(2**1000))


