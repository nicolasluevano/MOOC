# write your solution here
sentence = input("Write text:")


words = sentence.split()

all_words = []

result = ''

with open("src/wordlist.txt") as new_file:
    for word in new_file:
        word = word.replace("\n", "")
        all_words.append(word)

for word in words:
    if word.lower() in all_words:
        result += f'{word} '
    else:
        result += f'*{word}* '

print(result)
