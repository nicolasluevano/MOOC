# Write your solution here
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature:"))
rain = input("Will it rain(yes/no):")

a = "Wear jeans and a T-shirt"
b = "I recommend a jumper as well"
c = "Take a jacket with you"
d = "Make it a warm coat, actually"
e = "I think gloves are in order"
f = "Don't forget your umbrella!"

if temp > 20:
    print(a)

if 10 <= temp <=20:
    print(a)
    print(b)

if 5 <= temp <= 10:
    print(a)
    print(b)
    print(c)

if temp <= 5:
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

if rain == 'yes':
    print(f)