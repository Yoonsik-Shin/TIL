def d(n):
    if n<100:
        return n+(n//10)+(n%10)
    elif n<1000:
        return n+(n//100)+(n%100//10)+(n%10)
    elif n<=10000:
        return n+(n//1000)+(n%1000//100)+(n%1000%100//10)+(n%10)
        
lst1=[]        
lst2=[]

for i in range(1,10001):
    lst1.append(i)
    lst2.append(d(i))

lst2.sort()

sets1=set(lst1)
sets2=set(lst2)

a = list(sets1-sets2)
a.sort()

for i in a:
    print(i)
