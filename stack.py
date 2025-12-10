from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed to stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        popped = self.top.data
        self.top = self.top.next
        print(f"{popped} popped from stack")

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        print("Top element:", self.top.data)

    def display(self):
        temp = self.top
        if temp is None:
            print("Stack is empty")
            return
        print("Stack elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
