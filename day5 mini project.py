# names = ["nandhu", "shiva", "gorre", "madhu"]
# for name in names:
#     print(name)
#     print(name + "reddy")

# student_scores = input().split()
# for n in range (0, len(student_scores)):
#      student_scores[n] = int(student_scores[n])
# highest_score = 0
# for score in student_scores:
#      if score > highest_score:
#          highest_score = score
# print(f"the highest score in the class is: {highest_score}")

# for i in range(1,11):
#     print(i)


# total = 0
# for number in range(1,101):
#     total  += number
# print(total)

# target = int(input())
# even = 0
# for num in range(2, target+1, 2):
#     even += num
# print(even)

import random
letters = ['a' 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
symbols = ['!', '#', '$' '%', '&', '(', ')', '*', '+']
print("welcome to password generator/n")
num_letters = int(input("how many letters you want\n"))
num_numbers = int(input("how many numbers you like add?\n"))
num_symbols = int(input("how many symbols you want to add?\n"))
password = ''
for i in range(1,num_letters+1):
    password += random.choice(letters)
for i in range(1,num_numbers+1):
    password += random.choice(numbers)
for i in range(1, num_symbols+1):
    password += random.choice(symbols)
print(password)












