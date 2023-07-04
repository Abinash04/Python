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
        # if self.length == 0:
        #     return None
        temp = self.head
        while temp is not None:
            print("print_list:", temp.value)
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
            
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False    # if success then true else false
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next   # more to understand
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None     # none: as we are returning a node
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        temp.next = self.get(index + 1)
        prev.next = None

        self.length -= 1
        return temp
        
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        



ll = LinkedList(3)
ll.append(4)
ll.append(6)
# ll.pop()
ll.print_list()
print(ll.pop())
# print(ll.pop())
# print(ll.pop())
ll.prepend(9)
ll.print_list()
ll.pop_first()
ll.print_list()
print(f"get value:{ll.get(1)}")
ll.set_value(0,5)
ll.print_list()
ll.insert(1,13)
ll.print_list()
ll.remove(2)
ll.print_list()
ll.reverse()
ll.print_list()
