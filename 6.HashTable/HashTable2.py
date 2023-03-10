'''
4. 자료 구조 해쉬 테이블의 장단점과 주요 용도
- 장점
  - 데이터 저장/읽기 속도가 빠르다. (검색 속도가 빠르다.)
  - 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
- 단점 
  - 일반적으로 저장공간이 좀더 많이 필요하다.
  - 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
- 주요 용도
  - 검색이 많이 필요한 경우
  - 저장, 삭제, 읽기가 빈번한 경우
  - 캐쉬 구현시 (중복 확인이 쉽기 때문)
'''

# 연습1: 리스트 변수를 활용해서 해쉬 테이블 구현해보기 
# 1. 해쉬 키 생성: hash(data)
# 2. 해쉬 함수: key % 8 

# 내장함수 hash(), 실행할 때마다 결과가 달라져 잘 안쓰긴 함
print(hash('Dave'))

hash_table = list([0 for i in range(8)]) # list comprehension 문법

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
    
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '0102030200')
print(save_data('Andy', '01033232200'))
print(read_data('Dave'))

print(hash_table)