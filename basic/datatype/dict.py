# dictionary are key pair , how we have maps in java

dic = {"username": "Punit123", "password": "pass1234"}
# different way to  get value by using key
print(dic["username"])
print(dic.get("password"))
print(dic.items())
print(dic.keys())
print(dic.values())
print(dic.setdefault("username"))

# adding  and updating values
dic["password"] = "1234pass"
dic["group"] = "Admin"
dic.update({"username": "Punit21"})
print(dic)

# remove
dic.popitem()
print(dic)

# nested Dictionary
edu = {"PG": {"college": "Jain University", "per": 78 },
        "UG": {"college": "Bangalore University", "per": 75},
        }
print(edu)
print(edu["PG"])

# --------------------------------- Ending Dictionary ----------------------------------------------