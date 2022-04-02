# Dictionary Method
Dic = {'name': "Muhaimin " "\n" "Hasnain " "\n" "Hamza", 'skill': "Coding " "Creative Writing " "Exploring"}

# Method Get: Returns the value of the specified key
print(Dic.get("name"))

# Method Values: Returns a list of all the values in the dictionary
print("====================")
print(Dic.values(), "\n")

# Method Pop: Removes the element with the specified key
print("====================")
print("Previous====================", "\n", Dic, "\n")
# print(Dic.pop("skill"))
print("After====================", "\n", Dic, "\n")

# Method copy: Returns a copy of the dictionary
print("Copy====================")
print(Dic.copy(), "\n")

# Method keys: Returns a list containing the dictionary's keys
print("keys====================")
print(Dic.keys(), "\n")

# Method clear: Removes all the elements from the dictionary
print("clear====================")
# Dic.clear()
print(Dic, "\n")

# Method fromkeys: Returns a dictionary with the specified keys and value
print("fromkeys====================")
print(Dic.fromkeys("name"), "\n")

# Method items: Returns a list containing a tuple for each key value pair
print("items====================")
Dic.items()
print(Dic, "\n")

# Method  popitem: Removes the last inserted key-value pair
print("popitem====================")
Dic.popitem()
print(Dic, "\n")

# Method update() : Updates the dictionary with the specified key-value pairs
print("update====================")
Dic.update({"Ranking": "1"})
print(Dic, "\n")

# Method setdefault: Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print("setdefault====================")
print(Dic.setdefault("name"), "\n")






