with open("file1.txt") as file1:
    file_1 = (file1.readlines())
    file_1 = [int(num.rstrip('\n')) for num in file_1]
with open("file2.txt") as file2:
    file_2 = (file2.readlines())
    file_2 = [int(num.rstrip('\n')) for num in file_2]

print(file_1)
print(file_2)

combined_numbers = [num for num in file_1 if num in file_2]
print(combined_numbers)
