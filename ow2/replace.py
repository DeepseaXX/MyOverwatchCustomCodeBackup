# 传入文件(file),将旧内容(old_content)替换为新内容(new_content)
def replace(file, old_content, new_content):
    content = read_file(file)
    content = content.replace(old_content, new_content)
    rewrite_file(file, content)

# 两个list
def replacelist(file, old_list, new_list):
    content = read_file(file)
    for old, new in zip(old_list, new_list):
        content = content.replace(old, new)
    rewrite_file(file, content)

# 一个list
def replaceonelist(file, list):
    content = read_file(file)
    for item in list:
        content = content.replace(item[0], item[1])
    rewrite_file(file, content)

# 读文件内容
def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
        f.close()

    return read_all

# 写内容到文件
def rewrite_file(file, data):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)
        f.close()


filename = './修改后/2023.01.02/中城.txt'
original = []
after=[]
forenlist=[]
forenlist.append(["★ Find items from the list","★ 寻找列表中物品"])
forenlist.append([" and press[F](Interact)","并按下 [F] (互动)"])
forenlist.append([" and press [F] (Interact)","并按下 [F] (互动)"])
forenlist.append(["★ Set high or ultra model detail settings to see all items ","★ 设置高或超高画质细节来显示所有物品"])
forenlist.append(["★ Set medium or higher model detail settings to see all items ",
                 "★ 设置中或高画质细节来显示所有物品"])
forenlist.append(["★ List of items", "★ 物品列表"])
forenlist.append(
    ["★ Try more than 50 interesting maps:\\r\\nbit.do/finditems", "★ 尝试50多张新地图:\\r\\nbit.do/finditems\\r\\n原作者：Foren#2660\\r\\n中文看图找物找东西交流群1074896927"])

forenlist.append(["Find Items ★", "列文虎克找东西 ★"])
forenlist.append(
    ["Set high or ultra model detail settings to see all items", "设置高或超高画质细节来显示所有物品"])
forenlist.append(
    ["Options > Video > Graphics quality > Advanced > Model Detail", "设置-视频-图像质量-高级-模型细节"])
forenlist.append(["Find items from the list", "寻找列表中的物品"])
forenlist.append(
    ["Press [F] (Interact button) when you are close to the item", "靠近物品后按下 [F] (互动键)"])
forenlist.append(["String(\"Run\")", "Custom String(\"加速\")"])
forenlist.append(["String(\"Speed\"), String(\"Upgrade\")", "Custom String(\"速度\"), Custom String(\"升级\")"])
forenlist.append(["String(\"Found\")", "Custom String(\"已找到\")"])
forenlist.append(["String(\"No\"), String(\"Item\")", "Custom String(\"错\"), Custom String(\"误\")"])
forenlist.append(["String(\"Next Attempt\")", "Custom String(\"下次尝试\")"])
forenlist.append(["String(\"{0} sec\")", "Custom String(\"{0} 秒\")"])
forenlist.append(["String(\"Winner\")", "Custom String(\"胜利\")"])
forenlist.append(["String(\"Visible\")", "Custom String(\"可见\")"])
forenlist.append(["Custom String(\"Try other maps!\"), Custom String(\"bit.do/finditems\")", "Custom String(\"试试其他地图！\"), Custom String(\"bit.do/finditems\")"])
forenlist.append(["//Set Invisible", "Set Invisible"])
forenlist.append(["Set Invisible", "//Set Invisible"])





# 替换操作(将test.txt文件中的'Hello World!'替换为'Hello Qt!')
#replace(filename, 'Find items', 'test')
replaceonelist(filename, forenlist)

#itemlist.append(["", ""])
