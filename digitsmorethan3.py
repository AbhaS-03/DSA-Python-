n = 12312778132

freq= [0] * 10
k=3
while n != 0:
    last_digit = n %10
    freq[last_digit] +=1
    n//=10

for i in range(len(freq)):
    if k <= freq[i]:
        print(i,"->", freq[i])
