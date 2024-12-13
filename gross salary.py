basic_salary=float(input("enter the basic salary:"))
if basic_salary<10000:
   HRA=0.67*basic_salary
   DA=0.73*basic_salary
elif basic_salary<20000:
   HRA=0.69*basic_salary
   DA=0.76*basic_salary
else:
   HRA =0.73 * basic_salary
   DA =0.89 * basic_salary
gs=HRA+DA+basic_salary
print("your gross salary  amount:",gs)