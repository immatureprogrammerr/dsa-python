# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List
class SinglyLinkedList:

    # Contructor function
    def __init__(self):
        self.head = None

    # function to append a node in Linked list
    def append(self, data):
        new_node = Node(data)

        # if the new node is the first node to be added
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # function to display the nodes in a Linked list
    def display(self):

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # function to delete a node
    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:
            print("key is not found")
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
    
    # reverse a Linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
    
    # check if Linked list is Palindrome
    def is_palindrome(self):
        stack = []
        current = self.head

        while current:
            stack.append(current.data)
            current = current.next

        current = self.head

        while current:
            if current.data != stack.pop():
                return False
            current = current.next
        return True
    # Get the middle of the Linked list
    def get_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data if slow else None


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(2)
    sll.append(1)
    sll.display()
    sll.reverse()
    sll.display()
    print(sll.is_palindrome())
    print(sll.get_middle())