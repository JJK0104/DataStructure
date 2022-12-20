'''
앞으로 보게될 각 함수, 메서드들마다 이런 공통점이 있다

1. 현재 노드를 head노드, 처음 노드로 설정
node = head

2. 원하는 조건을 만족할 때까지 다음 노드로 이동 
node = node.next

즉, '처음(head)'부터 한번 쓱 살펴본다는 느낌
'''

# 1) 링크드 리스트로 데이터 추가하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head # add 함수가 실행될 때마다 node는 head(=node1)로 설정됨
    while node.next: # 다음 노드인 node.next 가 있으면 계속 반복 실행... node.next가 None일 때까지
        # 이 과정은 add(data) 실행 전 구성된 링크드 리스트의 마지막 노드로 이동하는 과정이라고 생각해도 된다. 
        node = node.next # 현재 node를 다음 노드 node.next로 설정
    node.next = Node(data) # node.next = None이면, 마지막 노드면 마지막 노드에 Node(data)를 연결

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

# 2) 링크드 리스트 데이터 출력하기(검색하기)
node = head # head = node1 
while node.next: # 1) 링크드 리스트로 데이터 추가하기와 비슷한 개념
    print(node.data) # 데이터를 출력하고 다음 노드로 이동... 언제까지? node.next가 마지막 노드일 때 까지(node.next가 None)
    node = node.next 
print (node.data) # 마지막 데이터 출력하기

#  이렇게 써도 된다.
# while node:
#     print (node.data)
#     node = node.next

##########################################################################

# 3) 링크드 리스트 데이터 사이에 데이터를 추가
node3 = Node(1.5)  

'''
node3을 node1과 node2 사이에 넣을려면
node1.next -> node3 , node3.next -> node2
'''
node = head # head = node1 ... 현재 node1은 위의 2) add(index)로 인해 다른 노드들과 연결된 상태
search = True

# while문 안에서 node = node.next는 우리가 '원하는 노드'로 '이동'하는 과정이다.
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next # 다음 노드로 이동하는 과정... 1),2)와 같은 개념

# while문을 빠져나오면 현재 node는 node.data = 1 인 노드, node.next -> node2 가리키고 있겠지
node_next = node.next
node.next = node3 # node1.next -> node3으로 설정
node3.next = node_next # node3.next  -> node2로 설정

node = head
while node.next:
    print(node.data)
    node = node.next
print (node.data)