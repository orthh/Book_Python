# 딕셔너리자료형 : key, value쌍, 연관 배열(Associative array) 또는 해시(Hash)라고 한다.
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic = {"name": "pey", "phone": "010-9999-1234", "birth": "1118"}


# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a) # {1: 'a', 2: 'b'}
a['name'] = 'pey'
print(a) # {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]
print(a) # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제하기
del a["name"]
print(a) # {1: 'a', 2: 'b', 3: [1, 2, 3]}

grade = {''}

# 딕셔너리 사용
grade = {"pey" : 10, "julliet" : 99}
print(grade["pey"])

# 딕서너리 에서 key는 고유한 값이므로 중복되는 key값은 하나를 제외한 
#   나머지는 무시된다(뒤에것이 나오네)
# key에 리스트 불가, value에는 리스트 가능
a = {1:'a', 1: 'b'}
print(a)

# 딕셔너리 관련 함수들
# key리스트 만들기 : a.keys()
# 리스트 고유 함수 수행x
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(a.keys) # dick_keys 객체 리턴
for k in a.keys() : print(k)

# Value 리스트 만들기 : values
for k in a.values() : print(k)

# key, value 쌍 얻기 : items
for item in a.items() :
  print(item) # 튜플로 묶은 값 dict_items 객체로 리턴
  
# key, value 쌍 모두 지우기 : clear
a.clear()
print(a)

# key로 value 얻기 : get(key), get(key, default)
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.get("name"))

print(a.get('nokey', 'foo'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기 : in
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print("name" in a) # True
print("email" in a) # False