# A closure allows a function to access variables from an outer function that has already returned.
def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(person + ' have only ' + str(coins) + ' coin left')
        elif coins == 1:
            print(person + ' have only ' + str(coins) + ' coin left')
        else:
            print(person + ' out of coin')
    return play_game


shadow = parent_function('R', 2)
light = parent_function('J', 5)

shadow()
shadow()
light()

shadow()
light()
light()
