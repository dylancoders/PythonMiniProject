import json
import os


class Contact:

    def __init__(self, name=None, age=None, year_born=None, address=None):
        self.name = name
        self.age = age
        self.year_born = year_born
        self.address = address

    def get_user_info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.year_born = int(input("Enter your year born: "))
        self.address = input("Enter your address: ")

    def print_user_info(self):
        print(f"User Name is: {self.name}")
        print(f"User Age is: {self.age}")
        print(f"User Address is: {self.address}")
        print(f"User Year Born is: {self.year_born}")

    def __repr__(self):
        data = {
            "name": self.name,
            "age": self.age,
            "year_born": self.year_born,
            "address": self.address
        }
        return data


class Contact_By_Email(Contact):
    def __init__(self, name=None, age=None, year_born=None, address=None, email=None, email_domain=None, email_title=None, email_content=None):
        super().__init__(name=name, age=age, year_born=year_born, address=address)
        self.email = email
        self.email_domain = email_domain
        self.email_titles = email_title
        self.email_content = email_content

    def get_user_info(self):
        super().get_user_info()
        self.email = input("Enter your email: ")
        while "@" not in self.email or "." not in self.email:
            print("Please enter a valid email address!")
            self.email = input("Enter your email: ")
        domain_still = self.email.split("@")[1]
        self.email_domain = domain_still.split(".")[0]
        self.email_title = input("Enter your email title: ")
        self.email_content = input(
            "Enter email content (less more 256 words): ")
        while len(self.email_content) > 256:
            print("Error! You have to enter more less 256 words!")
            self.email_content = input(
                "Enter email content (less more 256 words): ")

    def write_user_info_to_txt(self):
        with open("email.txt", 'w') as f:
            f.write(self.name + "\n")
            f.write(self.email + "\n")
            f.write(self.email_title + "\n")
            f.write(self.email_content + "\n")
        print("Success!")

    def print_user_info(self):
        super().print_user_info()
        print(f"User Email is: {self.email}")

    def __repr__(self):
        data = super().__repr__()
        data['email'] = self.email
        return str(data)


class Contact_By_Phone(Contact):
    def __init__(self, name=None, age=None, year_born=None, address=None, phone_number=None, phone_carrier=None, country=None, sms_title=None, sms_content=None):
        super().__init__(name=name, age=age, year_born=year_born, address=address)
        self.phone_number = phone_number
        self.phone_carrier = phone_carrier
        self.country = country
        self.sms_title = sms_title
        self.sms_content = sms_content

    def check_number(self):
        for c in self.phone_number:
            if c.isalpha():
                return False
                break
        return True

    def get_user_info(self):
        super().get_user_info()
        self.phone_number = str(input("Enter your phone number: "))
        while len(str(self.phone_number)) > 10 or len(str(self.phone_number)) < 10 or not self.check_number():
            is_char = not self.check_number()
            is_full_number = len(str(self.phone_number)) > 10 or len(
                str(self.phone_number)) < 10
            if is_char:
                print("Has characters in your phone number")
            if is_full_number:
                print(
                    f"Your phone number has {len(str(self.phone_number))} characters")
                print("Your number phone must be less more than 11 and more than 9")
            self.phone_number = str(input("Enter your phone number: "))
        self.sms_title = input("Please enter your SMS title: ".upper())
        self.sms_content = input("Enter email content (less more 256 words): ")
        while len(self.sms_content) > 256:
            print("Error! You have to enter more less 256 words!")
            self.sms_content = input(
                "Enter email content (less more 256 words): ")

    def write_user_info_to_txt(self):
        with open("sms.txt", 'w') as f:
            f.write(self.name + "\n")
            f.write(str(self.phone_number) + "\n")
            f.write(self.sms_title + "\n")
            f.write(self.sms_content + "\n")
        print("Success!")

    def print_user_info(self):
        super().print_user_info()
        print(f"User Number Phone is: {self.phone_number}")

    def __repr__(self):
        data = super().__repr__()
        data['phone_number'] = self.phone_number
        return str(data)


class DataManager:
    def __init__(self, data_manager=[]):
        self.data_manager = data_manager

    def write_data(self):
        data = []
        for user in self.data_manager:
            new_user = {
                "name": user.name,
                "age": user.age,
                "year_born": user.year_born,
                "address": user.address
            }
            try:
                new_user["email"] = user.email
                new_user["email_title"] = user.email_title
                new_user["email_content"] = user.email_content
            except AttributeError:
                new_user["phone_number"] = user.phone_number
                new_user["sms_title"] = user.sms_title
                new_user["sms_content"] = user.sms_content
            data.append(new_user)
        with open("data.json", "w") as f:
            json.dump(data, f)

    def read_data(self):
        if 'data.json' in os.listdir():
            new_data = []
            with open('data.json', 'r') as f:
                data = json.load(f)
            for user in data:
                if "email" in user:
                    new_user = Contact_By_Email()
                    new_user.name = user["name"]
                    new_user.age = user["age"]
                    new_user.year_born = user["year_born"]
                    new_user.address = user["address"]
                    new_user.email = user["email"]
                    new_user.email_title = user["email_title"]
                    new_user.email_content = user["email_content"]
                else:
                    new_user = Contact_By_Phone()
                    new_user.name = user["name"]
                    new_user.age = user["age"]
                    new_user.year_born = user["year_born"]
                    new_user.address = user["address"]
                    new_user.phone_number = user["phone_number"]
                    new_user.sms_title = user["sms_title"]
                    new_user.sms_content = user["sms_content"]
                new_data.append(new_user)
            self.data_manager = new_data
        else:
            self.data_manager = []

    def add_user(self):
        while True:
            user_choose = input("You need to choose email or sms ?: ")
            if user_choose.lower() == "email":
                user = Contact_By_Email()
                user.get_user_info()
                break
            elif user_choose.lower() == "sms":
                user = Contact_By_Phone()
                user.get_user_info()
                break
            else:
                print("Please enter email or sms!")
        self.data_manager.append(user)
        # print(user.name)

    def display_user(self):
        if len(self.data_manager) == 0:
            print("Not found any user in list".upper())
        else:
            for i in range(len(self.data_manager)):
                print(f"ID: {i+1}")
                print(f"Name: {self.data_manager[i].name}")
                print(f"Age: {self.data_manager[i].age}")
                print(f"Year Born: {self.data_manager[i].year_born}")
                print(f"Address: {self.data_manager[i].address}")
                try:
                    print(f"Email:{self.data_manager[i].email}")
                except AttributeError:
                    print(f"PhoneNumber: {self.data_manager[i].phone_number}")
                print("----------\n")

    def remove_user(self):
        self.display_user()
        if len(self.data_manager) == 0:
            pass
        else:
            while True:
                user_option = int(input("Enter ID you want to remove: "))
                try:
                    self.data_manager.pop(user_option - 1)
                    break
                except IndexError:
                    print("Please enter correct ID!")
            print("Remove user successfully")

    def edit_user(self):
        self.display_user()
        if len(self.data_manager) == 0:
            pass
        else:
            while True:
                user_option = int(input("Enter ID you want to edit: "))
                try:
                    self.data_manager[user_option - 1].get_user_info()
                    break
                except IndexError:
                    print("Please enter correct ID!")
            print(f"ID edited successfully: {user_option}")

    def write_user_to_text(self):
        self.display_user()
        if len(self.data_manager) == 0:
            pass
        else:
            while True:
                user_option = int(
                    input("Enter ID you want to write to text: "))
                try:
                    self.data_manager[user_option - 1].write_user_info_to_txt()
                    break
                except IndexError:
                    print("Please enter correct ID!")
            print(f"ID information written successfully: {user_option}")

    def exit(self):
        while True:
            print("""
            0. Exit with save change
            1. Exit without save change
            """)
            exit_option = int(input("Enter ID you want to exit: "))
            if exit_option == 0:
                self.write_data()
                print("Exit successfully with save change!")
                exit()
            elif exit_option == 1:
                print("Exit successfully without save change!")
                exit()
            else:
                print("Please enter a number in above list!".upper())

    def run(self):
        self.read_data()
        while True:
            print("""
            0. Exit
            1. Show user
            2. Add user
            3. Edit user
            4. Remove user
            5. Write user's information to file
            6. Save data
            """)
            user_number = int(input("Enter your option to choose features: "))
            if user_number == 0:
                self.exit()
            elif user_number == 1:
                self.display_user()
            elif user_number == 2:
                self.add_user()
            elif user_number == 3:
                self.edit_user()
            elif user_number == 4:
                self.remove_user()
            elif user_number == 5:
                self.write_user_to_text()
            elif user_number == 6:
                self.write_data()
            else:
                print("Please enter a number in above list!".upper())


if __name__ == "__main__":
    app = DataManager()
    app.run()
