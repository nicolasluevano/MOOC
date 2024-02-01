# Write your solution here
temp = int(input('Please type in a temperature (F):'))

cold_msg = "Brr! It's cold in here!"

to_cel = float((temp - 32) * 5/9)

print(f'{temp} degrees Fahrenheit equals {to_cel} degrees Celsius')
if to_cel < 0:
    print(cold_msg)