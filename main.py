database = {}

flag = True
db = {}
def deleteFunc(db):
    print("Введите элемент: ")
    key = input()
    db.pop(key)

def addFunc(db):
    print("Введите имя: ")
    name = input()
    print("Введите фамилию: ")
    lastName = input()
    print("Введите должность: ")
    status = input()
    print("Введите зарплату: ")
    salary = input()
    db[name+lastName] = {
    "name" : name,
    "lastname": lastName,
    "status" : status,
    "salary" : salary
    }
    print('DONE')

def changeFunc(db):
    key= input()
    db.pop(key)
    addFunc(db)

def show(db):
    for key in db.keys():
        print("key " + key)
        print("data ", db[key])


while flag:
    action = input()
    if action == "add":
        addFunc(database)
    elif action == "change":
        changeFunc(database)
    elif action == "delete":
        deleteFunc(database)
    elif action == "show":
        show(database)
    else:
        print("Неверная комманда!")
        flag = False
