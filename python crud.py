database = []

def create_record():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    record = {
        'id': len(database) + 1,
        'name': name,
        'age': age,
        'email': email
    }
    database.append(record)
    print("Record created successfully.")

def read_records():
    if not database:
        print("No records found.")
    else:
        for record in database:
            print(f"ID: {record['id']}, Name: {record['name']}, Age: {record['age']}, Email: {record['email']}")

def update_record():
    record_id = int(input("Enter the ID of the record to update: "))
    for record in database:
        if record['id'] == record_id:
            name = input(f"Enter new name (current: {record['name']}): ")
            age = input(f"Enter new age (current: {record['age']}): ")
            email = input(f"Enter new email (current: {record['email']}): ")
            record['name'] = name if name else record['name']
            record['age'] = age if age else record['age']
            record['email'] = email if email else record['email']
            print("Record updated successfully.")
            return
    print("Record not found.")

def delete_record():
    record_id = int(input("Enter the ID of the record to delete: "))
    for record in database:
        if record['id'] == record_id:
            database.remove(record)
            print("Record deleted successfully.")
            return
    print("Record not found.")

def menu():
    while True:
        print("\nCRUD Operations Menu:")
        print("1. Create a record")
        print("2. Read all records")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_record()
        elif choice == '2':
            read_records()
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
