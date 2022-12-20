'''
앞으로 보게될 각 함수, 메서드들마다 이런 공통점이 있다

1. 현재 노드를 head노드, 처음 노드로 설정
node = head

2. 원하는 조건을 만족할 때까지 다음 노드로 이동 
node = node.next

즉, '처음(head)'부터 한번 쓱 살펴본다는 느낌
'''

# Node 구현
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

# 링크드 리스트로 데이터 추가하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head # add 함수가 실행될 때마다 node는 head로 설정됨
    while node.next: # node.next 가 있으면 
        node = node.next # 현재 node를 node.next로 저장
    node.next = Node(data) # node.next = None이면, 마지막 Node면 실행됨 

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

# 링크드 리스트 데이터 출력하기(검색하기)
node = head # head = node1 
while node.next:
    print(node.data)
    node = node.next
print (node.data)