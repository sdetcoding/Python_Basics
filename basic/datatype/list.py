# List and Tuple
ls = [1, 2, 8, 5, 7, 7, 0, 8, 9, 5, 6, 5, 5, 0]
# printing list
print(ls)

# remove
ls.remove(2)
del ls[-1]

# append in list
ls.append(3)
ls[4] = 21

# removing  duplicate from list
ls = list(dict.fromkeys(ls))
print("remove dup", ls)

# count the frequency of word
print(ls)
print(ls.count(5))
print(ls.index(5))

# sorting of list
ls.sort()
print(ls)

# reverse of list
ls.reverse()
print(ls)

# list copy
lsa = ["Punit", "Chaudhary"]
ls1 = lsa.copy()
print(ls1)
lsa.extend(ls)
print(lsa)

# tuple we are not allowed to append tuple
tuple1 = (1, 2, 4)
print(tuple1)
# handling with exception so we should stop program to terminate abnormally
try:
    tuple1[2] = 9
except Exception as e:
    print("we are not allowed to append tuple ", e)
finally:
    print("covered exception")

# ------------------------Ending List and tuple -------------------------------------------
