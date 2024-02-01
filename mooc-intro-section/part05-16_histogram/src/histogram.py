# Write your solution here
def histogram(word: str):
    count = {}
    for i in word:
        if i not in count:
            count[i] = '*'
        elif i in count:
            count[i] += '*'
    for key, value in count.items():
        print(key, value)

if __name__ == "__main__":
    histogram("abba")
