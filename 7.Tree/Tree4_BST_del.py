'''
이진 탐색 트리 삭제 
* 매우 복잡함. 경우를 나누어서 이해하는 것이 좋음

1. Leaf Node 삭제 
* Leaf Node: Child Node 가 없는 Node
삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다. 

2. Child Node 가 하나인 Node 삭제 
 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.

3. Child Node 가 두 개인 Node 삭제
- 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다. (선택한 Node를 삭제한 노드 자리에 넣는다고 생각)
- 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다. (선택한 Node를 삭제한 노드 자리에 넣는다고 생각)


3.1. 삭제할 Node의 오른쪽 자식중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우
- 삭제할 Node의 오른쪽 자식 선택
- 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택 ( 이 노드는 삭제한 노드보다 큰 노드들 중에서 가장 작은 노드)
- 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
- 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
- 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
- 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는, 해당 Node의 본래 Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함
'''



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        # 여기까지 왔다는 건 BST에 해당 value를 가진 노드가 없다는 거
        return False  


    # 1. 삭제할 Node 탐색
    # 삭제할 Node가 없는 경우도 처리해야 함
    # 이를 위해 삭제할 Node가 없는 경우는 False를 리턴하고, 함수를 종료 시킴
    def delete(self, value):
        searched = False
        # 초기 노드, current_node에는 삭제할 노드를 가리키게 할 거임
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        if searched == False:
            return False

        # 현재 self.current_node는 삭제할 노드를 가리키고 있는 상태

        ### 이후부터 Case들을 분리해서, 코드 작성
        # Case1: 삭제할 Node가 Leaf Node 인 경우
        # self.current_node 가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
        if  self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        
        # Case2: 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
        # Case2-1: 삭제할 노드가 왼쪽에 Child Node를 한개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        # Case2-2: 삭제할 노드가 오른쪽에 Child Node를 한개 가지고 있을 경우
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        #  Case3: 삭제할 노드가 Child Node를 두 개 가지고 있을 경우
        #  Case3-1: 삭제할 Node가 Parent Node 왼쪽에 있을 때
        #  기본 사용 가능 전략
        #   1. 삭제할 Node의 오른쪽 자식 중, 가장 작은 값(가장 왼쪽 노드)을 삭제할 Node의 Parent Node가 가리키도록 한다.
        #   2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값(가장 오른쪽 노드)을 삭제할 Node의 Parent Node가 가리키도록 한다.
        # * 기본 사용 가능 전략 중, 1번 전략을 사용하여 코드를 구현하기로 함
        #   - 경우의 수가 또다시 두가지가 있음
        #     - Case3-1-1: 삭제할 Node가 Parent Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node가 없을 때
        #     - Case3-1-2: 삭제할 Node가 Parent Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
        #        - 가장 작은 값을 가진 Node의 Child Node가 왼쪽에 있을 경우는 없음, 왜냐하면 왼쪽 Node가 있다는 것은 해당 Node보다 더 작은 값을 가진 Node가 있다는 뜻이기 때문임
        if self.current_node.left != None and self.current_node.right != None: # case3
            if value < self.parent.value: # case3-1
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # 반복문이 끝나면 self.change_node는 가장 작은 값을 가진(가장 왼쪽) 노드
                if self.change_node.right != None: # case3-1-2
                    self.change_node_parent.left = self.change_node.right
                else: # case3-1-1
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left

        # Case3-2: 삭제할 Node가 Parent Node 오른쪽에 있을 때
        # * 기본 사용 가능 전략
        #   1. 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다. 
        #   2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
        # * 기본 사용 가능 전략 중, 1번 전략을 사용하여 코드를 구현하기로 함
        #   - 경우의 수가 또다시 두가지가 있음
        #     - Case3-2-1: 삭제할 Node가 Parent Node의 오른쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node가 없을 때
        #     - Case3-2-2: 삭제할 Node가 Parent Node의 오른쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
        #        - 가장 작은 값을 가진 Node의 Child Node가 왼쪽에 있을 경우는 없음, 왜냐하면 왼쪽 Node가 있다는 것은 해당 Node보다 더 작은 값을 가진 Node가 있다는 뜻이기 때문임
        else: # Case 3-2
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None: # Case3-2-2
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right