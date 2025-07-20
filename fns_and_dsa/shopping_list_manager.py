def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")



from shopping_list_manager import display_menu

def main():
    shopping_list = []


    while True:
        display_menu()
        choice = input("Enter your choice (1 - 4): ")

        if choice == '1':
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)
            print(f"Successfully added '{item}'.")

        elif choice == '2':
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Successfully removed '{item}'.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("Shopping List: ")
                for i in range(len(shopping_list)):
                    print(f"{i + 1}. {shopping_list[i]}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


