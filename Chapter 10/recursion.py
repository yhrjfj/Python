def add_one(num):
    if num >= 9:
        return num+1
    total = num + 1
    print(total)
    return add_one(total)


my_new_value = add_one(0)
print(my_new_value)
# # ====================================================================

# def loop():
#     for i in range(1, 11):
#         print(i)
#     return "Loop completed"


# loop()
# #=====================================================================
