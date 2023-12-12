# Write your solution here
def longest(strings: list):
    word_length = 0
    longest_word = ''
    for string in strings:
        if len(string) > word_length:
            word_length = len(string)
            longest_word = string
    return longest_word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))