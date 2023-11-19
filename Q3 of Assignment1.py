#Q3
#Write a nested for loop that prints the following output: 

S=8
for i in range( 1,  S+1):
    
    
    for j in range (S,i,-1):
        
        print("   ",end=" ")
    for j in range (1,i+1):
        Z=2**(j-1)
        print(Z,end=" ")
        
    for j in range (i-1 ,0 ,-1):
        Z=2**(j-1)
        print(Z, end="  ")
        
    print()
    
        