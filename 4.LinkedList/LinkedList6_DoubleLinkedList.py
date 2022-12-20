'''
다양한 링크드 리스트 구조 

기존의 링크드 리스트는 항상 앞에서부터 검색해야하는 단점이 있었다. 뒤에 있는 데이터도 무조건 앞에서부터 검색해야했다.
이런 단점을 보완한 게 더블 링크드 리스트

* 더블 링크드 리스트(Doubly linked list) 기본 구조 
  - 이중 연결 리스트라고도 함
  - 장점: 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능

  이전데이터 주소 | 데이터 | 다음데이터 주소 <-> 이전데이터 주소 | 데이터 | 다음데이터 주소 
  
  특정 데이터가 앞에 가까우면 앞에서부터 검색, 뒷부분에 가까우면 뒤에서부터 검색 가능 
'''

class Node:
    # 더블링크드 리스트는 주고가 2개
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

'''
앞으로 보게될 각 함수, 메서드들마다 이런 공통점이 있다

1. 현재 노드를 head노드, 처음 노드로 설정
node = head

2. 원하는 조건을 만족할 때까지 다음 노드로 이동 
node = node.next

즉, '처음(head)'부터 한번 쓱 살펴본다는 느낌
'''

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        # 처음에 노드가 하나라면 head나 tail 똑같
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            # 노드의 끝을 찾아가려는 작업
            while node.next:
                node = node.next
            # 위 반복문이 끝나면 node는 마지막 노드를 가리키고 있다.
            new = Node(data)
            node.next = new
            new.prev = node
            # tail은 마지막 노드
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next


double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

double_linked_list2 = NodeMgmt(None)
print(double_linked_list2.head)
