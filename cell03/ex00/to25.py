#!/home/swichaid/Desktop/python3/.venv/bin/python3
a = int(input('Enter number less than:\n '))
def table():
        if a <= 25 :
            for i in range (a,26):
                print(f'inside the loop, my variable is {i}')
        else:
            print("Error")
table()
