'''
충돌(Collision) 해결 알고리즘 (좋은 해쉬 함수 사용하기)
 해쉬 테이블의 가장 큰 문제는 충돌(Collision)의 경우입니다.
 이 문제를 충돌(Collision) 또는 해쉬 충돌(Hash Collision)이라고 부릅니다.
 한개 이상의 data가 동일한 hash address에 저장되는 경우 발생.

1. Chaining 기법
- 개방 해슁 또는 Open Hashing 기법 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
- 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법

2. Linear Probing 기법
- 폐쇄 해슁 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
- 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
  - 저장공간 활용도를 높이기 위한 기법
'''

# 연습2: 연습1의 해쉬 테이블 코드에 Chaining 기법으로 충돌해결 코드를 추가해보기
# 1. 해쉬 키 생성: hash(data)
# 2. 해쉬 함수: key % 8 

hash_table = list([0 for i in range(8)]) # list comprehension 문법
print(hash_table)

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # hash_table = [0, 0, 0, 0, 0, 0, 0, 0] 으로 만들어줬으니까
    # value가 0이 아니라고 가정하겠다
    # 그러면 hash_table[hash_address] != 0 은 거기에 data가 있다는 거다 
    if hash_table[hash_address] != 0:
        # linked list 대신 list 사용
        for index in range(len(hash_table[hash_address])): 
            if hash_table[hash_address][index][0] == index_key:
                # 이미 있는 index_key면 덮어쓰기
                hash_table[hash_address][index][1] = value
                return
        # 중복 index_key가 아니면 추가하기
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]
    
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 값이 저장되어 있다면
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        # 여기로 넘어왔다는 건 list는 있는데 해당하는 key값에 해당하는 value가 없었다는 거
        return None
    # 값이 없다면 
    else:
        return None

# hash() 값이 계속 바뀌고 %8 값이 같아야서 test 하기 좀 어렵다

print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)

save_data('Dd', '1201023010')
save_data('Data', '3301023010')
print(read_data('Dd'))

print(hash_table)
 