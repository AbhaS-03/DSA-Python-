n = 123128945

freq= [0] * 10
while n != 0:
    last_digit = n %10
    freq[last_digit] +=1
    n//=10

for i in range(len(freq)-1):
    print(i,"->", freq[i])
