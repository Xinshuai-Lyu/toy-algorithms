class BinaryTree:
    class Node:
        def __init__(self, instance, left=None, right=None):
            self.instance = instance
            self.left = left
            self.right = right
        def __eq__(self, other):
            return self.instance == other.instance
        def __gt__(self, other):
            return self.instance > other.instance
        def __lt__(self, other):
            return self.instance < other.instance
        def __ge__(self, other):
            return self.instance >= other.instance
        def __le__(self, other):
            return self.instance <= other.instance
        def __str__(self):
            return str(self.instance)
    def __init__(self, root=None):
        self.root = root
    def insert(self, instance):
        new_node = BinaryTree.Node(instance)
        if not self.root:
            self.root = new_node
        else:
            self.__insert__(new_node, self.root)
    def __insert__(self, new_node, parent):
        if new_node >= parent:
            if not parent.right:
                parent.right = new_node
            else:
                self.__insert__(new_node, parent.right)
        else:
            if not parent.left:
                parent.left = new_node
            else:
                self.__insert__(new_node, parent.left)
        
def serialize(tree):
    return str(tree.instance)
        
def serialize_tree(tree):
    if not tree: return ""
    root = serialize(tree)
    left_tree = serialize_tree(tree.left)
    right_tree = serialize_tree(tree.right)
    left_separate = "" if left_tree == "" else " "
    right_separate = "" if right_tree == "" else " "
    return root + left_separate + left_tree + right_separate + right_tree

def deserialize(tree_str):
    L = tree_str.split(" ")
    binary_tree = BinaryTree()
    for instance in L:
        binary_tree.insert(int(instance))
    return binary_tree
    
L = [54, 32, 51, 1, 5,15353, 136, -5]
binary_tree = BinaryTree()
for instance in L:
    binary_tree.insert(instance)

serialize_tree_result = serialize_tree(binary_tree.root)
assert(serialize_tree_result == "54 32 1 -5 5 51 15353 136")
recovered_binary_tree = deserialize(serialize_tree_result)
assert(recovered_binary_tree.root.left.left.instance == 1)
assert(recovered_binary_tree.root.instance == 54)
assert(recovered_binary_tree.root.right.instance == 15353)
assert(recovered_binary_tree.root.right.left.instance == 136)






