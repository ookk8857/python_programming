"""
yesterday count

file open mode
r : read
w : write (텍스트 파일은 r은 기본이라 생략 가능)
rb : read binary
wb : write binary
a : append

"""

def file_read(file_name):
    with open(file_name, "r" ,encoding="utf-8") as file :
        lyric = file.read()
        #print(lyric)
        return (lyric)


read = file_read("yesterday.txt")
print(read)
n_of_YESTERDAY =  read.upper().count("YESTERDAY")
print(f'Number of a word YESTERDAY ==> {n_of_YESTERDAY}')

n_of_Yesterday = read.count("Yesterday")
print(f'Number of a word Yesterday ==> {n_of_Yesterday}')

n_of_yesterday = read.lower().count("yesterday")
print(f'Number of a word yesterday ==> {n_of_yesterday}')
