def add_to_list(task):
    to_do_list.append(task)
    print(f"{task} added successfully\n")
    
def update_from_list(old_task,new_task):
    if old_task in to_do_list:
        for index , task in enumerate(to_do_list):
            if task == old_task:
                to_do_list[index] = new_task
                print(f"{old_task} updated to {new_task}")
    else:
        print(f"{old_task} not found")
        
def display_list():
    if len(to_do_list) >= 1:
        for index , task in enumerate(to_do_list):
            print(f"{index + 1}. {task}")
    else:
        print("List is empty\n")
    print()


file = open("to_do_list.txt","a")
print("Welcome to to do list")
to_do_list = []

while True:
    print("Main Menu")
    print("1. Add")
    print("2. update")
    print("3. show list")
    print("4. exit\n")
    
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        task = input("Enter task to add: ")
        add_to_list(task)
        
    elif user_input == "2":
        old_task = input("Enter task you want to update: ")
        new_task = input("Enter updated task: ")
        update_from_list(old_task, new_task)
        
    elif user_input == "3":
        display_list()
        
    elif user_input == "4":
        break
    
    else:
        print("\n invalid input")
        
for entry in enumerate(to_do_list):
    file.write(entry)
    
file.close()