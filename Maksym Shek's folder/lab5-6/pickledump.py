import pickle

FILENAME = "C:\\Users\\Super\\Desktop\\MAKSYM SHEK\\Maksym Shek's folder\\lab5-6\\user.dat"

users = (
    ("Tom", 28, True),
    ("Alice", 23, False),
    ("Bob", 34, False)
)

with open(FILENAME, "wb") as file:
    pickle.dump(users, file)

with open (FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print ("Name", user[0],"\tAge", user[1], "\tMarried", user[2])