class Node:

    def __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):

        if self.data:

            if data < self.data:

                if self.left is None:

                    self.left = Node(data)

                else:

                    self.left.insert(data)
            else:

                if self.right is None:

                    self.right = Node(data)

                else:

                    self.right.insert(data)
        else:

            self.data = data


    def findval(self, val):

        if self.data:

            if val < self.data:

                if self.left is None:

                    return str(val) + " not found"

                else:

                    return self.left.findval(val)

            elif  val > self.data:

                if self.right is None:

                    return str(val) + " not found"

                else:

                   return self.right.findval(val)
            else:

                print(str(val) + " found")

    #inorder as well
    def PrintTree(self):

        if self.left:
            self.left.PrintTree()

        print(self.data)

        if self.right:
            self.right.PrintTree()
                    
    def PrintLeftViewUtil(self,level,maxlevel):

        

        if maxlevel[0] < level:

            print(self.data)
            maxlevel[0] = level
        
        if self.left:
            self.left.PrintLeftViewUtil(level+1,maxlevel)

        if self.right:
            self.right.PrintLeftViewUtil(level+1,maxlevel)
        
    def PrintLeftView(self):
          
        level = 1
        maxlevel = [0]
        self.PrintLeftViewUtil(level, maxlevel)
















                    
