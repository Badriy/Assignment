#Q1
#a certain steel is graded according to the following conditions:
#i.Rockwell hardness > 50
#ii.Carbon content > 0.7
#iii.Tensile strength > 5600 kg/cm2
#The steel is graded as follows:
#a. Grade 10, if all the conditions are satisfied
#b. Grade 9, if conditions (i) and (ii) are satisfied
#c. Grade 8, if conditions (ii) and (iii) are satisfied
#d. Grade 7, if conditions (i) and (iii) are satisfied
#e. Grade 0, otherwise
#Draw the flow chart and algorithm steps to solve this problem.


#rh = Rockwell Hardness
#cc = Carbon content
#ts = Tensile strength
   
rh_f=0
cc_f=0
ts_f=0
rh = int(input("Enter the value of Hardness : "))
cc = float(input("Enter the value of Carbon Content: "))
ts = int(input("Enter the value of Tensile Strength: "))
if (rh>50):
 rh_f=1
if (cc>0.7):
 cc_f=1
if (ts>5600):
 ts_f=1
if(rh_f==1 and cc_f==1 and ts_f==1):
#Grade is 10 if all of the conditions are met    
 grade = 10
elif(rh_f==1 and cc_f==1 and ts==0):
#Grade is 9 if condition (i) and (ii) are met      
 grade = 9
elif(rh_f==0 and cc_f==1 and ts_f==1):
#Grade is 8 if conditions (ii) and (iii) are met      
 grade = 8
elif(rh_f==1 and cc_f==0 and ts_f==1):
#Grade is 7 if (i) and (iii)conditions are met      
 grade = 7
else:
#Grade is 0 if non of the conditions are met      
 grade = 0
 
print("The Grade of Steel  :", grade)

