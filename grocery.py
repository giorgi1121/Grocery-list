#make empty dictionary
dict = {}

#try-except for catching errors
try:
    #create loop for asking user items and add them to dict
    while True:
        item = input().upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
except EOFError:
    pass

#create sorted list of dict
lst = sorted(dict)

#print items from dict according to alphabetic system using sorted list
for x in lst:
    print(dict[x], x)
