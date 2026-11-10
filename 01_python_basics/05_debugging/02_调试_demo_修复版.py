# =====================================================================
# 02. 调试练习 Demo —— 修复版（参考答案）
# ---------------------------------------------------------------------
# 这个文件是 01.调试demo.py 的修复版。
# 建议先自己调完 5 个阶段，再来看这里的改法。
#
# 每个修复点都用“修复 N”标出来了，可以和原文件对比着看。
# =====================================================================

import sys
import traceback

# 7 名学生，每人 3 门课的成绩
STUDENTS = [
    {"name": "张三", "class_name": "一班", "scores": [88, 92, 79]},
    {"name": "李四", "class_name": "二班", "scores": [95, 67, 84]},
    {"name": "王五", "class_name": "一班", "scores": [72, 90, 85]},
    {"name": "赵六", "class_name": "二班", "scores": [60, 78, 91]},
    {"name": "钱七", "class_name": "三班", "scores": [99, 88, 94]},
    {"name": "孙八", "class_name": "三班", "scores": [50, 55, 58]},
    {"name": "周九", "class_name": "一班", "scores": [45, 62, 51]},
]


# ---------------------------------------------------------------------
# 阶段 1：计算全班平均分
# 修复 1：count 要累加“分数的个数”，而不是“学生的个数”
# ---------------------------------------------------------------------
def stage1_average(students):
    print("开始计算全班平均分 ...")

    total = 0
    count = 0
    for student in students:
        total += sum(student["scores"])
        count += len(student["scores"])     # 修复 1

    average = total / count
    print(f"总分: {total}，参与计算的分数个数: {count}")
    print(f"全班平均分: {average:.2f}")
    return average


# ---------------------------------------------------------------------
# 阶段 2：找总分最高的学生
# 修复 2：range 的结束值不包含，len(students) 已经越界了
# ---------------------------------------------------------------------
def stage2_top_student(students):
    print("开始查找总分最高的学生 ...")

    top = students[0]
    for i in range(1, len(students)):       # 修复 2
        current = students[i]
        if sum(current["scores"]) > sum(top["scores"]):
            top = current

    print(f"总分最高: {top['name']}，总分: {sum(top['scores'])}")
    return top


# ---------------------------------------------------------------------
# 阶段 3：按班级分组
# 修复 3：不要用可变对象（{} / []）当默认参数
#         默认参数只在函数定义时创建一次，会被所有调用共享
# ---------------------------------------------------------------------
def stage3_group_by_class(students, groups=None):   # 修复 3
    if groups is None:
        groups = {}

    for student in students:
        class_name = student["class_name"]
        groups.setdefault(class_name, []).append(student["name"])
    return groups


def run_stage3():
    print("第一次：传入全部学生")
    first = stage3_group_by_class(STUDENTS)
    print(f"分组结果: {first}")

    print("\n第二次：只传入二班学生")
    second_batch = [s for s in STUDENTS if s["class_name"] == "二班"]
    second = stage3_group_by_class(second_batch)
    print(f"分组结果: {second}")


# ---------------------------------------------------------------------
# 阶段 4：二分查找（递归）
# 修复 4：往右找时左边界要跳过 mid，否则区间不会缩小，递归永远出不来
# ---------------------------------------------------------------------
SORTED_SCORES = sorted(score for student in STUDENTS for score in student["scores"])


def binary_search(scores, target, left=0, right=None):
    if right is None:
        right = len(scores) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if scores[mid] == target:
        return mid
    if scores[mid] < target:
        return binary_search(scores, target, mid + 1, right)   # 修复 4
    return binary_search(scores, target, left, mid - 1)


def run_stage4():
    print(f"有序分数: {SORTED_SCORES}")

    target = 92
    index = binary_search(SORTED_SCORES, target)
    print(f"查找 {target}: 下标 {index}，值 {SORTED_SCORES[index]}")

    print("\n再查找一个不存在的分数 100 ...")
    index = binary_search(SORTED_SCORES, 100)
    print(f"查找 100: 下标 {index}")


# ---------------------------------------------------------------------
# 阶段 5：剔除不及格的学生
# 修复 5：删除元素后，后面的元素会整体前移一位，
#         此时不能再 i += 1，否则会跳过一个元素
# ---------------------------------------------------------------------
def stage5_remove_failed(students, pass_line=60):
    print(f"开始剔除平均分低于 {pass_line} 的学生 ...")

    i = 0
    while i < len(students):
        student = students[i]
        average = sum(student["scores"]) / len(student["scores"])
        if average < pass_line:
            print(f"  剔除 {student['name']}（平均分 {average:.2f}）")
            students.pop(i)
        else:
            i += 1                      # 修复 5：只有没删除时才往后走

    return students


def run_stage5():
    # 传副本，避免影响后面的阶段（字典本身不会被修改）
    remaining = stage5_remove_failed(STUDENTS.copy())
    names = [student["name"] for student in remaining]
    print(f"剩余 {len(remaining)} 人: {names}")


# ---------------------------------------------------------------------
# 运行入口
# ---------------------------------------------------------------------
STAGES = {
    "1": ("阶段 1：计算平均分", lambda: stage1_average(STUDENTS)),
    "2": ("阶段 2：找总分最高的学生", lambda: stage2_top_student(STUDENTS)),
    "3": ("阶段 3：按班级分组", run_stage3),
    "4": ("阶段 4：二分查找（递归）", run_stage4),
    "5": ("阶段 5：剔除不及格学生", run_stage5),
}


def main():
    choice = sys.argv[1] if len(sys.argv) > 1 else "all"
    if choice != "all" and choice not in STAGES:
        print("用法: python 02.调试demo-修复版.py [all|1|2|3|4|5]")
        return

    failed = []
    for key, (title, run) in STAGES.items():
        if choice not in ("all", key):
            continue

        print("\n" + "=" * 60)
        print(title)
        print("=" * 60)

        try:
            run()
        except Exception as exc:
            failed.append(key)
            print(f"\n[阶段 {key} 抛出异常] {type(exc).__name__}: {exc}")
            traceback.print_exc(limit=6)

    if choice == "all":
        print("\n" + "=" * 60)
        if failed:
            print(f"运行结束，阶段 {', '.join(failed)} 抛出了异常。")
        else:
            print("运行结束，所有阶段都正常执行。")
        print("=" * 60)


if __name__ == "__main__":
    main()
