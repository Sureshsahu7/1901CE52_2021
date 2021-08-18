#python 3.7.1
#1901ce52 Suresh sahu
bount=0
count=0
def meraki_helper(a):
 global count
 global bount
 ok=False
 q=a
 if a<10 and a>-1:
    count+=1
    ok=False
    print("Yes -",q,"is a Meraki number")
    
 else:
    while a>9:
      b=int(a%10)
      a=int(a/10)
      c=int(a%10)
      d=abs(b-c)
      if d==1:
        ok=True
        continue
      elif d!=1:
        print("No -",q,"is not a Meraki number")
        bount+=1
        ok=False
        break
 if ok==True:
    count+=1
    print("Yes -",q,"is a Meraki number")
 
 
#Given input of list
input_list=[12,  14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5,  123,  45, 76345,  987654321]
for i in range(len(input_list)):
 n=int(input_list[i])
 meraki_helper(n)
print("the input list contains",count,"meraki and",bount,"non meraki numbers.")