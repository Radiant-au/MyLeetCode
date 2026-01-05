class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self , value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 
        
    def delete(self , target):
        current = self.head
        previous = None
        while current:
            if current.value == target:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
            
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
            
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.prepend(0)
ll.delete(2)