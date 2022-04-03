"""
과제1 While
"""

#과제 1-1
i = 0
result = 0
while i < 1000:
    i += 1
    if i%3 == 0:
        result += i
print(result)

#과제 1-2
count = 10
while count >= 1:
    print("*" * count)
    count = count - 1
    if count == 0:
        break

#과제 1-3
"""
실패작
# listA = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# sum=0
# index=0
# while 0 < len(listA):
#     index += 1
#     if listA.pop() >= 50:
#         sum += listA.pop()
#         print(index)
# print(sum)
"""
listA = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum=0
index=0
while index < len(listA)-1:
    index += 1
    if listA[index] >= 50:
        sum += listA[index]
        # print(index)
print(sum)

listA = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum=0
index=0
while len(listA) > 0:
    temp_var = listA.pop()
    if temp_var >= 50:
        # print(listA)
        sum += temp_var
print(sum)


"""
과제2 For
"""
#과제 2-1
i = 0
list = []
while i < 100:
    i += 1
    list.append(i)
for i in list:
    print(i)

#과제 2-2
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
index = 0
sum = 0
for i in A:
    while index < len(A):
        sum += A[index]
        index += 1
print(sum / len(A))

#과제 2-3
numbers = [1, 2, 3, 4, 5]
result1 = [n*2 for n in numbers if n%2 == 1]
print(result1)

result=[]
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)