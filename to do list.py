def todo_list():
    todos = []
    while True:
        print("\n1. Add Todo")
        print("2. Show Todos")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            todo = input("Enter Todo: ")
            todos.append(todo)
        elif choice == 2:
            print("\nTodos:")
            for todo in todos:
                print(f"- {todo}")
        elif choice == 3:
            break

todo_list()
