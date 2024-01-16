class info:
    def __init__(self,phone,email,address):
        self.phone = phone
        self.email = email
        self.address = address
        
    def add_contact(self):
        self.name_list.append[self.name]
        
    def update_phone(self,new_number):
        print(f"Phone number change from {self.phone} to {new_number}")
        self.phone = new_number

    def update_address(self,new_address):
        print(f"address change from {self.address} to {new_address}")
        self.address = new_address
        
    def update_(self,new_email):
        print("email changed from {self.email} to {new_email}")
        self.email = new_email
        
    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address        
        
print("Welcome to contact book made by Jawad ALi")
contact_dict = {}
file = open("contact.txt","a")

while True:
    print("1. Add contact")
    print("2. View contact list")
    print("3. Search contact")
    print("4. update contact")
    print("5. delete contact")
    print("6. exit")
    
    user_input = input("Enter your choice from 1 to 5: ")
    
    if user_input == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        
        contact_dict[name] = info(phone, email, address)
        print("\nContact added successfully \n")
        
    elif user_input == "2":
        print()
        if len(contact_dict) >= 1:
            for name in contact_dict:
                phone =contact_dict[name].get_phone()
                email = contact_dict[name].get_email()
                address = contact_dict[name].get_address()
                print(f"name: {name} phone: {phone} email: {email}")
                
        else:
            print("\nEmpty contact book\n")
            
        print()
                
    elif user_input == "3":
        print("1. name")
        print("2. phone number")
        search_by = input("Choose 1 or 2: ")
                          
        if search_by == "1":
            search_name = input("Enter name to search: ")
            if search_name in contact_dict:
                phone =contact_dict[search_name].get_phone()
                email = contact_dict[search_name].get_email()
                address = contact_dict[search_name].get_address()
                print(f"name: {search_name} phone: {phone} email: {email} address {address}")

            
            else:
                print("name no found")
                
            print()
                
        else:
            search_number = input("Enter number to search contact: ")
            for name in contact_dict:
                if search_number == contact_dict[name].get_phone():
                    phone =contact_dict[name].get_phone()
                    email = contact_dict[name].get_email()
                    address = contact_dict[name].get_address()
                    print(f"name: {name} phone: {phone} email: {email} address {address}")
                    
    elif user_input == "4":
        name = input("Enter name: ")
        new_phone = input("Enter phone number: ")
        new_email = input("Enter email: ")
        new_address = input("Enter address: ")
        
        if new_phone == "":
            new_phone = contact_dict[name].get_phone()
        elif new_email == "":
            new_email = contact_dict[name].get_email()
        elif new_address == "":
            new_address = contact_dict[name].get_address()
            
            
        if name in contact_dict:
            contact_dict[name] = info(new_phone, new_email, new_address)
            print("\nContact updated\n")
            
        else:
            contact_dict[name] = info(new_phone, new_email, new_address)
            print("Contact not found, Added new contact!")
            
            
    elif user_input == "5":
        name = input("Enter name: ")
        contact_dict.pop(name)
        print("\n contact deleted")
        
        
    elif user_input == "6":
        break
    
    else:
        print("Invalid input")
        

for name in contact_dict:
        phone =contact_dict[name].get_phone()
        email = contact_dict[name].get_email()
        address = contact_dict[name].get_address()
        file.write(f"name: {name} phone: {phone} email: {email} address {address}")
file.close()