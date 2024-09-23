def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # to_add = input("Enter item to add: ")
            to_add = input("Enter the item to add: ")
            shopping_list.append(to_add)
        elif choice == '2':
            to_remove = input("Enter the item to remove: ")
            if to_remove in shopping_list:
                shopping_list.remove(to_remove)
            else:
                print("Item not found")
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
