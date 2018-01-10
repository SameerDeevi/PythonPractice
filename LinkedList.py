class Node:
    def __init__(self, FirstElement):
        self.data = FirstElement
        self.next = None

    def getdata(self):
        return self.data

    def setdata(self,newdata):
        self.data = newdata

    def getnext(self):
        return self.next

    def setnext(self,newnode):
        self.next = newnode

        
        
class Linkedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def Add(self, newdata):
        temp = Node(newdata)
        temp.setnext(self.head)
        self.head = temp

    def display(self):
        current = self.head
        while current != None:
            print(current.getdata())
            current = current.getnext()


mylist = Linkedlist()
mylist.Add(1)
mylist.Add(12)

            
        

