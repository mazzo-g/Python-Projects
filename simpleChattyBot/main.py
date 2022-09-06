bot_name = "Lavender"
birth_year = "2022"

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

print("Please remind me your name.")
your_name = input()
print(f"What a great name you have, {your_name}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 abd 7.")
remainder3 = float(input("> "))
remainder5 = float(input("> "))
remainder7 = float(input("> "))
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"You age is {your_age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
number = int(input())
for step in range(number + 1):
    print(f"{step} !")

print("Let's test your programming knowledge.")

answer = input("Why do we use methods?\n"
               "1. To repeat a statement multiple times.\n"
               "2. To decompose a program into several small subroutines.\n"
               "3. To determine the execution time of a program.\n"
               "4. To interrupt the execution of a program.")

while answer != "2":
    print("Please, try again.")
    answer = input()

print("Congratulations, have a nice day!")
