import pickle
import hashlib


def member_data():
    try:
        with open("member.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def check_password(userid, password):
    m = hashlib.sha256()
    m.update(password.encode("utf-8"))
    return m.hexdigest() == members[userid][1]


class member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print("회원명:{} \n회원닉네임:{}".format(self.name, self.username))


class post:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    # def write_display(self):
    #     return "제목:{},글쓴이:{}\n내용:{}".format(self.title,self.author,self.content)


members = member_data()
posts = []

while True:
    quit = input("환영합니다 글쓰실려면 아무키나 누르세요(종료는x)")
    if quit == "x":
        break
    memberone = input("id를 입력하시오!>")
    if memberone not in members:
        print("일치하는 id가 없습니다 회원가입을 하세요")
        newmember = member(
            input("이름을 입력해주세요>"), input("id를 입력해주세요>"), input("password를 입력해주세요>")
        )
        m = hashlib.sha256()
        m.update(newmember.password.encode("utf-8"))
        members[newmember.username] = []
        members[newmember.username].append(newmember.name)
        members[newmember.username].append(m.hexdigest())
        print("새로운 회원이 생겼다")
        print("만들어진 아이디로 로그인하세요!")
    else:
        if check_password(memberone, input("password를 입력하세요>")) == True:
            while True:
                quit = input("글쓰기를 종료하시려면 x를 눌러주세요 아니면 아무키나 누르세요")
                if quit != "x":
                    newpost = post(input("제목을 입력하세요>"), memberone, input("내용을 입력하세요>"))
                else:
                    break
        posts.append(newpost)

print("사용내역목록입니다")

print("회원이름 목록")
for i in members:
    print(members[i][0])

author = input("id를 입력하세요")
print("{}회원이 쓴 글 목록".format(author))
for poster in posts:
    if author == poster.author:
        print(poster.title)

word = input("단어를 입력하세요")
print("{}단어가 들어간 글 목록".format(word))
for poster in posts:
    if word in poster.content:
        print(poster.title)


with open("member.pkl", "wb") as f:
    pickle.dump(members, f)
