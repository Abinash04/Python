'''
Doubly Linked List
{
    "value":4,
    "next: None,
    "prev": None
}
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # print DLL
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return True


    # Append
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            new_node.prev = None
            new_node.next = None
            self.length += 1
            return True

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    # pop
    def pop(self):
        # case1: if no items
        if self.length == 0:
            return None
        # case2: if 1 item
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        # case3: if > 1 items
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp.value

    # prepend
    def prepend(self, value):
        new_node = Node(value)
        # case1: if no items
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # case2: if 1 or more items
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        return True

    # pop first
    def pop_first(self):        
        # case1: if no items
        if self.length == 0:
            return None
        
        temp = self.head
        # case2: if 1 item
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # if > 1 items
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        self.length -= 1
        return temp

    # get
    def get(self, index):
        # case1: if index is out of range
        if index < 0 or index >= self.length:
            return None
            
        # case2: if index is within range
        temp = None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp


    # set
    def set_value(self, index, value):
        # new_node = Node(value)
        # current_value = self.get(index)
        # next_value = self.get(index+1)
        # prev_value = self.get(index-1)
        # prev_value.next = new_node
        # new_node.next = next_value

        # alternate way
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # insert
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length +=1
        return True

    # remove
    def remove(self, index):
        if index < 0 or index >= self.length: 
            return False
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()

        current_value = self.get(index)
        prev_value = self.get(index-1)
        current_value.next.prev = current_value.prev
        prev_value.next = current_value.next
        current_value.next = None
        current_value.prev = None

        self.length -=1
        return True
        
        



my_doubly_linked_list = DoublyLinkedList(7)
# print(my_doubly_linked_list)
# my_doubly_linked_list.print_list()
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(61)

print("Appending:", my_doubly_linked_list.print_list())
print("Popping:", my_doubly_linked_list.pop())
print("Prepend:", my_doubly_linked_list.prepend(12))
print("Popping:", my_doubly_linked_list.pop())
print("Prepend:", my_doubly_linked_list.prepend(42))
my_doubly_linked_list.print_list()
print("PopFirst:", my_doubly_linked_list.pop_first().value)
my_doubly_linked_list.print_list()
print("Get index:", my_doubly_linked_list.get(2).value)
my_doubly_linked_list.set_value(1,16)
my_doubly_linked_list.print_list()
my_doubly_linked_list.insert(1,8)
print("**********")
print("Insert:", my_doubly_linked_list.print_list())
my_doubly_linked_list.remove(1)
print("**********")
my_doubly_linked_list.print_list()









