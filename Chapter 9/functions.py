def hello_world():
    print('Hello World!')


hello_world()
# ======================================================================


def sum(num1=0, num2=0):
    if (type(num1) is not int) and (type(num2) is not int):
        return 'Something Wrong....!'
    return num1 + num2


total = sum(4, 10)
print(total)
# ========================================================================

# # For single argument
# def multiple_items(args):  # Without *
#     print(args)
#     print(type(args))


# multiple_items('Shadow')

# For multiple argument
def multiple_items(*args):  # With *
    print(args)
    print(type(args))


multiple_items('Shadow', 'Light', 'YHR', 'JFJ')
# ========================================================================


def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_named_items(first='Yousuf', last="Hasan", final='Riyad')
