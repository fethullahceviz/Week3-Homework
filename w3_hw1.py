# PerfectNumbers from 1 to 1000
def perfect_Number(n): 
   sum = 0
   for i in range(1,n):
      if n%i==0:
         sum += i
   return sum == n
filter2=list(filter(perfect_Number, range(1,1001)))
print("PerfectNumbersList between 1-1000 :",filter2)#filtre
print("PerfectNumbersSum  between 1-1000 :",sum(filter2))#sum

