'''
1. 정렬 (sorting) 이란?
- 정렬 (sorting): 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
- 정렬은 프로그램 작성시 빈번하게 필요로 함

2. 버블 정렬 (bubble sort) 란?
* 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

#### 직접 눈으로 보면 더 이해가 쉽다: https://visualgo.net/en/sorting

3. 간단한 경우 부터 생각해보자

데이터 길이  |  조건체크  |  턴
2               1       1
3               2       2
4               3       3

for index in range(데이터킬이 -1): # 턴
    for index2 in range(데이터길이 - index -1): # 한턴 한턴 지날수록 마지막에 가까운 숫자들은 가장 큰 숫자들이 됨
        if 앞데이터 > 뒤데이터 : 
            swap(앞데이터, 뒤데이터)

4. 알고리즘 구현
* **특이점 찾아보기**
  - n개의 리스트가 있는 경우 최대 n-1번의 로직을 적용한다.
  - 로직을 1번 적용할 때마다 가장 큰 숫자가 뒤에서부터 1개씩 결정된다.
  - 로직이 경우에 따라 일찍 끝날 수도 있다. 
    따라서 로직을 적용할 때 한 번도 데이터가 교환된 적이 없다면 이미 정렬된 상태이므로 더 이상 로직을 반복 적용할 필요가 없다.

  리스트 데이터  |  1회 로직 적용  | 2회 로직 적용  | 3회 로직 적용  | 4회 로직 적용
  9,1,7          1,7,9             -
  9,7,1          7,1,9          1,7,9             -
  1,9,3,2        1,3,2,9        1,2,3,9           -
  9,3,2,1        3,2,1,9        2,1,3,9         1,2,3,9         -
  9,7,5,3,1      7,5,3,1,9      5,3,1,7,9       3,1,5,7,9     1,3,5,7,9
  5,7,3,9,4      5,3,7,4,9      3,5,4,7,9       3,4,5,7,9       -
  1,9,3,2,7      1,3,2,7,9      1,2,3,7,9         -

  1) for num in range(len(data_list)) 반복
  2) swap = 0 (교환이 되었는지를 확인하는 변수를 두자)
  3) 반복문 안에서, for index in range(len(data_list) - num - 1) n - 1번 반복해야 하므로
  4) 반복문안의 반복문 안에서, if data_list[index] > data_list[index + 1] 이면
  5) data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
  6) swap += 1 
  7) 반복문 안에서, if swap == 0 이면, break 끝

'''