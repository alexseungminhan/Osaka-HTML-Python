from static.Node import Node
class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def add_node(self,name='',addr='',rankingPos=0,numberRev=0,cur=[]) -> None: #값을 다 받는 경우
        new_node = Node(name,addr,rankingPos,numberRev,cur)
        #print('new_node')
        #print(new_node)
        if self.head :
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node


    def print_node(self):
        if self.head is None:
            print("empty list")
            return None
        
        cur = self.head
        
        while cur!=None:
            print(cur)
            cur=cur.next
    
    def find_list(self, search, selectedOption,orderOption,Vegan_option,Vegetarian_friendly,Gluten_free):

        search_lower=search.lower()
        print(selectedOption)
        result = []

        cur = self.head
        while cur!=None:
            if search_lower in cur.name.lower():
                
                if selectedOption=='Reviews':
                    temp_data = cur.numberRev
                else:
                    selectedOption='Ranking'
                    temp_data = cur.rankingPos
                '''
                if Vegan_option=='on' and 'vegan option' not in cur.cur:
                    cur=cur.next
                    continue
                if Vegetarian_friendly=='on' and 'vegetarian friendly' not in cur.cur:
                    cur=cur.next
                    continue
                if Gluten_free=='on' and 'gluten free' not in cur.cur:
                    cur=cur.next
                    continue
                '''

                result.append({
                    'name':cur.name,
                    'addr':cur.addr,
                    selectedOption:temp_data})
    
            cur=cur.next

        if orderOption == 'Ascending':
            result.sort(key=lambda x:x[selectedOption])
        elif orderOption == 'Descending':
            result.sort(key=lambda x:x[selectedOption],reverse=True)
        
        return result
        