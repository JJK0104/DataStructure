'''
앞으로 보게될 각 함수, 메서드들마다 이런 공통점이 있다

1. 현재 노드를 head노드, 처음 노드로 설정
node = head

2. 원하는 조건을 만족할 때까지 다음 노드로 이동 
node = node.next

즉, '처음(head)'부터 한번 쓱 살펴본다는 느낌
'''

# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        # 방어 코드
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next: # 맨뒤의 노드로 찾아가는 과정
                node = node.next
            node.next = Node(data) # 맨뒤의 노드로 갔으면 Node(data) 연결
        
    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()