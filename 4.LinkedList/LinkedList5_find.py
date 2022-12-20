'''
앞으로 보게될 각 함수, 메서드들마다 이런 공통점이 있다

1. 현재 노드를 head노드, 처음 노드로 설정
node = head

2. 원하는 조건을 만족할 때까지 다음 노드로 이동 
node = node.next

즉, '처음(head)'부터 한번 쓱 살펴본다는 느낌
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print ('해당 값을 가진 노드가 없습니다.')
            return
        if self.head.data == data: # 경우의 수1: self.head를 삭제해야할 경우 - self.head를 바꿔줘야 함
            temp = self.head # self.head 객체를 삭제하기 위해, 임시로 temp에 담아서 객체를 삭제했음
            self.head = self.head.next # 만약 self.head 객체를 삭제하면, 이 코드가 실행이 안되기 때문!
            del temp
        else:
            node = self.head
            while node.next: # 경우의 수2: self.head가 아닌 노드를 삭제해야할 경우
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next       
                    del temp                         
                    pass                             
                else:
                    node = node.next
                    
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

# 테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print (node.data)