#!//usr/bin/python3
# msg = int(input('Please tell me your age: '))
# print(f'You are currently {msg}')
# print(f"In 10 years,you'll be {msg+10} years old")
# print(f"In 20 years,you'll be {msg+20} years old")
# print(f"In 30 years,you'll be {msg+30} years old")

try:
    msg = int(input("Please tell me youe age: "))

    for i in range (10,31,10):
        print(f"In {i} year, you'll be {msg+i} years old")
except: print("please enter the number")
