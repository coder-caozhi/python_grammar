# =====================================================================
# 13. 超市购物结算小助手（练习骨架：只保留注释，自己补代码）
# ---------------------------------------------------------------------
# 需求：
#   1. 打印欢迎语（分隔线用 "=" * 50）
#   2. 循环录入商品名 + 价格，输入 q / Q 结束（break）
#   3. 价格不是数字 → 提示"价格输入有误，请重新输入" 并 continue
#   4. 打印购物清单：1. 苹果    5.50 元 ...，最后打印"共 N 件商品"
#   5. 计算总价（原价）
#   6. 打折：>=200 打 8 折；>=100 打 9 折；<100 不打折
#   7. 打印应付金额、结束语
# =====================================================================


# ---------------------------------------------------------------------
# 欢迎语
# ---------------------------------------------------------------------
# 提示：print("=" * 50) → 欢迎语 → print("=" * 50)
print("=" * 50)
print("欢迎使用超市助手")
print("=" * 50)



# ---------------------------------------------------------------------
# 准备容器
# ---------------------------------------------------------------------
# items 里每个元素是 [商品名, 价格]，例如 ["苹果", 5.5]
# 提示：items = []
items = []

# ---------------------------------------------------------------
# 一、循环录入商品
# ---------------------------------------------------------------
# 提示：while True:
#   1) 读商品名：name = input("请输入商品名称（输入 q 结算）：").strip()
#      - 输入 q / Q 结束录入 → break
#      - 名称为空 → 提示后 continue
#   2) 读价格：price_str = input("请输入商品价格：").strip()
#      - try / except ValueError 判断是不是数字，不是则提示后 continue
#      - 价格为负数 → 提示后 continue
#   3) 录入成功 → items.append([name, price])
while True:
    # 修正1：.strip 要加括号，否则拿到的是"方法对象"而不是字符串
    name = input("请输入商品名称（输入q结算）：").strip()
    if name == 'q' or name == 'Q':
        break
    # 修正2：input 不会返回 None，没输入时是空字符串 ""
    if name == "":
        print("请输入商品名称：")
        continue
    price_str = input("请输入商品价格：").strip()
    if price_str == "":
        print("请输入商品价格：")
        continue
    # 修正3：用 float 而不是 int（价格可能是小数），并且要把结果存回 price
    #        实测 int('5.5') 会报 ValueError
    try:
        price = float(price_str)
    except ValueError:
        print("输入价格非数字。retry")
        continue
    # 修正4：price 现在是数字，才能和 0 比较（字符串 < 数字会报 TypeError）
    if price < 0:
        print("商品价格不能 < 0")
        continue
    # 修正5：append 只接收 1 个参数，要用列表包起来
    items.append([name, price])


# ---------------------------------------------------------------
# 二、打印购物清单
# ---------------------------------------------------------------
# 提示：print("------ 购物清单 ------")
#   用 for i, item in enumerate(items, start=1) 逐行打印
#   格式：f"{i}. {item_name}    {item_price:.2f} 元"
#   最后打印：f"共 {len(items)} 件商品"
print("------ 购物清单 ------")
for i, item in enumerate(items, start=1):
    # 修正6：用点号分隔不符合需求，改成 "序号. 名称    价格 元"
    #        另注意 ": .2f" 有个空格会多留符号位，去掉空格用 ":.2f"
    print(f"{i}. {item[0]}    {item[1]:.2f} 元")
# 修正7：for-else 的 else 表示"循环没被 break 才执行"，语义不对
#        直接放在循环外面才对；且 len(items) 不要再套一层 len
print(f"共 {len(items)} 件商品")


# ---------------------------------------------------------------
# 三、计算总价（原价）
# ---------------------------------------------------------------
# 提示：original_total = sum(item[1] for item in items)
#       print(f"原价：{original_total:.2f} 元")

original_total = sum(item[1] for item in items)
# 修正8：中文"元"要放在花括号外面，写在里面会报 Invalid format specifier
print(f"原价：{original_total:.2f} 元")
# ---------------------------------------------------------------
# 四、根据金额打折（if / elif / else）
# ---------------------------------------------------------------
# 提示：
#   if original_total >= 200:   discount_rate = 0.8  → "已享受 8 折优惠"
#   elif original_total >= 100: discount_rate = 0.9  → "已享受 9 折优惠"
#   else:                       discount_rate = 1.0  → 无折扣
#   有折扣时打印折扣说明
if original_total >= 200:
    discount_rate = 0.8
    discount_desc = "已享受 8 折优惠"
elif original_total >= 100:
    discount_rate = 0.9
    discount_desc = "已享受 9 折优惠"
else:
    discount_rate = 1.0
    discount_desc = ""
# 修正9：补上需求要求的"折扣说明"打印（无折扣时不打印说明）
if discount_desc != "":
    print(discount_desc)

# ---------------------------------------------------------------
# 五、打印最终金额
# ---------------------------------------------------------------
# 提示：final_total = original_total * discount_rate
#       print(f"应付金额：{final_total:.2f} 元")
#       print("感谢光临，欢迎下次再来！")
final_total = original_total * discount_rate
# 修正10：这里才是"应付金额"，删掉前面重复打印的 the final price
print(f"应付金额：{final_total:.2f} 元")
print("感谢光临，欢迎下次再来！")

# ---------------------------------------------------------------
# 可选挑战
# ---------------------------------------------------------------
# 挑战 1：记录并打印最贵商品（用变量记录当前最大价格）
# 挑战 3：一件商品都没买时，提示"您还没有选购任何商品"

max_item_name = None
max_item_price = 0.0
# 修正11：for i in items 时 i 就是商品本身（列表 [名称, 价格]），
#         不能用 items[i] 去索引；直接遍历 item 即可，注意拼写 items
for item in items:
    if item[1] > max_item_price:
        max_item_price = item[1]
        max_item_name = item[0]

if max_item_name is not None:
    print(f"最贵商品：{max_item_name}（{max_item_price:.2f} 元）")
else:
    print("您还没有选购任何商品")
