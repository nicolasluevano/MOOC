# Write your solution here


def histogram(word: str):
    count = {}
    for i in word:
        if i not in count:
            count[i] = '*'
        elif i in count:
            count[i] += '*'
    print(count)

if __name__ == "__main__":
    histogram("statistically")
