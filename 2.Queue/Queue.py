'''
큐 (Queue)

1. 큐 구조
* 줄을 서는 행위와 유사
* 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
  - 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
  - FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대
  
2. 알아둘 용어
* Enqueue: 큐에 데이터를 넣는 기능
* Dequeue: 큐에서 데이터를 꺼내는 기능

3. 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
* queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue() 제공
* 프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조를 사용
  - Queue(): 가장 일반적인 큐 자료 구조
  - LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
  - PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력
  
* 일반적인 큐 외에 다양한 정책이 적용된 큐들이 있음
'''

# 1. Queue()로 큐 만들기 (가장 일반적인 큐, FIFO(First-In, First-Out))

import queue
data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(10)
print(data_queue) # <queue.Queue object at 0x7f8fa00853a0>
print(data_queue.qsize()) # 2
print(data_queue.get()) # 'funcoding'
print(data_queue.qsize()) # 1
print(data_queue.get()) # 10

# 2. LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out))
data_queue = queue.LifoQueue()
data_queue.put("funcoding")
data_queue.put(10)
print(data_queue.qsize()) # 2
print(data_queue.get()) # 10

# 3. PriorityQueue()로 큐 만들기
data_queue = queue.PriorityQueue()

# 첫번째 인자가 우선순위, 두번째 인자가 data
# 우선순위가 작을수록 먼저 출력된다.
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print(data_queue.qsize()) # 3
print(data_queue.get()) # (5,1)
print(data_queue.get()) # (10, 'korea')
print(data_queue.get()) # (15, 'china')

# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기 
queue_list = list()

def enqueue(data):
    queue_list.append(data)
    
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list)) # 10
print(dequeue()) # 0