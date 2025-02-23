import requests
#Moby Dick by Herman Melville
link1 = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"

result = requests.get(link1)
unique_words_1 = {}
punctuation = ",.'!?-=()'"
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace(p, " ")
    words = line.split()
    for word in words:
        unique_words[word] = unique_words.get(word,0) + 1

print(len(unique_words))
#Unique Words Moby Dick = 23610
#Unique words Romeo and Juliet = 5192