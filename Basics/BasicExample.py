#hello world 1st example
#print ("hello World")

# my first python function
def func1():
 print ("I my first func")
 print ("in the func")

#func1 call
func1();

def sqa(num):
 return num*num;


# print (sqa(5))

for x in range(5,11):
 #if (x%2==0): 
  #continue
 print (x)

days=["m", "t", "w"]
#for loop printing both index and value
for i, d in enumerate(days):
 print (i, d)

# for loop printing value
for i in days:
 print (i)

# class declaration
class myClass():
#self is equivalent to this in c++
#function definition
 def meth1(self):
  print ("inside mehtod1 of class")
 def meth2(self, something):
  print ("hi in 2nd mehtod" + something+ "hi"+ "just another example")
#3rd method definition of our class
 def meth3(self):
  print("this is the 3rd method")

#subclass
class anotherClass(myClass): 
 def meth2(self):
  print ("anotherCalass meth2")
 def meth1(self):
  myClass.meth1(self);
  print("another class meth1")

c=myClass();
c.meth1()
c.meth2(" Python uses indentation")
c2=anotherClass()
c2.meth1()
print("\n")

c2.meth2()

print("\n\n\n")
# 
f=open("textFile.txt", "r")

#for i in range(10):
 #f.write("this is line %d \n" % (i+1))
contents=f.read()
print (contents)
f.close()





