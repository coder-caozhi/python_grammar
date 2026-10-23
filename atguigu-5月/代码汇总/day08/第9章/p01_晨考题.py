"""
创建一个TodoList类，表示家庭任务清单，包含以下内容：

- 类属性：total_tasks（所有待办事项的总数，初始值为0）、total_complete_tasks（所有已完成任务总数）
- 实例属性：owner（拥有者）、task_type（类别，例如“生活”，“工作”），
    tasks（任务列表，每个任务是一个字典：{"task": "任务名", "completed": False}）、
created_time（创建时间，提示datetime.datetime.now()可以获取当前时间）
在__init__方法中：

- 初始化实例属性
- 任务列表为空
"""
import datetime

class ToDoList:
    total_tasks = 0
    total_complete_tasks = 0

    def __init__(self, owner, task_type):
        self.owner = owner
        self.task_type = task_type
        self.tasks = []
        self.created_time = datetime.datetime.now()
    """
    定义实例方法：
    - add_task(self,task_name)：添加新任务（更新tasks列表，并更新total_tasks+=1）
    - complete_task(self,task_name)：将指定任务标记为已完成（并更新total_complete_tasks+=1）
    - show_tasks(self,show_all=True)：显示单个任务清单中所有任务（如果show_all=False，只显示未完成的任务）
    - delete_task(self,task_name)：删除指定任务（更新tasks列表，并更新total_tasks-=1等）
    - get_progress(self)：计算并返回单个任务清单中完成任务的百分比
    """
    def add_task(self,task_name):
        #如果希望单个任务清单中的任务名称不重复，可以加如下的代码
        # for task in self.tasks:
        #     if task["task"] == task_name:
        #         return
        task = {"task": task_name, "completed": False}
        self.tasks.append(task)
        ToDoList.total_tasks += 1

    def complete_task(self,task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["completed"] = True
                ToDoList.total_complete_tasks += 1
                # break #如果任务清单中的任务名称不会重复，就可以break
    def show_tasks(self,show_all=True):
        if show_all:
            # print("当前任务清单中的所有任务：", self.tasks)
            print(f"{self.owner}当前任务清单中的所有任务：", {task["task"]:"已完成" if task["completed"] else "未完成" for task in self.tasks})
        else:
            # print("当前任务清单中所有未完成任务：",[task for task in self.tasks if not task["completed"]])
            print(f"{self.owner}当前任务清单中所有未完成任务：",{task["task"]:"未完成" for task in self.tasks if not task["completed"]})
    def delete_task(self,task_name):
        i = 0
        while i<len(self.tasks):
            if self.tasks[i]["task"] == task_name:
                ToDoList.total_tasks -= 1
                if self.tasks[i]['completed']:
                    ToDoList.total_complete_tasks -=1
                del self.tasks[i]
            else:
                i+=1
    def get_progress(self):
        completed_count = 0
        for task in self.tasks:
            if task["completed"]:
                completed_count += 1
        return f"{completed_count / len(self.tasks):.2%}"

    """
    定义类方法：
   - get_total_tasks(cls)：获取家庭所有待办事项的总数
   - get_total_progress(cls)：获取家庭所有任务完成百分比
    """
    @classmethod
    def get_total_tasks(cls):
        return cls.total_tasks
    @classmethod
    def get_total_progress(cls):
        return f"{cls.total_complete_tasks / cls.total_tasks:.2%}"

    """
    定义静态方法：
     is_valid_task(task_name)：验证任务名称是否有效（长度1-50字符）
    """
    @staticmethod
    def is_valid_task(task_name):
        return 1<=len(task_name.strip())<=50

"""
创建2个待办事项列表（不同拥有者），并进行以下操作：
- 分别添加几个个任务
- 完成部分任务
- 显示所有任务和只显示未完成任务
- 查看任务完成进度
- 删除一个任务
- 使用静态方法验证1个任务名称
"""
# t1 = ToDoList("爸爸","工作")
# t1.add_task("写代码")
# t1.add_task("开会")
# t1.show_tasks()
#
# t2 = ToDoList("妈妈","家务")
# t2.add_task("洗衣服")
# t2.add_task("拖地")
# t2.show_tasks()
#
# t2.complete_task("洗衣服")
# t2.show_tasks()
# t2.show_tasks(show_all=False)
# print("t2任务清单的完成百分比：",t2.get_progress())
#
# print("家庭任务完成百分比：", ToDoList.get_total_progress())
#
# t2.delete_task("洗衣服")
# t1.delete_task("开会")
# t1.show_tasks()
# t2.show_tasks()
#
# print(ToDoList.is_valid_task("看电视"))

"""
动态操作练习：
- 为某个TodoList对象动态添加一个priority属性（优先级）
- 动态添加一个实例方法sort_by_name()，按任务名称排序
- 动态增加类属性category
- 尝试动态删除某个对象的show_tasks方法，观察调用时的错误
"""
def sort_by_name(self):
    self.tasks.sort(key=lambda task: task["task"])

ToDoList.sort_by_name = sort_by_name
t3 = ToDoList("儿子","学习")
t3.add_task("Chinese")
t3.add_task("Math")
t3.add_task("English")
t3.show_tasks()
t3.sort_by_name()
t3.show_tasks()

t3.priority = 10
ToDoList.category = "尚硅谷"
# del t3.show_tasks #错误。单独删除某个对象的实例方法，只适用于   对象.实例方法 = types.MethodType(函数, 对象)这种方式动态添加的实例方法