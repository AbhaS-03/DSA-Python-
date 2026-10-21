# find maximum value
def get_max(*num):
    if len(num) == 0:
        return None
    max_num = num[0]
    for n in num:
        if n > max_num:
            max_num = n
    return max_num

print(get_max(3,12,14,8,8,91))
print(get_max("Payal", "Arya", "Jiya"))

# find longest string 
def long_str(*s):
    if len(s) == 0:
        return None
    long_sen = s[0]
    for i in len(s):
        if i > long_sen:
            long_sen = i
    return long_sen
print(long_str("Rohan","Era","Rajlaxmi"))