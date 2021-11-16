
# class 선언
class User:
    # 생성자 선언
    def __init__(self,name): # name 속성 받기
        self.name = name

    def __str__(self): # toString()처럼
        return self.name

# 객체 생성
user = User("파이썬")
print(user)

