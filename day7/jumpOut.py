# break语句
# continue语句

i = 1
count = 0
for i in range(11):
    if i==6:
        break;
    else:
        count += i
print(count)



i = 1
count = 0
for i in range(11):
    if i==6:
        continue;
    else:
        count += i
print(count)