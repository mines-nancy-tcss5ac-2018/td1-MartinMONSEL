def solve(doc):
    "Solve the 22th Euler Problem - Score d'un fichier de noms"
    n = 0
    for w in liste(doc):
        s = 0
        for l in w:
            s= s +ord(l)-64
        n = n + s * (liste(doc).index(w)+1)
    return n



def liste(doc):
    "Transforme le fichier en liste de noms - Retire les caractères parasites"
    f = open(doc, 'r')
    L =[]
    for l in f :
        for p in l.split(","):
            L = L + [p[1:-1]]
    L = sorted(L)
    return L

print (solve('p022_names.txt'))
            
            
        
    