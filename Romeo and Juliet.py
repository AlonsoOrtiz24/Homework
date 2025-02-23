import requests
#Rome and Juliet by William Shakespeare
link1 = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"

result = requests.get(link1)
unique_words = {}
punctuation = ",.'!?-=()'"
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace(p, " ")
    words = line.split()
    for word in words:
        unique_words[word] = unique_words.get(word,0) + 1

print(len(unique_words))
#unique words = 5192