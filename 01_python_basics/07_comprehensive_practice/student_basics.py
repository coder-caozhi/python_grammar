"""学生成绩管理：适合从上到下跟敲的 Python 基础练习。

数据只保存在内存中，退出程序后不会保存。运行方法见 README.md。
"""

def read_score():
    while True:
        text = input("please input grade (0-100): ").strip()
        try:
            score = float(text)
        except ValueError:
            print("the grade must be number, please input again")
            continue

        if 0 <= score <= 100:
            return score
        print("the grade must be between 0 and 100, please input again")


def score_level(score):
    if score >= 90:
        return "great"
    elif score >= 60:
        return "passed"
    else:
        return "failed"


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print(f"nama: {self.name}, grade: {self.score}, tier: {score_level(self.score)}")


def add_student(students):
    name = input("please input name:").strip()
    # 空字符串在条件判断中为假：not 表示取反
    if  not name:
        print("name can't be empty")
        return

    score = read_score()
    student = Student(name, score)
    students.append(student)
    print("add successfully")


def show_students(students):
    if not students:
        print("no student record")
        return

    print("\n --- student grade")
    for number, student in enumerate(students, start=1):
        print(f"{number}.", end="")
        student.show()


def show_average(students):
    if not students:
        print("还没有学生记录, 无法计算平均分")
        return

    total = 0.0
    for student in students:
        total += student.score

    average = total / len(students)

    print(f"{len((students))}人，{average: .2f}")


def find_student(students):
    name = input("please input the name you want to find")
    found = False
    for student in students:
        if student.name == name:
            student.show()
            found = True

    if not found:
        print("there is no student")



def main():
    # [] 创建空列表；它可以保存多个学生对象。
    students = []
    while True:
        print("\n===== 学生成绩管理 ======")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 计算平均分")
        print("4. 按姓名查找")
        print("0. 退出")
        choice = input("please input a choice").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_average(students)
        elif choice == "4":
            find_student(students)
        elif choice == "0":
            print("already exit")
            break
        else:
            print("there is no this options")

PI = 3.14

print(f"{__name__}")

if __name__ == "__main__":
    main()