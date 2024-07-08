import Node
class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def add_node(self,name='',addr='',rankingPos=0,numberRev=0,cur=[]) -> None:
        new_node = Node.Node(name,addr,rankingPos,numberRev,cur)
        if self.head :
            self.tail.next = next
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        