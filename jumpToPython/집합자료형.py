s1 = set([1, 2, 3])
print(s1)

# 집합 자료형의 특징
#  - 중복을 허용하지 않는다
#  - 순서가 없다.

# set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환후 해야한다.

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 1. 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 2. 합집합
print(s1 | s2)
print(s1.union(s2))

# 3. 차집합
print(s1 - s2)
print(s1.difference(s2))

# 집합자료형 관련 함수들
# 값 1개 추가하기(add)
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가하기 : update
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)