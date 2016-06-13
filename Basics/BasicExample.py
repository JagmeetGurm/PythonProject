#hello world 1st example
#print ("hello World")

# my first python function
def func1():
 print ("I my first func")
 print ("in the func")

#func1();

def sqa(num):
 return num*num;


# print (sqa(5))

for x in range(5,11):
 #if (x%2==0): 
  #continue
 print (x)

days=["m", "t", "w"]

for i, d in enumerate(days):
 print (i, d)


# class declaration
class myClass():
 def meth1(self):
  print ("inside mehtod1 of class")
 def meth2(self, something):
  print ("hi in 2nd mehtod" + something)


c=myClass();
c.meth1()
c.meth2(" hi friends")
