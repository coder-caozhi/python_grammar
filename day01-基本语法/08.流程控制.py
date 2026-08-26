age = 1

if age > 18:
    print("你是一个成年人")

print("="*60)

if 0 <= age <= 3:
    if age <= 1:
        print("哺乳期")
    elif age <= 2:
        print("哺乳期已结束")
    else:
        print("该上幼儿园了")
elif 3 < age < 12:
    print("儿童")
elif 13 < age < 17:
    print("青少年")
elif 17 < age < 44:
    print("青年")
elif 44 < age < 59:
    print("中年")
elif 60 < age < 116:
    print("老年")
else:
    print("您已成仙")

print("="*60)

status = 600
match status:
    case 200:
        print("请求成功")
    case 302:
        print("重定向")
    case 403:
        print("无权访问")
    case 404:
        print("您请求的资源到火星了")
    case 405:
        print("请求方式不允许")
    case 500:
        print("服务器内部错误")
    case _:
        print("未知的状态码")
