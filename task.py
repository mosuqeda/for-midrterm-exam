# Press 1 SHOW ALL DATA
# Press 2 ADDED SINGLE DATA 
# Press 3 ADD MULTIPLE DATA
# Press 4 DELETE
# Press 5 DELETE ALL DATA
# Press 6 UPDATE DATA
data = ["Carlos", "James", "Garay", "Mosqueda"]

def show_all_data():
    if data:
        print(data)
    else:
        ("No Existent Data")
    
    print(data)
        
def add_single_data():
    user = input("Input a Data: ")
    data.append(user)
    print(data)

def add_multiple_data():
    user1 = int(input("how many data would you want to add?: "))
    for i in range(user1):
        ask = input("Input a Data: ")
        print("multiple data was added")
    
    print(data)
    
def remove_data():
    user2 = input("remove a data: ")
    if user2 in data:
        data.remove(user2)
        print("Data has been cut")
    else:
        print("Data not found")
        
    print(data)
        
def remove_all_data():
    data.clear()
    print("All Data has been removed")
    
    print(data)
    
def update_data():
    show_all_data()
    old_user = input("input data to update: ")
    if old_user in data:
        new_user = input("New Data:")
        index = data.update(old_user)
        data[index] = new_user
        print(old_user, + " updated to " + new_user )
    else:
        print("Data not Found")
        
    print(data)
        
def main():
    while True:
        print("Menu")
        print("Press [1] SHOW ALL DATA")
        print("Press [2] ADDED SINGLE DATA ")
        print("Press [3] ADD MULTIPLE DATA")
        print("Press [4] DELETE")
        print("Press [5] DELETE ALL DATA")
        print("Press [6] UPDATE DATA")
        print("Press [7] Exit")
        
        users = int(input('Select from 1 to 7.:'))
        
        if users == 1:
            show_all_data()
        if users == 2:
            add_single_data()
        if users == 3:
            add_multiple_data()
        if users == 4:
            remove_data()
        if users == 5:
            remove_all_data()
        if users == 6:
            update_data()
        if users == 7:
            print("THE END")
            break
        else:
            print("ERROR")


main()