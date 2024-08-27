
# this is creating a node and initialize the node value. 

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Print_LL(self):
        if self.head is None:
            print("Lisked list Empty")
        else:
            n = self.head        
            while n is not None:
                print(n.data)
                n = n.ref

LL1 = LinkedList()
LL1.Print_LL()