N = int(input())
M = int(input())
semolina = set()    # semolina - манная
oatmeal = set()     # oatmeal - овсяная

print("Фамилии детей, любящих манную кашу:")
for _ in range(N):
    semolina.add(input())
print("Фамилии детей, любящих овсяную кашу:")
for _ in range(M):
    oatmeal.add(input())
both = semolina & oatmeal
if both:
    print(len(both))
else:
    print("Таких нет")




