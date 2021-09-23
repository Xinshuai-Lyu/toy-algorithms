"""
Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de 
and the set of strings [dog, deer, deal], return [deer, deal].
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __le__(self, other):
        if self.val <= other.val:
            return True
class Binary_Search_Tree:
    def __init__(self):
        self.root = None
    def __insert__(self, parent, node):
        if not self.root:
            self.root = node
        else:
            if parent <= node:
                if not parent.right:
                    parent.right = node
                else:
                    self.__insert__(parent.right, node)
            else:
                if not parent.left:
                    parent.left = node
                else:
                    self.__insert__(parent.left, node)
    def insert(self, val):
        node = Node(val)
        self.__insert__(self.root, node)
set_of_strings = set(["dog", "deer", "deal", "great", "male", "female", "nice", "ice", "good"])
bst = Binary_Search_Tree()
for string in set_of_strings:
    bst.insert(string)
def get_matched_result(root, query):
    result = []
    if root:
        val = root.val
        if val[0:len(query)] == query:
            result.append(root.val)
            result.extend(get_matched_result(root.left, query))
            result.extend(get_matched_result(root.right, query))
        elif val[0:len(query)] < query:
            result.extend(get_matched_result(root.right, query))
        else:
            result.extend(get_matched_result(root.left, query))
    return result
print(get_matched_result(bst.root, "de"))
print(get_matched_result(bst.root, "g"))
print(get_matched_result(bst.root, "nice"))
print(get_matched_result(bst.root, "s"))
print(get_matched_result(bst.root, "d"))
print(get_matched_result(bst.root, "niced"))
