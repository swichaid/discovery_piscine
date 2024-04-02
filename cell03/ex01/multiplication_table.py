#!/home/swichaid/Desktop/python3/.venv/bin/python
num = int(input('Enter number:\n'))
def table():
    for i in range (0,10):
        result = num*i
        print(f'{i} x {num} = {result}')
table()
