#!/home/swichaid/Desktop/python3/.venv/bin/python3
def main():
    try:
        x = int(input("Give me the first number: "))
        y = int(input("Give me the second number: "))

        print(f"{x} + {y} = {x+y}")
        print(f"{x} - {y} = {x-y}")
        print(f"{x} / {y} = {x//y}")
        print(f"{x} * {y} = {x*y}")
    except: print("Please enter the integer number")

main()

