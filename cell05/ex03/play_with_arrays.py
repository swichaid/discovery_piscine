#!/usr/bin/python3
Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(Original_array)
New_array = [num + 2 for num in Original_array]
New_array_filtered = [num for num in New_array if num >= 5]
set_array = set(New_array_filtered)
print(set_array)
