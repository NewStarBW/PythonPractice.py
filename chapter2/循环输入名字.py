while 1:
    name = input("请输入您的姓名：")
    if name == "郭清":
        print("郭靖同学，学好 Python，前途无量")
    elif name == "张三":
        print("您好，张三先生。有什么我能帮助您的吗？")
    elif name == "李四":
        print("李四，请问您需要什么帮助吗？")
    elif name == "end":
        break
    else:
        print("很高兴认识你，" + name + "。")