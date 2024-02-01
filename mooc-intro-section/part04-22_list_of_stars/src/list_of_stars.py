# Write your solution here
def list_of_stars(ls):
    for i in ls:
        print("*" * i)

if __name__ == "__main__":
    ls = [3,5,7,9]
    list_of_stars(ls)