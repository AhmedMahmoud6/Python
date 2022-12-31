lst = list()
def splitter():

    user = input('Enter your word to change: ')
    for i in user:
        lst.append(i)
    print('there is', len(lst), 'chars in this word' )
    repeater()
    return ''.join(lst)


def repeater():
        user_inp = input('how many characters you wanna replace: ')
        user_int = int(user_inp)
        for i in range(user_int) :
            if i < len(lst):

                user_index = input('Enter the index of the character you wanna change')

                user_indexed = int(user_index)

                user_change = input('Enter the new character: ')
                try:

                    lst[user_indexed] = user_change
                    i = i + 1
                except:
                    print('invalid index, please try again')
                    quit()



t = splitter()
print(t)
