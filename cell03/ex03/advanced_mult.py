#!/home/swichaid/Desktop/python3/.venv/bin/python3
import sys

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'YOLO':
            print('none')
        elif sys.argv[1] != 'YOLO':
            print('Wrong arrgument')
        exit()

    elif len(sys.argv) == 1:
        mult_table()

def mult_table():
    for i in range (11):
        if i < 10:
            print(f"Table de {i}:", *[i*j for j in range (11)])

main()
