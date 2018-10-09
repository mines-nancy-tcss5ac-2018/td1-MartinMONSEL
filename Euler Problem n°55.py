def solve(n):
    "Solve the 55th Euler Problem -- Nombres de Lychrel inférieurs à n"
    L=[]
    for k in range(1,n):
        i=k+Reverse(k)
        
        incr=1
        while not Palindrome(i) and incr<50:
            i+=Reverse(i)
            incr+=1
        if incr>=50:
            L.append(k)
    return(len(L),L)
        
    
    



def Palindrome(k):
    "Teste si le nombre k est un palindrome"
    K=str(k)
    OK=True
    
    while OK and len(K)>=1 :
        if K[0]==K[len(K)-1]:
            K=K[1:len(K)-1]
        else:
            OK=False
    return(OK)
    
def Reverse(k):
    "Renvoie le nombre à l'envers"
    K=str(k)
    L=0
    for i in range(0,len(K)):
        L+=int(K[i])*(10**i)
    return(L)
    
    