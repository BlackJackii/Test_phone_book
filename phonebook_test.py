from unittest import TestCase, main
from unittest.mock import patch
import phone_book_prog
import os
import json


class PhoneBookTest(TestCase):
    def test_addnew(self):
        with patch("builtins.input", side_effect=["name", "lastname", "city", "phone"]) as tp:
            phone_book_prog.add_new()

        with open("phone_book.json", "r") as file:
            new_dict = json.load(file)
            for index, key in new_dict.items():
                if key["name"] == "Name":
                    print("***** string 'Name' is ok")
                if key["lastname"] == "Lastname":
                    print("***** string 'Lastname' is ok")
                if key["city"] == "City":
                    print("***** string 'City' is ok")
                if key["phone"] == "Phone":
                    print("***** string 'Phone' is ok")
        file.close()
        print("***** Add_NEW func is ok")

    def test_is_exist(self):
        assert os.path.exists("phone_book.json")
        print("**** phone_book.json is exist")

    def test_dell(self):
        try:
            with patch("builtins.input", side_effect=["Name"]) as td:
                phone_book_prog.del_phone()
                with open("phone_book.json", "r") as file:
                    file = json.load(file)
                    if len(file) < 3:
                        print("*****Dell func is ok")
        except FileNotFoundError:
            print("Cant find file")


if __name__ == '__main__':
    main()
