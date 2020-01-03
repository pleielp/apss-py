class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return '{}'.format(self.data)

class LinkedList(object):
    def __init__(self):
        head = Node("head")
        self.head = head
        self.tail = head
        self.current = None
        self.data_num = 0

    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.data_num += 1

    def delete(self):
        pop_data = self.current.data

        if not self.current.next:
            self.tail = self.current.prev
            self.current.prev.next = None
        else:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev

        if self.current.prev is self.head:
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = None
        else:
            self.current = self.current.prev

        self.data_num -= 1

        return pop_data
            
    def first(self):
        if self.data_num == 0:
            return None

        self.current = self.head.next
        return self.current.data

    def next(self):
        if self.current.next == None:
            return None
        
        self.current = self.current.next
        return self.current.data

    def __str__(self):
        node = self.head.next
        array = list()
        while node:
            array.append(node.data)
            node = node.next
        return '{}'.format(array)

linked_list = LinkedList()
linked_list.append(2)
linked_list.append(5)
linked_list.append(7)
print(linked_list)
print(linked_list.first())
print(linked_list.next())
print(linked_list.delete())
print(linked_list.delete())
print(linked_list)
print(linked_list.delete())
print(linked_list)
