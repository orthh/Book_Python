# 4가지 타입
print("Hello World")

print('Python is fun')

print("""Life is too short, You need python""")

print('''Life is too short, You need python''')

food = "Python's favorite food is perl"
print(food)

say = '"Python is ver easy." he says.'
print(say)

say2 = "\"Python is very easy. \" he says."
print(say2)

multiline = "Life is too short\nYou need python"
print(multiline)

mulitline2 = """
  Life is too short
  You need python
"""
print(mulitline2)

mulitline4 = """Life is too short
You need python"""
print(mulitline4)

mulitline3 = '''
  Life is too short
  You need python
'''

print(mulitline3)

a = "python";
print(a*2) #pythonpython

print("=" * 50);
print("My Program");
print("=" * 50);

print(len(a)) #6

b = "Life is too short, You need Python"

print(b[3]); #e

for item in b :
  print(item)
  
#슬라이싱
print(b[0:3]); #Lif => 0부터 3미만까지(끝번호 포함하지 않음)
#즉 3-0 (뺀값 3 글자 출력)

print(b[3:]) #끝번호 생략 : 3번인덱스부터 끝까지
print(b[:5]) #처음부터 5번 미만까지 출력

print(b[:]) #처음부터 끝까지

mix = "20010301Rainy"
year = mix[:4]
day = mix[4:8]
weather = mix[8:]

print(year)
print(day)
print(weather)

# mix[2] = 'A' 에러 -> 불가능


# 문자열 포매팅
print("I eat %d apples." % 3)
print("I eat %s apples" % "five")

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day))

#  %s 는 자동으로 %뒤에 있는 값을 문자열로 바꾼다.
print("I have %s apples" %3.33333223)

print("error is %d%%" % 98)

# format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples".format(number))
print("I ate {0} apples. so I was sick for {1} days".format(number, day))
print("I ate {number} apples. so I was sick for {day} days".format(number=2, day=4))

print("I ate {number} and {day}") # 불가

print("{0:>10}".format("hi"))
print("{0:<10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"));

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y));

# f문자열 포매팅
name = "홍길동"
age = 30
test = f"나의 이름은 {name} 입니다. 나이는 {age + 1}입니다."
print(test);

# 문자열 관련 함수들
# 문자개수 세기
a = "hobby";
print(a.count('b'));

# 위치 알려주기1(find)
a = "Python is the best choice"
print(a.find("b"))
print(a.find("k"))