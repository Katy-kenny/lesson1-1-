example = "Капибара"
print(example[0])
print(example[-1])

a = len(example)

if a % 2 == 0:
    b = a // 2  # Используем целочисленное деление

    print(example[b:])
if a % 2 != 0:
    b = a // 2  # Используем целочисленное деление

    print(example[b-1:])

print(example[::-1])
print(example[1::2])
