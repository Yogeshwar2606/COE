print("welcome to my bank")
class Bank:
   totalbalance=50000
   ope=3
   def viewoptions(self):
       print("1.deposite")
       print("2.withdraw")
       print("3.Balance Enquiry")
       print("0.exit")

   def pin(self):
       x=8657

       for i in  range(0,3):
           y = int(input("enter pin number"))
           if(i==2):
               print("card is blocked for today")
           if(x==y):
               obj.viewoptions()
               break

           else:
               print("entered invalid pin")


   def deposite(self):
       x=int(input("enter the money to deposite:"))
       if x>100 and x%100==0 and x<=50000:
           y=x+self.totalbalance
           print(y)
           self.totalbalance=y

       else:
           print("amount should be greater then 100 and amount deposite should be less then 50k and amount multiples of 100")
   def withdraw(self):
       x=int(input("enter the money to withdraw:"))
       if x<self.totalbalance and x>=100 and x%100==0 and self.totalbalance>=500 and x<=20000:
           if self.ope==0 :
               print("Not more than 3 times")
               return
           y=self.totalbalance-x
           print(y)
           self.ope-=1
           print("you left with",self.ope,"times")
           self.totalbalance=y
       else:
           print("amount should be greater then 100")



   def enquirybalance(self):
       print(self.totalbalance)
   def exit(self):
       print("you selected exit operation")

       exit(0)
obj=Bank()
obj.pin()
while True:
   choice=int(input("enter the operation:"))
   if choice==1:
       obj.deposite()
   elif choice==2:
       obj.withdraw()
   elif choice==3:
       obj.enquirybalance()
   else:
       obj.exit()