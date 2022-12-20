'''
연습: 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고, 테스트해보기
- 더블 링크드 리스트의 tail 에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
- 테스트: 임의로 0 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드를 추가해보기
'''

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
    
    def search_from_head(self, data):
        if self.head == None:
            return False
    
        # 시작 노드 설정. head부터 찾기 시작
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False
    
    def search_from_tail(self, data):
        if self.head == None:
            return False

        # 시작 노드 설정. tail부터 찾기 시작    
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        # 맨 앞 노드까지 찾았는데도 찾는 data가 없으면 False 반환 
        return False
    
    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            # 시작 노드 설정. tail에서부터 검색 시작
            node = self.tail
            # 찾는 data가 아니면 계속 앞으로 이동
            while node.data != before_data:
                node = node.prev
                # 찾는 data가 없으면
                if node == None:
                    return False
            # node.data 가 찾는 data면 이제 반복문을 빠져나오고 아래 코드들이 실행
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()
print("="*50)

node_3 = double_linked_list.search_from_tail(3)
print(node_3.data)
print("="*50)

node_10 = double_linked_list.search_from_tail(10)
print(node_10) # False

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()

node_3 = double_linked_list.search_from_tail(1.5)
print(node_3.data)