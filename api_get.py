from requests import get

text = """
1. UZ -> EN 
2. EN -> UZ
3. STOP
choice : 
"""

while True:
    choice = int(input(text))
    if choice == 1:
        name = input("text enter in uz -> : ")
        uz = f"https://langapi-sjvl.onrender.com/uz_en/{name}"
        resp = get(uz)
        print(resp.json()["EN"])
    elif choice == 2:
        name = input("text enter in en -> : ")
        en = f"https://langapi-sjvl.onrender.com/en_uz/{name}"
        resp = get(en)
        print(resp.json()["UZ"])

    else:
        print("Thank you")
        break
