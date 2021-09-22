class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __eq__(self, other):
        if other == None: return False
        return self.val == other.val
memory = {}
def all_equal(root, left, right):
    if str(root) in memory:
        return memory[str(root)]
    if left == None and right == None:
        memory[str(root)] = True
        return True
    elif right == None:
        result = all_equal(left, left.left, left.right)
        memory[str(root)] = (result and left == root)
        return (result and left == root)
    elif left == None:
        result = all_equal(right, right.left, right.right)
        memory[str(root)] = (result and right == root)
        return (result and right == root)
    else:
        if left == right and left == root:
            left_result = all_equal(left, left.left, left.right)
            right_result = all_equal(right, right.left, right.right)
            result = (left_result and right_result)
            memory[str(root)] = result
            return result
        else:
            memory[str(root)] = False
            return False
def count_unival_tree(root):
    if root == None: return 0
    count_left_unival_tree = count_unival_tree(root.left)
    count_right_unival_tree = count_unival_tree(root.right)
    # all nodes under a tree have the same value 
    if all_equal(root, root.left, root.right):
        return count_left_unival_tree + count_right_unival_tree + 1
    else:
        return count_left_unival_tree + count_right_unival_tree
def start_count_unival_tree(root):
    global memory
    if memory: memory = {}
    result = count_unival_tree(root)
    return result
    
def count_unival_tree_without_memory(root):
    if root == None: return 0, True
    left_unival_tree_count, is_left_unival_tree = count_unival_tree_without_memory(root.left)
    right_unival_tree_count, is_right_unival_tree = count_unival_tree_without_memory(root.right)
    if is_left_unival_tree and is_right_unival_tree:
        if root.left and root.left != root:
            return left_unival_tree_count + right_unival_tree_count, False
        elif root.right and root.right != root:
            return left_unival_tree_count + right_unival_tree_count, False
        elif root.left != root.right:
            return left_unival_tree_count + right_unival_tree_count, False
        else:
            return left_unival_tree_count + right_unival_tree_count + 1, True
    else:
        return left_unival_tree_count + right_unival_tree_count, False

"""
  1
 2  1
3 1 3 
"""
        
root = Node(1)
root.left = Node(2)
root.right = Node(1)
root.left.left = Node(3)
root.left.right = Node(1)
root.right.left = Node(3)

print(count_unival_tree_without_memory(root))
print(start_count_unival_tree(root))

