'''
앞으로 보게될 각 함수, 메서드들마다 이런 공통점이 있다

1. 현재 노드를 head노드, 처음 노드로 설정
node = head

2. 원하는 조건을 만족할 때까지 다음 노드로 이동 
node = node.next

즉, '처음(head)'부터 한번 쓱 살펴본다는 느낌
'''

# 특정 노드 삭제
'''
1. head 삭제
2. 마지막 노드 삭제
3. 중간 노드 삭제
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
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
    
    # 삭제
    def delete(self, data):
        # 방어 코드
        if self.head == '':
            print ("해당 값을 가진 노드가 없습니다.")
            return
        
        # 1) head 삭제하는 경우
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next # 두번째 노드인 self.head.next 를 head 노드로 설정
            del temp # 'del 객체'로 객체 삭제
        # 2) 삭제하는 노드가 head가 아닌 경우
        else:
            node = self.head # node는 head를 가리킴
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else: # 다음 노드로 이동
                    node = node.next

linkedlist1 = NodeMgmt(0) # linkedlist1.head -> Node(0)
linkedlist1.desc() # 0

# head가 살아있음을 확인
print(linkedlist1) # <__main__.NodeMgmt object at 0x7f8c00088fd0> 
print(linkedlist1.head) # <__main__.Node object at 0x7f7928190fa0>
print(linkedlist1.head.data, linkedlist1.head.next)
# head를 지워봄(위에서 언급한 경우의 수 1)
linkedlist1.delete(0)

# None이 나온다는 것은 linkedlist1.head 가 정상적으로 삭제되었음을 의미
print(linkedlist1.head) # None

# 다시 하나의 노드를 만들어봄
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# 이번엔 여러 노드를 더 추가해봄
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
print("-"*50)

# 노드 중에 한개를 삭제함 (위에서 언급한 경우의 수2)
linkedlist1.delete(4)

# 특정 노드가 삭제되었음을 알 수 있음
linkedlist1.desc()
print("-"*50)
linkedlist1.delete(9)
linkedlist1.desc()