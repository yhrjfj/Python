person = "Shadow"
coins = 5

# 1st way
print('\n' + str(person) + ' has ' + str(coins) + ' coin left')

# 2nd way
message = '\n%s has %s coin left \n' % (person, coins)
print(message)

# 3rd way
message = '{} has {} coin left \n'.format(person, coins)
print(message)

# 4th way "match index"
message = '{1} has {0} coin left \n'.format(coins, person)
print(message)

# 5th way
message = '{person} has {coins} coin left \n'.format(
    person=person, coins=coins)
print(message)

# ==============================================================================================================
# Using dictionary
player = {'person': 'Light', 'coins': 10}
dic_message = '{person} has {coins} coin left\n'.format(**player)
print(dic_message)

# ==============================================================================================================

# Main way
f_message = f'This is f-string\n{person} has {coins} coin left\n'
print(f_message)

f_message = f'This is f-string\n{person} has {coins+2} coin left\n'
print(f_message)

f_message = f'This is f-string\n{person.upper()} has {coins+2} coin left\n'
print(f_message)

# From dictionary "Line 25"
f_message = f'This is f-string\n{player["person"].upper()} has {player["coins"]} coin left\n'
print(f_message)

# ==============================================================================================================
# Formatting option
num = 7.77
# f mins fixes
print(f'Formatting option:\n2 times {num} equals to: {2*num:.3f}\n')
