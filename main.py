
'''#palindrome finder
x=str(input("what is your word?"))
y=list(x)
z=x[0]
a=[-1]

for i in range ((int)(len(y)/2)):
  
  if y[i]!=y[-(i+1)]:
    print("False")
  else:  
    print("True")

#faction simplifyer
div=list(input("what is your division equaition?"))
x=int(div[0])
y= int(div[2])
d = int(x/y)
r = x%y
if r==0:
  print(d)
else:
  print(d,"(",r,"/",y,")")

#find the b biggest number in n ammount of numbers
n=list(input("what is your list of numbers?"))
b=int(input("which place biggest number?"))
g=sorted(n)
print(g[-b])

#letter swapper
n=list(input("what is your word?"))
k=int(input("what is the postion of the elements you want swapped? "))
if k>len(n):
  print("item is out of range")  
#https://www.kirupa.com/html5/swapping_items_array_js.htm
else:
  t=n[k-1] # temp storage
  n[k-1] = n[-k] #move one of the elements
  n[-k] = t # move temp storage to the other element
  print(n)

#element sticher
h=list(input("what are your numbers?(no spaces or commas)"))
a=h[i]
b=h[-i]
for i in range (len(h)):'''
'''
#meteric coversion distance calculator
cm=1
m=cm*100
km=cm*1000
value=int(input("from value"))
convert_from = str(input("what do you want to convert?"))
convert_to = str(input("what are you converting to?"))
result = 0
if convert_from == "meters":
    if convert_to == "centimeters":
        result = value*100
    if convert_to == "kilometers":
        result = value/1000

if convert_from == "kilometers":
    if convert_to == "centimeters":
        result = value*100*1000
    if convert_to == "meters":
        result = value*1000

if convert_from == "centimeters":
    if convert_to == "kilometers":
        result = value/1000/100
    if convert_to == "meters":
        result = value/100
  
print (result)'''


#implementation using switch technique
def switch():
  cval = int(input("Enter a value"))
  cfrom = str(input("What do you want to convert "))
  cto = str(input("What do you converting to? "))

  def meters():
    if cto == "centimeters":
        print(cval*100)
    if cto == "kilometers":
        print(cval/1000)

  def kilometers():
    if cto == "centimeters":
        print(cval*100*1000)
    if cto == "meters":
        print(cval*1000)

  def centimeters():
    if cto == "kilometers":
        print(cval/1000/100)
    if cto == "meters":
        print(cval/100)

  def feet():
    if cto=="centimeters":
      print(cval*30)
    if cto=="meters":
      print(cval*30/100)
    if cto=="kilometers":
      print(cval*30/1000)
    if cto=="inches":
      print(cval*12)

  def inches():
    if cto=="centimeters":
      print(cval*2.5)
    if cto=="meters":
      print(cval*2.5*100)
    if cto=="kilometers":
      print(cval*2.5*1000)
    if cto=="feet":
      print(cval/12)
    if cto=="yards":
      print(cval/12*3)

  def yards():
    if cto=="centimeters":
      print(cval/3*30*3)
    if cto=="meters":
      print(cval/3*30*3*100)
    if cto=="kilometers":
      print(cval/3*30*3*100*10)

  def default():
    print("invalid option")

  dict = {
        "centimeters" : centimeters,
        "meters" : meters,
        "kilometers" : kilometers,
        "feet" : feet,
        "inches" : inches,
        "yards" : yards
    }
  dict.get(cfrom,default)() # get() method returns the function matching the argument
 
switch()