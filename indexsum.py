# even 
def even(l):
    total= 0
    for i in range(0,len(l),2):
        total += l[i]
    return total
l = [ 10,20,30,40 ,50]
print(even(l))