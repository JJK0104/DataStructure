'''
이전에 작성한 코드를 보면 해쉬 테이블을 8개의 슬롯을 가진 공간으로 정의했다 
그런데 저장할 data가 4개 이상(50%) 이상이면 충돌이 발생할 가능성이 높아지기 때문에 
이럴 경우에는 해쉬테이블의 슬롯을 2배로 늘려주는 것이 일반적이다.

빈번한 충돌을 개선하는 기법
- 해쉬 함수을 재정의 및 해쉬 테이블 저장공간을 확대
- 예:

hash_table = list([None for i in range(16)]) # 16개의 슬롯으로 늘려주기 

def hash_function(key):
    return key % 16
'''

'''
참고: 해쉬 함수와 키 생성 함수
- 파이썬의 hash() 함수는 실행할 때마다, 값이 달라질 수 있음
- 유명한 해쉬 함수들이 있음: SHA(Secure Hash Algorithm, 안전한 해시 알고리즘)
  - 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능
'''

# SHA-1
# 별도 라이브러리 설치 pip install hashlib
import hashlib

# encoding 한다는 것은 바이트로 바꿔 주는 거
data = 'test'.encode() # b'test'
print('\'test\'.encode():',data)
hash_object = hashlib.sha1() # 해쉬 함수 만들기
hash_object.update(data) # hash값(해쉬 주소)이 object에 들어간다
hex_dig = hash_object.hexdigest() # 16진수 '문자열'로 추출
print(type(hex_dig)) # <class 'str'>
# 'test'라는 값에 sha1이라는 해쉬 함수를 통해서 나온 해쉬 값(해쉬 주소)
# 이 해쉬 값(해쉬 주소)은 문자열(data)가 똑같을 경우에는 항상 동일한 hash 값이 나오고 
# 문자열이 한글자든 10만 글자든 이 사이즈로 나온다
print ('hex_dig:',hex_dig) # a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

# SHA-256
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print (hex_dig)

# 연습4: 연습2의 Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수를 sha256 해쉬 알고리즘을 사용하도록 변경해보기 
# 1. 해쉬 키 생성: hash(data)
# 2. 해쉬 함수: key % 8 
import hashlib

hash_table = list([0 for i in range(8)])

def get_key(data):
        hash_object = hashlib.sha256()
        hash_object.update(data.encode())
        hex_dig = hash_object.hexdigest() # hex_dig은 문자열
        return int(hex_dig, 16) # 정수로 바꿔주기

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

print (get_key('db') % 8) # 1
print (get_key('da') % 8) # 2
print (get_key('dh') % 8) # 2

save_data('da', '01200123123')
save_data('dh', '3333333333')
print(read_data('dh'))

