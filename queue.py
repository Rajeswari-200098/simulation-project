from node import Node

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        print(f"{data} added to queue")

    def dequeue(self):
        if self.front_node is None:
            print("Queue Underflow")
            return
        removed = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        print(f"{removed} removed from queue")

    def front(self):
        if self.front_node is None:
            print("Queue is empty")
            return
        print("Front element:", self.front_node.data)

    def display(self):
        temp = self.front_node
        if temp is None:
            print("Queue is empty")
            return
        print("Queue elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
