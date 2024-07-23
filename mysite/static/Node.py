class Node():
    def __init__(self,name='',addr='',rankingPos=0,numberRev=0,cur=[]) -> None:
        self.name = name
        self.addr = addr
        self.rankingPos=rankingPos
        self.numberRev=numberRev
        self.cur=cur
        self.next = None
    def __str__(self):
        return f'name = {self.name} \naddr={self.addr}\ncur={self.cur}'

