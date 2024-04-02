#!/home/swichaid/Desktop/python3/.venv/bin/python
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a * b
    if result == 0:
        print('the result is negative and positive.')
    elif result < 0 :
        print('the result is negative.')
    else:
        print('the result is positive.')
except ValueError:
    print('please enter the number')
