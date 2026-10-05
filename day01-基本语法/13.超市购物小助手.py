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
    name = input("请输入商品名称（输入q结算）：").strip
    if name == 'q' or name == 'Q':
        break
    if name is None:
        print("请输入商品名称：")
        continue
    price = input("please input good's price:").strip
    if price is None:
        print("请输入商品价格：")
    try:
        int(price)
    except ValueError:
        print("输入价格非数字。retry")
        continue
    if price < 0:
        print("商品价格不能 < 0")
        continue
    items.append(name, price)


# ---------------------------------------------------------------
# 二、打印购物清单
# ---------------------------------------------------------------
# 提示：print("------ 购物清单 ------")
#   用 for i, item in enumerate(items, start=1) 逐行打印
#   格式：f"{i}. {item_name}    {item_price:.2f} 元"
#   最后打印：f"共 {len(items)} 件商品"
for i, item in enumerate(items, start = 1):
    print(f"{i}.{item[0]}.{item[1]: .2f}元")
else:
    print(f"共{len(len(items))}件商品")


# ---------------------------------------------------------------
# 三、计算总价（原价）
# ---------------------------------------------------------------
# 提示：original_total = sum(item[1] for item in items)
#       print(f"原价：{original_total:.2f} 元")

original_total = sum(item[1] for item in items)
print(f"原价:{original_total: .2f元}")
# ---------------------------------------------------------------
# 四、根据金额打折（if / elif / else）
# ---------------------------------------------------------------
# 提示：
#   if original_total >= 200:   discount_rate = 0.8  → "已享受 8 折优惠"
#   elif original_total >= 100: discount_rate = 0.9  → "已享受 9 折优惠"
#   else:                       discount_rate = 1.0  → 无折扣
#   有折扣时打印折扣说明
if original_total >=200:
    discount_rate = 0.8
elif original_total >= 100:
    discount_rate = 0.9
else:
    discount_rate = 1.0
print(f"the final price is {original_total * discount_rate} yuan")

# ---------------------------------------------------------------
# 五、打印最终金额
# ---------------------------------------------------------------
# 提示：final_total = original_total * discount_rate
#       print(f"应付金额：{final_total:.2f} 元")
#       print("感谢光临，欢迎下次再来！")
final_total = original_total * discount_rate
print(f"the final price is {final_total: .2f} yuan")
print("感谢光临，欢迎下次再来")

# ---------------------------------------------------------------
# 可选挑战
# ---------------------------------------------------------------
# 挑战 1：记录并打印最贵商品（用变量记录当前最大价格）
# 挑战 3：一件商品都没买时，提示"您还没有选购任何商品"

max_item_price = 0.0
for i in items:
    if max_item_price < items[i][1]:
        max_item_price = item[i][1]
