# data type in python ( Numeric, List, String, tuple, Dictionary, Boolean, Set )
# --------------------------------------------------------------------------------
# 1. Numeric ( int, float, complex )
i = 3               # int
f = 4.556           # float
c = 1j              # complex

# printing variable data type  and value
print(type(i), i)
print(type(f), f)
print(type(c), c)

# -------------------------------------------------------------------------------------
# String
stng = " lets play with string "     # string variable
# multiline string
mstng = """multiline string, let's   
        play around it"""

# printing the string
print(stng)
print(mstng)

# slicing of string
print(stng[0:9])

# strip, right strip, left strip
print(stng.strip())
print(stng.rstrip())
print(stng.lstrip())

# upper case, lower case , first character caps
print(stng.upper())
print(stng.lower())
print(stng.title())

# split of string
print(stng.split(" "))

# replace
print(stng.replace("w", "W"))

# format
txt = "My name is {}"
name = "Punit Chaudhary"
print(txt.format(name))

# string length
l = len(stng)
print(len(stng))

# reverse of String
print(stng[::-1])

# with logic
rev = ""
for ii in range(l-1, 0, -1):
    rev = rev + stng[ii]
print("Reverse : ", rev)

# convert string into list
stng = stng.strip()
lst = stng.split(" ")
print(lst)

# count the character frequency in string
print(stng.count("s"))

# with logic
count = 1
stng = stng.strip()
stng = stng.replace(" ", "")
stng = sorted(stng)
l1= len(stng)
print(stng)
for x in range(1, l1):
    b = stng[x-1] == stng[x]
    if b == True:
        count = count+1
    else:
        print(stng[x-1], count)
        count = 1
print(stng[x-1], count)

#---------------------------Ending with String ----------------------------------------