# operations

'''
Below 3 will add a new node so we will create a class Node.
append
prepend
insert


get
pop
pop_first
'''
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)  # local variable - scope is within this constructor
        self.head = new_node    # instance variable - can be accessed/modified anywhere within the class
        self.tail = new_node
        self.length = 1

    def print_list(self):
        # 2 cases
        # i) if no nodes
        # ii) if 1 or more nodes
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)

        # if no nodes present
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
            
            


ll = LinkedList(3)
ll.append(4)
ll.append(6)
ll.print_list()