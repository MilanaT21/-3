N = int(input())
synonyms = {}
for _ in range(N):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1

word_search = input("Введите слово для поиска синонима: ")
if word_search in synonyms:
    print(synonyms[word_search])
else:
    print("Данное слово отсутствует в словаре.")

print(synonyms)