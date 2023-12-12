# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!



def palindromes(word):
    result = False
    while result == False:
        # word = input("Please type in a palindrome:")
        reversed = []
        for i in word:
            reversed.append(i)
        reversed.reverse()
        reversed = ''.join(reversed)
        if word == reversed:
            result = True
            ans = f"{word} is a palindrome!"
            return ans
        else:
            ans = "that wasn't a palindrome"
            return ans


palindromes()