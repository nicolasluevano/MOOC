# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    #return new version of string
    #does not contain any chars from second string
    #use list comprehensions
    #max lengh of function == 3 lines
    new_list = "".join([letter for letter in string if letter not in forbidden])
    return new_list

if __name__ == "__main_)":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)