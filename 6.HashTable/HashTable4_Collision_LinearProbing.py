# 연습3: 연습1의 해쉬 테이블 코드에 Linear Probling 기법으로 충돌해결 코드를 추가해보기
# 1. 해쉬 키 생성: hash(data)
# 2. 해쉬 함수: key % 8 

hash_table = list([0 for i in range(8)])
print(hash_table) # [0, 0, 0, 0, 0, 0, 0, 0]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 0 이 아니라는 건 data가 있다는 거
    if hash_table[hash_address] != 0:
        # hash_address 부터 끝까지 반복. len(hash_table) == 8
        for index in range(hash_address, len(hash_table)):
            # 비어있는 슬롯 발견하면 저장
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            # index_key가 동일하면 값 update
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

print (hash('dk') % 8)
print (hash('da') % 8)
print (hash('dc') % 8)

save_data('dk', '01200123123')
save_data('da', '3333333333')
read_data('dc')