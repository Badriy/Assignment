x=["ONE","Red", "Code", "pythin"]
n= int(input("Enter the len(n): "))

def check_words(x,y):
    y= []
    for i in x:
        if len(i) > n:
           y.append(i)
    if len(y) > 0:
        return y  
    else:
        return"No words longer than "+ str(n)
    
print(check_words(x,n))
    