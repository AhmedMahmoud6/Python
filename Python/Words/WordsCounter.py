#first of all we need to make the user open a file
user = input('please enter file name: ')
try:
    file = open(user)
except:
    print('file name is incorrect or not found, please try again!')
    quit()
#we now need an empty dictionary to put all the words in that mysterious file to that dict
dict = dict()
#we're making an iteration variable that iterates through the file and
#splitting all the file words then looping through the splitted words and
#check if these words are in the dict or not and if it's in add one to it's current count
#if it's not in the dict set it's value to 0 and add 1 to it
for iteration in file:
    split = iteration.split()
    for test in split:
        dict[test] = dict.get(test,0) + 1
#after finding and counting all the words, now we need to know what's the biggest word and
#how many times did it repeat in the file
bigword = 0
bigcount = 0
#making a 2 iteration variable in the for loop, one for the dict keys and one for the value
#we using the .items func to make the dict a list of tuples to get the key and value
#then we check if the value is None or the value is greater than the current bigcount (value)
#and setting the current word and current value to bigword and bigcount if the condition is true
for key,value in dict.items():
    if value is None or value > bigcount:
        bigword = key
        bigcount = value

print('the word',bigword,'repeated',bigcount,'times in the file')
