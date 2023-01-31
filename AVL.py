class AVLnode:
    def __init__(self, key = None, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = None

class AVLtree:

    def __init__(self, key, value):

        self.root = AVLnode(key, value)

    def get(self, data):
        
        a = self.search(data, self.root)

        if a != None:

            return a.value
        
        return None

    def search(self, data, cur_node):
        if cur_node== None:
            return False

        elif data == cur_node.key:
            return cur_node
        
        if data < cur_node.key:
            return self.search(data, cur_node.left)
        else:
            return self.search(data, cur_node.right)
    
    def put(self, data, value = None):
        data = AVLnode(data, value)
        y = None
        x = self.root

        while x != None:
            y = x
            if data.key < x.key:
                x = x.left
            else: 
                x = x.right
        
        data.parent = y 

        if y == None:
            self.root = data
        
        elif data.key < y.key:
            y.left = data
        else:
            y.right = data
        
        self.setHeight(data, data.key) 

    def setHeight(self, node,newInsert = None):
        newInsert = newInsert
        node.height = self._setHeight(node)

        if newInsert != None:
            self.unbalanceDetector(node, newInsert)

        if node.parent != None:
            self.setHeight(node.parent, newInsert)

    def _setHeight(self, node):
        
        if node == None:
            return 0
        left = self._setHeight(node.left)
        right = self._setHeight(node.right)
        return max(left, right) + 1

    def __setHeight(self, node):

        if node != None:
            node.height = self._setHeight(node)
            self.__setHeight(node.left)
            self.__setHeight(node.right)

    def unbalanceDetector(self, node, newInsert):

        root = node
        if root.left != None:
            leftH = root.left.height

        else:
            leftH = 0

        if root.right != None:
            rightH = root.right.height
        else:
            rightH = 0

        bHeight = leftH - rightH

        if bHeight < -1 or bHeight > 1:
            self.directionDetector(node, bHeight, newInsert)

    
    def directionDetector(self, node, bfctor, newInsert):

        if bfctor > 1 and newInsert < node.left.key:
            self.leftRoation(node)
          
        elif bfctor < -1 and newInsert > node.right.key:
            self.rightRoation(node)
            
        elif bfctor > 1 and newInsert > node.left.key:
            self.rightRoation(node.left)
            self.leftRoation(node)
            
        elif bfctor < -1 and newInsert < node.right.key:
            self.leftRoation(node.right)
            self.rightRoation(node)
           
    
    def leftRoation(self, node):

        root = node
        pivot = node.left           #find the pivot in left side
     
        root.left = pivot.right     #move the right child of pivot to root
        #FIX2: add parent reset
        if pivot.right !=None:
            pivot.right.parent = root 
        pivot.right = root          #then pivot has right child root

        #reset their parent
        pivot.parent = root.parent  
        root.parent = pivot
        
        #if the pivot has parent
        if pivot.parent != None:

            #depends if pivot is in his parent left or right
            #according to the postion, insert pivot as child to his parent
            #FIX1: need to check if pivot.parent.left exists or not
            if pivot.parent.left !=None:
                if pivot.parent.left.key == root.key:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            else:
                pivot.parent.right = pivot
            
            #reset the height for parent above
            self.setHeight(pivot.parent)
        else:
            self.root = pivot

        #reset the height for pivot
        self.__setHeight(pivot)

    def rightRoation(self, node):

        root = node
        pivot = node.right

        root.right = pivot.left
        #FIX2: add parent reset
        if pivot.left !=None:
            pivot.left.parent = root 
        pivot.left = root

        pivot.parent = root.parent
        root.parent = pivot

        if pivot.parent != None:
            #FIXED: need to check if pivot.parent.left exists or not
            if pivot.parent.left !=None:
                if pivot.parent.left.key == root.key:
                    pivot.parent.left = pivot
                else:
                    pivot.parent.right = pivot
            else:
                pivot.parent.right = pivot

            self.setHeight(pivot.parent)
        else:
            self.root = pivot
        self.__setHeight(pivot)


    # Printing the tree
    def printTree(self):
        print("AVL tree:")
        self.__printTree(self.root)

    def __printTree(self, node, level=0):
        if node is None:
            return
        if node.value != None:
            self.__printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', str(node.key)+","+str(node.value)+","+str(node.height))
            self.__printTree(node.right, level + 1)


if __name__ == "__main__":
#15-bob, 20-anna, 24-tom, 10-david, 13-david, 7-ben, 30-karen, 36-erin, 25-david.
    T = AVLtree("lorem", 1)
    T.put("ipsum", 2)
    T.put("dolor", 3)
    T.put("sit", 4)
    T.put("amet", 5)
    T.put("consectetur", 6)
    T.printTree()

    T.printTree()

