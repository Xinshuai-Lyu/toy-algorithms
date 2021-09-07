class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0

def get_poiner(object):
    pass

def dereference_pointer(pointer):
    pass
        
class XORLinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            self.__add__(0, self.head, node)
            
    def __add__(self, prev_node_pointer, current_node, new_node):
        next_node = dereference_pointer(prev_node_pointer ^ current_node.both)
        while next_node:
            prev_node_pointer = get_poiner(current_node)
            current_node = next_node
            next_node = dereference_pointer(prev_node_pointer ^ next_node.both)
        next_node_pointer = get_poiner(new_node)
        both = prev_node_pointer ^ next_node_pointer
        current_node.both = both
        new_node.both = get_poiner(current_node)
        
    def get(index):
        i = 0
        if index == i:
            return self.head
        else:
            current_node = self.head
            next_node = dereference_pointer(current_node.both)
            while next_node:
                i += 1
                if index == i:
                    return next_node
                prev_node_pointer = get_poiner(current_node)
                current_node = next_node
                next_node = dereference_pointer(prev_node_pointer ^ next_node.both)
                
