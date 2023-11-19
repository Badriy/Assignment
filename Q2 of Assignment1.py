#Q2
# Suppose that the tuition for a university is $10,000 this year and increases 5% every year. In
# one year, the tuition will be $10,500. Write a program that computes the tuition in ten years
# and the total cost of four years’ worth of tuition after the tenth year.

tuition = 10000  
x = 0.05  
years = 10  
i = 0  
current_year = 1
while(current_year <= years):
    tuition = tuition * (1 + x)  
    print("Tuition in year "+str(current_year)+": "+ "$"+str(tuition))
    
    
    if current_year <= 4:
        i+= tuition
    
    current_year += 1


print("Total cost for four years after the tenth year: $"+str(i))
