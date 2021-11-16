### LIST
my_list = [20,30,40]
my_list2 = list()

# list 언패킹
n1,n2,n3 = my_list
print(n1,n2,n3)

# list 삽입
my_list.append(10) # 한개씩 삽입
print(my_list)

my_list.extend([50,60]) # 맨끝에 리스트에 새로운 여러개 (리스트) 추가
print(my_list)

my_list.insert(0,10) #0번째에 10삽입
print(my_list)

my_list[2] = 100 # 인덱스를 줘서 원하는 자리에 삽입
print(my_list)

# set 중복제거 / 순서 유지 안됨 / list형에서 set형으로 변경됨
my_set = set(my_list)
print(type(my_set), my_set)


###TUPLE
# tuple은 read only list!!!! 한번 값이 세팅되면 변경 안됨이 중요
my_tuple = (10,20,30)
my_tuple2 = tuple()
print(type(my_tuple), my_tuple)

# 튜플 삽입
#my_tuple[0] = 50
#print(my_tuple) # 튜플은 한번 값 세팅하면 변경할 수 없음!!!!!

num1 = (3) # int
num2 = (3,) # tuple ,때문에 튜플로 정의됨
print(type(num1), type(num2))

def swap(a,b):
    return (b,a)

a,b = swap(a,b)
print(a,b)


