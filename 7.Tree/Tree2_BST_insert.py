# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기 

# 노드 클래스 만들기
# 더블 링크드 리스트랑 비슷
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 탐색 트리에 데이터 넣기
# 이진 탐색 트리 조건에 부함하게 데이터를 넣어야 함
class NodeMgmt:
    def __init__(self, head):
        self.head = head # 루트 노드를 head로 지칭
    
    def insert(self, value):
        # 링크드 리스트와 비슷하게 이제 이 노드가 트리를 순회해야된다.
        # 초기 노드 설정
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                # 만약 이미 노드가 있다면 
                if self.current_node.left != None:
                    # 노드 이동, 비교할 대상을 바꾸고 끝
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else: # 크거나 같을 경우
                if self.current_node.right != None:
                    # 노드 바꾸기, 이동하고 끝
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
