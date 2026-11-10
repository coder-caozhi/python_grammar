"""学生成绩管理：适合从上到下跟敲的 Python 基础练习。

数据只保存在内存中，退出程序后不会保存。运行方法见 README.md。
"""

# class 定义类：把一个学生的数据和相关功能放在一起。
class Student:
    # __init__ 在创建对象时调用；self 表示当前对象。
    def __init__(self, name, score):
        # = 给变量或对象属性赋值；点号用于访问对象的属性。
        self.name = name
        self.score = score

    # def 定义函数；写在类中的函数叫方法。
    def show(self):
        # f 字符串中的 {表达式} 会被计算并放进字符串。
        print(f"姓名：{self.name}，成绩：{self.score}，等级：{score_level(self.score)}")


# 函数可以接收参数，return 用来返回结果。
def score_level(score):
    # if / elif / else 按顺序判断条件，只执行第一个成立的分支。
    # >= 表示大于或等于，冒号后的缩进代码属于对应分支。
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def read_score():
    # while True 会持续循环，直到遇到 return 或 break。
    while True:
        # input 获取用户输入，结果是字符串；strip 去掉首尾空白。
        text = input("请输入成绩（0 到 100）：").strip()
        # try / except 处理可能发生的错误，避免输入字母时程序退出。
        try:
            # float 将字符串转换为小数，例如 "85.5" 转成 85.5。
            score = float(text)
        except ValueError:
            print("成绩必须是数字，请重新输入。")
            # continue 结束本次循环，开始下一次循环。
            continue

        # 连续比较相当于 score >= 0 and score <= 100。
        if 0 <= score <= 100:
            return score
        print("成绩必须在 0 到 100 之间，请重新输入。")


def add_student(students):
    name = input("请输入姓名：").strip()
    # 空字符串在条件判断中为假；not 表示取反。
    if not name:
        print("姓名不能为空。")
        return

    score = read_score()
    # Student(...) 创建对象；列表的 append 方法把对象添加到末尾。
    student = Student(name, score)
    students.append(student)
    print("添加成功。")


def show_students(students):
    # 列表为空时，not students 为真。
    if not students:
        print("还没有学生记录。")
        return

    print("\n--- 学生成绩 ---")
    # for ... in ... 依次遍历列表；enumerate 从 1 开始生成序号。
    for number, student in enumerate(students, start=1):
        print(f"{number}. ", end="")
        student.show()


def show_average(students):
    if not students:
        print("还没有学生记录，无法计算平均分。")
        return

    total = 0.0
    for student in students:
        # += 是累加赋值，相当于 total = total + student.score。
        total += student.score
    # len 返回列表长度；/ 表示除法。
    average = total / len(students)
    # :.2f 表示小数保留两位显示。
    print(f"共 {len(students)} 人，平均分：{average:.2f}")


def find_student(students):
    name = input("请输入要查找的姓名：").strip()
    found = False
    for student in students:
        # == 比较两个值是否相等；可能有多个同名学生，逐个显示。
        if student.name == name:
            student.show()
            found = True
    if not found:
        print("没有找到该学生。")


def main():
    # [] 创建空列表；它可以保存多个学生对象。
    students = []
    while True:
        print("\n===== 学生成绩管理 =====")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 计算平均分")
        print("4. 按姓名查找")
        print("0. 退出")
        choice = input("请选择：").strip()

        # input 返回字符串，所以这里与字符串 "1"、"2" 等比较。
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_average(students)
        elif choice == "4":
            find_student(students)
        elif choice == "0":
            print("程序已退出。")
            # break 结束最近的一层循环。
            break
        else:
            print("没有这个选项，请重新输入。")


# 直接运行文件时执行 main；被其他文件导入时不会自动进入菜单。
if __name__ == "__main__":
    main()
