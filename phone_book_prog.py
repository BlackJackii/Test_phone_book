import json
import uuid
import os
import time


def start():
    while True:
        ans = input("""
  *********************
  * Choose menu item: *
  *********************
  | 1) Add new record.
  | 3) Search by last 
  | 4) Search by fullname 
  | 5) Search by number 
  | 6) Search by city 
  | 7) Delete phone 
  | 8) Update exist one
  | 9) Exit - press 'Q'
  |         Choose num: """).upper()
        
        menu_button = {"2": "name", "3": "lastname", "4": "full_name", "5": "phone", "6": "city"}
        if ans == "1":
            add_new()
            time.sleep(3)
        if ans in menu_button:
            name = input(f"Enter a {menu_button[ans]} u looking for: ").lower().title()
            print(search_by(name, key=menu_button[ans]))
            time.sleep(3)
        if ans == "7":
            del_phone()
        if ans == "8":
            update()
        if ans == "Q":
            print("Ty for using my prog")
            break


def add_new():
    new_dict = {}
    name = input("Enter a name u wanna add: ").lower().title()
    lastname = input("Enter a lastname: ").lower().title()
    city = input("Enter a city: ").lower().title()
    phone = input("Enter a phone: ")
    full_name = f"{name} {lastname}"
    ppl_id = str(uuid.uuid4())[:-6:-1]
    new_dict[ppl_id] = {
        "name": name,
        "lastname": lastname,
        "full_name": full_name,
        "city": city,
        "phone": phone
    }
    if os.path.exists("phone_book.json"):
        file = read_json()
        file.update(new_dict)
        write_json(file)
    else:
        write_json(new_dict)
    print("Your data added.")


def read_json():
    with open("phone_book.json", "r", encoding="utf8") as file:
        return json.load(file)


def write_json(what_to_write):
    with open("phone_book.json", "w", encoding="utf8") as file:
        json.dump(what_to_write, file, ensure_ascii=False, indent=4)
        return


def search_by(name, key="name"):
    phone_list = read_json()
    for i, k in phone_list.items():
        if k[key] == name:
            return (f'iD:{i}\nName:{k["name"]}\nLastname:{k["lastname"]}\nCity:{k["city"]}\nPhone:{k["phone"]}')


def update():
    user_update = input("Enter a name: ").lower().title()
    print(search_by(user_update, key="name"))
    what_to_change = input("Enter what to change: ")
    new_value = input("Value: ")
    p_id = search_id(read_json(), user_update)
    some_file = read_json()
    for i, key in some_file.items():
        if i == p_id:
            key[what_to_change] = new_value
            print(p_id)
            write_json(some_file)


def search_id(data, name="name"):
    if "name" in data:
        return data["name"] == name

    for k in data:
        if search_id(data[k], name):
            return k


def del_phone():
    user_delete = input("Enter a name u want to delete: ").lower().title()
    print(search_by(user_delete, key="name"))
    p_id = search_id(read_json(), user_delete)
    file = read_json()
    for i in file:
        if i == p_id:
            file.pop(p_id)
            write_json(file)
            print("*** Successfully ***")
            time.sleep(3)
            return


if __name__ == '__main__':
    start()
