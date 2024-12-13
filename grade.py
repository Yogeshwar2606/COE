print("enter project score")
project=int(input())
print("enter internal score")
internal=int(input())
print("enter external score")
external=int(input())
if project>=50 and internal>=50 and external>=50:
   total=0.7*project+0.10*internal+0.20*external
   if total>=90:
       print("A")
   elif total>80:
       print("B")
   else:
       print("c")
else:
   if project<50:
       print("failed in project and score is:",project)
   if external<50:
       print("failed in external and score is:",external)
   if internal<50:
       print("failed in internal and score is:",internal)