def solve():
    "Solve the 22nd Euler Problem (Names Score)"
    f = open("p022_names.txt", 'r')
    Sommetot=0
    
    Chainepren=f.readlines()
    Chainepren.split(",")
    Listetriee=sorted(Chainepren)
    
    
    for k in range(len(Listetriee)):
        
        Scorelettres=0
        
        for i in range (1,len(Listetriee[k])-1):
            
            Scorelettres+=ord(Listetriee[k][i])
        
        Scorenom=Scorelettres*(k+1)
        
        Sommetot+=Scorenom
    
    f.close()    
    
    return(Sommetot)
    



print("Le score total est",solve())
        
            
            
        
    