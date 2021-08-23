#python 3.7.1
#SURESH SAHU 1901CE52
def get_memory_score(input_l):
  lis_2=[]
  count=0
  for x in input_l:
     if x in lis_2:
      count+=1
     else:
      lis_2.append(x)
      if len(lis_2)==6:
         lis_2.remove(lis_2[0])
  return count

def is_digit(input_li):
  invalid_list=[]
  ok=True
  for x in input_li:
    if type(x)==int and x<10 and x>=0:
      continue
    else:
      invalid_list.append(x)
      ok=False
  
  if ok:
   return True
  else:
   print ("Please enter a valid input list")
   print ("Invalid inputs detected:", invalid_list)
   return False

input_list=[3, 4, 5, 3, 2, 1]
s=is_digit(input_list)
if s:
  print ("Score:",get_memory_score(input_list))

