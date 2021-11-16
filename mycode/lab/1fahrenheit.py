"""
섭씨 온도를 입력받아 화씨로 변환
"""

# 섭씨 > 화씨 변환 함수
def fah_convert(celsius):
    return((9/5)*float(celsius)+32)

print("변환하고 싶은 섭씨 온도를 입력해주"
      ""
      ""
      ""
      ""
      "세요")
user_input = input()
print(type(user_input),user_input) # str이여서 함수에서 float 변환
fah = fah_convert(user_input)
print('섭씨온도 : ', float(user_input))

print('화씨온도 : {0:.2f}'.format(fah)) # 소숫점 둘째자리

print(f'섭씨온도 : {user_input}') # 앞에 f를 붙이면 {}에 뿌리고 싶은 변수를 넣어도 됨
print(f'화씨온도 : {round(fah,2)}')
