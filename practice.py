"""
연습문제
"""

List = ["Life", "is", "too", "short"]
result = " ".join(List)
print(result)

a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print("need")
else:
    print('none')



count = 1
while count <= 4:
    print("*" * count)
    count += 1
    if count > 4:
        break


a = "mutzangesazachurum"
b = "aeiou"
count = 0
for i in a:
    if i in b:
        count += 1
print(count)

