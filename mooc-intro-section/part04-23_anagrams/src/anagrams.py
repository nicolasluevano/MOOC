# Write your solution here
def anagrams(str1,str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False

if __name__ == "__main__":
    str1 = "tame"
    str2 = "meta"
    print(anagrams(str1, str2))