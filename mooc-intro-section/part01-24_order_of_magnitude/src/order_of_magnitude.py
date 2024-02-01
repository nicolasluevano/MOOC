# Write your solution here
nummy = int(input("Please type in a number:"))
thou = "This number is smaller than 1000"
hunnid = "This number is smaller than 100"
tenny = "This number is smaller than 10"
thanks = "Thank you!"

if nummy < 10:
    print(thou)
    print(hunnid)
    print(tenny)
    print(thanks)

if 10 < nummy < 100:
    print(thou)
    print(hunnid)
    print(thanks)

if 100 < nummy < 1000:
    print(thou)
    print(thanks)

if nummy > 1000:
    print(thanks)
    
