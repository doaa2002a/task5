#question 1
name = input("Please enter your name: ")
age = input("Please enter your age: ")
street = input("Please enter your street: ")
city = input("Please enter your city: ")
country = input("Please enter your country: ")


#question 2
print(f'"Name: {name}"')
print(f'"Age: {age}"')
print(f'"Address: {street}, {city}, {country}"')
print(f'"name : {name}"')

#question 3
adjusted_age = int(age) - 5
message = f'Hello {name} Your age is {adjusted_age} Years old, your Address is {street},{city},{country}'
print(message)


#question 4
types = type(name), type(age), type(street), type(city), type(country)
print(types)

#question 5
print(f"\"Hello {name}, How Are You? \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")

#question 6
print(f"""\"Hello {name}, How Are You? \\
\"\"\" Your Age Is \"{age}\"\"\" + And
Your Country Is: {country}""")

#question 7
NAME2 = 'ITF Gsg Python'
first_letter = NAME2[0]
third_letter = NAME2[2]
last_letter = NAME2[-1]
print(f'First Letter Is "{first_letter}"')
print(f'Third Letter Is "{third_letter}"')
print(f'Last Letter Is "{last_letter}"')

#question 8
print(NAME2[11:14:1])
print(NAME2[0:3])
print(NAME2[0:7:2])
print(NAME2[-1:-8:-1])

#question 9
NAME3 = "$&$&Mohammed$&$&"
print(NAME3.strip("$&$&"))

#question 10
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7", "Love"))

##question 11 12
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"

print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
# question 13
# title() capitalizes the first character of each word in the string.
# capitalize() capitalizes only the first character of the entire string
#EX.1
text = "Doaa is a pharmacist student"
print(text.title())
#output "Doaa Is A Pharmacist Student"
#EX.2
print(text.capitalize())
#output "Doaa is a pharmacist student"

#question 14
first_name = "Dana"
print("***********" + first_name)
print("***********" + first_name + "***********")
print(first_name + "***********")

#question 15
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())

#question 16
if name_one.isupper():
    print("name_one contains only uppercase letters")
else:
    print("name_one does not contain only uppercase letters")
if name_two.islower():
    print("name_two contains only lowercase letters")
else:
    print("name_two does not contain only lowercase letters")
#OR
print(name_one.isupper())
print(name_two.islower())

# question 17 (bonus)
print(name_one.startswith('s'))
print(name_two.endswith('HD'))

# question 18
Msg = "I Love Python And Although I Love GSG with Zakaria"
print("Number of <Love> is:",Msg.count('Love'))
print("Number of <Love> is:",Msg.count('t'))

# question 19
mSg = "I %7 Python And Although I %7 GSG with Zakaria"
print(mSg.replace("%7", "Love", 1))

# question 20
def is_symmetrical_and_palindrome(s):
    s = s.replace(" ", "").replace(".", "").replace(",", "").lower()
    is_symmetrical = s == s[::-1]
    is_palindrome = s == s[::-1]
    return is_symmetrical, is_palindrome


test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa."
test4 = "madam"

result1 = is_symmetrical_and_palindrome(test1)
result2 = is_symmetrical_and_palindrome(test2)
result3 = is_symmetrical_and_palindrome(test3)
result4 = is_symmetrical_and_palindrome(test4)


def print_result(test, result):
    if result[0]:
        symmetrical_message = f"{test} is symmetrical,"
    else:
        symmetrical_message = f"{test} is NOT symmetrical,"

    if result[1]:
        palindrome_message = f"but {test} is a palindrome."
    else:
        palindrome_message = f"but {test} is NOT a palindrome."

    print(f"{symmetrical_message} {palindrome_message}")


print_result(test1, result1)
print("################################")
print_result(test2, result2)
print("################################")
print_result(test3, result3)
print("################################")
print_result(test4, result4)