# 리스트 슬라이싱
# 문자열과 마찬가지로 a[i:e]

# 리스트 연산하기
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a * 3)
print(len(a))

# a[2] + "hi" => 에러
# 정수와 문자열을 더하려 했기 떄문
print(str(a[2]) + "hi")

# del 함수 사용해 리스트 요소 삭제하기
a = [1,2,3]
del a[1]
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)

# 리스트 관련 함수들
a = [1,2,3]
a.append(4) #[1,2,3,4]
print(a)

a.append([5,6])
print(a) # [1, 2, 3, 4, [5, 6]]

# 리스트 정렬(sort)
a = [1,4,3,2]
a.sort()
print(a)

a = ['a','c','b']
a.sort()
print(a)

a = ['a','c','b']
a.reverse()
print(a)

# 리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4)
print(a) #[4,1,2,3]

# 리스트 요소 제거(remove) : 하나만 제거
a = [1,2,3,1,2,3]
a.remove(3) 
print(a) #[1,2,1,2,3]

# 리스트 요소 끄집어내기(pop)
a = [1,2,3]
a.pop()
print(a) #[1,2]
a.pop(1)
print(a) #[1]

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
print(a.count(1))

# 리스트 확장 : extend(x) => x에는 리스트만 올 수 있으며 원래의
#                           리스트에 x리스트를 더하게 된다.
a = [1,2,3]
a.extend([4,5])
print(a)
b = [6,7]
a.extend(b)
print(a)
a += [8,9]
print(a)