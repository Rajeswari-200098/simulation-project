from stack import Stack
from queue import Queue

stack = Stack()
queue = Queue()

while True:
    print("\n--- MENU ---")
    print("1. Stack Push")
    print("2. Stack Pop")
    print("3. Stack Peek")
    print("4. Stack Display")
    print("5. Queue Enqueue")
    print("6. Queue Dequeue")
    print("7. Queue Front")
    print("8. Queue Display")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        stack.push(int(input("Enter value: ")))
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        queue.enqueue(int(input("Enter value: ")))
    elif choice == 6:
        queue.dequeue()
    elif choice == 7:
        queue.front()
    elif choice == 8:
        queue.display()
    elif choice == 9:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice")
