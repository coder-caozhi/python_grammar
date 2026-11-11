# ============================================================================
# 学习目的：观察模型选择工具、接收工具结果再继续决策
# 技术讲解：create_agent 驱动消息/工具执行循环；工具分别查询商品与库存
# 阅读路线：本地模拟数据 → 两个工具 → Agent → messages 输入 → 查看工具调用轨迹
# 当前代码要注意：商品价格与库存是示例数据；tool_calls 是可观察调用记录，不等于暴露模型内部完整思维过程
# 动手验证：检查 search_products 与 check_inventory 的调用顺序及参数来源
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

# 模拟产品数据库
PRODUCT_DATABASE = {
    "无线耳机": [
        {"id": "WH-1000XM5", "name": "索尼 WH-1000XM5", "popularity": 95, "price": 299},
        {"id": "QC45", "name": "Bose QuietComfort 45", "popularity": 88, "price": 329},
        {"id": "AIRMAX", "name": "苹果 AirPods Max", "popularity": 92, "price": 549},
        {"id": "PXC550", "name": "森海塞尔 PXC 550", "popularity": 76, "price": 299},
        {"id": "HT450", "name": "JBL Tune 760NC", "popularity": 82, "price": 99}
    ],
    "游戏鼠标": [
        {"id": "GPW", "name": "罗技 G Pro 无线", "popularity": 90, "price": 129},
        {"id": "VIPER", "name": "雷蛇 Viper V2 Pro", "popularity": 87, "price": 149},
        {"id": "DAV3", "name": "雷蛇 DeathAdder V3", "popularity": 85, "price": 119}
    ],
    "笔记本电脑": [
        {"id": "MBP14", "name": "MacBook Pro 14英寸", "popularity": 94, "price": 1999},
        {"id": "XPS13", "name": "戴尔 XPS 13", "popularity": 89, "price": 1299},
        {"id": "TPX1", "name": "ThinkPad X1 Carbon", "popularity": 86, "price": 1499}
    ]
}

# 模拟库存数据库
INVENTORY_DATABASE = {
    "WH-1000XM5": {"stock": 10, "location": "仓库-A"},
    "QC45": {"stock": 0, "location": "仓库-B"},
    "AIRMAX": {"stock": 5, "location": "仓库-C"},
    "PXC550": {"stock": 15, "location": "仓库-A"},
    "HT450": {"stock": 25, "location": "仓库-B"},
    "GPW": {"stock": 8, "location": "仓库-C"},
    "VIPER": {"stock": 12, "location": "仓库-A"},
    "DAV3": {"stock": 3, "location": "仓库-B"},
    "MBP14": {"stock": 7, "location": "仓库-C"},
    "XPS13": {"stock": 0, "location": "仓库-A"},
    "TPX1": {"stock": 4, "location": "仓库-B"}
}


# 工具1：搜索产品
@tool
def search_products(query: str) -> str:
    """搜索产品并返回按受欢迎度排序的结果"""
    print(f"🔍 [工具调用] search_products('{query}')")

    # 关键词映射，支持多种中文表达方式
    keyword_mapping = {
        "无线耳机": ["无线耳机", "蓝牙耳机", "头戴式耳机", "耳机"],
        "游戏鼠标": ["游戏鼠标", "电竞鼠标", "鼠标"],
        "笔记本电脑": ["笔记本电脑", "笔记本", "手提电脑", "电脑"]
    }

    # 查找匹配的类别
    matched_category = None
    for category, keywords in keyword_mapping.items():
        if any(keyword in query for keyword in keywords):
            matched_category = category
            break

    if matched_category and matched_category in PRODUCT_DATABASE:
        products = PRODUCT_DATABASE[matched_category]
        # 按受欢迎度排序
        sorted_products = sorted(products, key=lambda x: x['popularity'], reverse=True)
        result = f"找到 {len(sorted_products)} 个匹配 '{query}' 的产品:\n"

        for i, product in enumerate(sorted_products, 1):
            result += f"{i}. {product['name']} (ID: {product['id']}) - 受欢迎度: {product['popularity']}% - ￥{product['price']}\n"

        return result


# 工具2：检查库存
@tool
def check_inventory(product_id: str) -> str:
    """检查特定产品的库存状态"""
    print(f"📦 [工具调用] check_inventory('{product_id}')")

    if product_id in INVENTORY_DATABASE:
        stock_info = INVENTORY_DATABASE[product_id]
        status = "有库存" if stock_info['stock'] > 0 else "缺货"
        return f"产品 {product_id}: {status} ({stock_info['stock']} 件库存) - 位置: {stock_info['location']}"
    else:
        return f"未找到产品ID: {product_id}"


# 创建代理
# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 【理解这一行】创建能够执行工具循环的 Agent；模型可提出工具调用，执行器负责运行并回填结果。
agent = create_agent(
    model,
    tools=[search_products, check_inventory],
    system_prompt="""你是电商助手，遵循ReAct模式：
    1. 先推理用户需求
    2. 选择合适的工具执行操作
    3. 基于工具结果进行下一步推理
    4. 重复直到获得完整答案

    保持推理步骤简洁明了。"""
)

# 测试案例1：无线耳机搜索
# 【理解这一行】运行 Agent 执行流程；区分旧式 input 与新版 messages 状态格式，观察工具调用记录。
result1 = agent.invoke({
    "messages": [{"role": "user", "content": "查找当前最受欢迎的无线耳机并检查是否有库存"}]
})

print("\n" + "=" * 40)
print("📊 最终结果:")
for msg in result1['messages']:
    if hasattr(msg, 'content'):
        print(f"{msg.__class__.__name__}: {msg.content}")
print("=" * 40)

print()
print()

# # 详细追踪ReAct循环过程
def track_react_cycle(messages):
    print("ReAct循环步骤分析:")
    step = 1
    for i, msg in enumerate(messages):
        msg_type = msg.__class__.__name__
        # 【理解这一行】这里只检查可见 tool_calls 和消息类型，不是在读取模型内部完整推理过程。
        if msg_type == "AIMessage" and hasattr(msg, 'tool_calls') and msg.tool_calls:
            print(f"\n🔄 步骤{step}: Reasoning + Acting")
            for tool_call in msg.tool_calls:
                print(f"   🛠️  工具调用: {tool_call['name']}({tool_call['args']})")
            step += 1
        elif msg_type == "ToolMessage":
            print(f"   📋  观察结果: {msg.content[:80]}...")
        elif msg_type == "AIMessage" and not (hasattr(msg, 'tool_calls') and msg.tool_calls):
            print(f"\n✅ 最终回答: {msg.content}")

# 追踪案例1的ReAct循环
track_react_cycle(result1['messages'])