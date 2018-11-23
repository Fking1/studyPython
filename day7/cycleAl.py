# 冒泡排序 range(x) 即为[0,x)
# range(a,b) 即为[a,b)
list1 = [3,2,6,4,4,8,5,4,1]
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)




