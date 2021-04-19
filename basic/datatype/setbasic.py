# --------- Lets Play with Set -------------------------------------
st = {1, 2, 3}
print(st)

# empty set
est = {}
print(est)

# adding value to set
st.add(4)
st.add(40)
st.add(64)
st.add(42)
print(st)

# removing value from set
st.pop()
st.remove(42)
st.discard(42)  # will not throw error if element is not present
print(st)

# creating set by se constructor
b = set([2, 3, 4, 88, 44, 22, 77])

# length of set
print(len(b))

# finding all the method associate with set
print(dir(b))

# union of set
print(st | b)
print(st.union(b))

# difference
print(st - b)
print(st.difference(b))

# frozen the value of set
s = frozenset(b)
print(s)
# trying to add value to frozenset
try:
    s.add(99)
except Exception as e:
    print(e)
finally:
    print("you cant add value to frozen set")

# ------------------------------- Ending up the set --------------------------------
