'''
배열(Array)
* 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
* 파이썬에서는 리스트 타입이 배열 기능을 제공함

1. 배열은 왜 필요할까?
- 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
- 같은 종류의 데이터를 순차적으로 저장
- 장점: 
  - 빠른 접근 가능
    - 첫 데이터의 위치에서 상대적인 위치로 데이터 접근(인덱스 번호로 접근)
- 단점: 
  - 데이터 추가/삭제의 어려움
    - 미리 최대 길이를 지정해야 함
'''


'''
* range(start, stop): 이상 ~ 미만
* range(stop): range(0,stop)
* range(start, stop, step): range(0, 20, 2)은 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
  - start, stop, step은 음수로 지정 가능
'''

# 아래의 dataset 리스트에서 전체 이름 안에 M은 몇번 나왔는지 빈도수 출력하기
dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1
print (m_count)