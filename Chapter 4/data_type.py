import math

# String Data Type

# Literal assignment
first = 'Shadow'
last = 'Light'
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor assignment
# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# fullname = first + " " + last
# print(fullname)
# print('')
# fullname += '!'
# print(fullname)

# Casting a number to a string
# print('')
# decade = str(2000)
# print(type(decade))
# print(decade)
# statement = "I born in " + decade + "."
# print(statement)
# print('')

# Multiple Line
multiple_line = '''
Hey there!
        I am shadow
                                                AND
                Shadow need's "Light" for showing himself.
'''
# print(multiple_line)
# print('')

# Escaping special character
# sentence = 'Hey!\nI\'m Back'
# print(sentence)
# print('')

# #String methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)
# print('')

# print('Make each word\'s first letter as a capital letter')
# print(multiple_line.title())
# print('Replace Hey to Hi')
# print(multiple_line.replace('Hey', 'Hi'))
# print('Print original line')
# print(multiple_line)

# print('Length: ' + str(len(multiple_line)))
# multiple_line += '                                                            '
# multiple_line = '                                                         ' + multiple_line
# print('Length: ' + str(len(multiple_line)))
# print('')
# # Removing white space
# print('Length: ' + str(len(multiple_line.strip())))
# print('Length: ' + str(len(multiple_line.lstrip())))
# print('Length: ' + str(len(multiple_line.rstrip())))


# # Build a  menu
# title = "menu".upper()
# print(title.center(20, '='))
# print("coffee".title().ljust(16, '.') + "$1".rjust(4))
# print("Muffin".title().ljust(16, '.') + "$2".rjust(4))
# print("Cheesecake".title().ljust(16, '.') + "$4".rjust(4))

# print('')

# # String index value
# print(first[1])  # Index value
# print(first[-1])  # Last value
# print(first[0:])  # Check value from first to last

# # Some methods return boolean value
# print('First letter start with "S": ' + str(first.startswith('S')))
# print('Last letter end\'s with "O": ' + str(first.endswith('O')))

# # Boolean data type
# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# # Numerical data type
# # Integer data type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))
# print('')

# # FLoat data type
gpa = 4.56
# y = float(3.2)
# print(type(gpa))
# print(isinstance(y, float))
# print('')

# # Complex data type
# complex_value = 5+3j
# print(type(complex_value))
# print(complex_value.real)
# print(complex_value.imag)

# Build in function for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print('\n')

print(math.pi)
print(int(math.sqrt(64)))
print(math.ceil(gpa))
print(math.floor(gpa))
