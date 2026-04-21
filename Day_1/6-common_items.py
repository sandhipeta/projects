num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]
result = []
for i in range(len(num1)):
    for j in range(len(num2)):
        if num1[i] == num2[j]:
            result.append(num1[i])

result.sort()

print(result)