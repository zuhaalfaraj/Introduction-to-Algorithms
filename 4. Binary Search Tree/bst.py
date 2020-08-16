


class Node:
    def __init__(self,value=None):
        self.value= value
        self.left = None
        self.right= None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root= Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self,value,root):
        if value<root.value:
            if root.left==None:
                root.left=Node(value)
            else:
                self._insert(value, root.left)
        elif value>root.value:
            if root.right==None:
                root.right=Node(value)
            else:
                self._insert(value, root.right)

        else:
            print("value already there")
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if cur_node!= None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root!= None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node== None: return cur_height
        left_h= self._height(cur_node.left, cur_height+1)
        right_h = self._height(cur_node.right,cur_height+1)
        return max(left_h,right_h)

    def search(self,value):
        if self.root!= None:
            return self._search(value,self.root)
        else:
            return False
    def _search(self,value,cur_node):
        if value == cur_node.value:
            return True
        elif value <cur_node.value and cur_node.left != None:
            return self._search(value, cur_node.left)
        elif value >cur_node.value and cur_node.right != None:
            return self._search(value, cur_node.right)


        return False



if __name__ == "__main__":
    bts =BinarySearchTree()

    bts.insert(10)
    bts.insert(2)
    bts.insert(3)
    bts.insert(23)
    bts.insert(11)
    bts.insert(9)

    bts.print_tree()

    print(bts.search(2))

