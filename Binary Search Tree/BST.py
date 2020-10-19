
class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.parent = parent
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertion(self, root, val):
        if root == None:
            self.root = Node(key=val)
        else:
            if val > root.key:
                if root.right == None:
                    root.right = Node(key=val, parent=root)
                else:
                    self.insertion(root.right, val)

            elif val < root.key:
                if root.left == None:
                    root.left = Node(key=val, parent=root)
                else:
                    self.insertion(root.left, val)
            else:
                print("Value already exist")

    def printTree(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while q:
            count = len(q)
            while count > 0:
                temp = q.pop(0)
                if temp.key == None:
                    print(None, end=' ')
                else:
                    print(temp.key, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                count -= 1
            print('')

    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return obj.minDepth(root.right) + 1
        if root.right == None:
            return obj.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


    def maxDepth(self, root):
        if root == None:
            return 0
        l_height = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)

        if (l_height > r_height):
            return l_height + 1
        else:
            return r_height + 1


def findLCA(root, n1, n2):

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


obj = BinarySearchTree()
numbers = open('numbers.txt', 'r')
content_file = numbers.read()
# SList = (list(map(int, content_file.split())))
# SList = [5, 8, 3, 2, 1, 7, 9, 4, 10, 6]
# print(SList)
SList = [4, 2, 6, 5, 3, 7, 1]

for i in SList:
    obj.insertion(obj.root, i)
print('\nIn-order Tree Traversal ::')
obj.printTree(obj.root)

print('\n{:<35} {}'.format('Minimum Depth of Binary Search Tree:',obj.minDepth(obj.root)))
print('{:<35} {}'.format('Maximum Depth of Binary Search Tree:',obj.maxDepth(obj.root)))

ancestors = list(map(int, input('Enter values for which we need to find LCA (two elements, space separated): ').split()))
lca = findLCA(obj.root, ancestors[0], ancestors[1]).key
print('\nLeast Common Ancestor for Given Nodes :', lca)