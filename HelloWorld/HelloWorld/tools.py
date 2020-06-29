'''
==================================================微博内容关键词==================================================
('秦昊', 11)
('伊能静', 5)
('大家', 4)
('一起', 3)
('姐姐', 3)
('爬山', 3)
('隐秘', 3)
('角落', 3)
('导演', 3)
('锦绣', 2)

==================================================沉寂关注==================================================
[1740661795, '电影风中有朵雨做的云']
[5136362277, '微博红包']
[5335243916, '沙海官微']
[5898283182, '电影妖猫传官博']

==================================================异常粉丝==================================================
==================================================关注分布==================================================
红V与橙V数量:64
蓝V:28

'''
import json
import shutil

def writeout():
    # 模拟数据
    dict = {
        "uid":"1740197697",
        "username":"sfer-何晓昕",
        "沉寂关注": [
            [7236957425, 'KK俱乐部_China'],
            [7239630504, 'KK-Grunt沈哲'],
            [1752820413, '高以翔Godfrey'],
            [5149686285, '公子乔一'],
            [5370284657, '李安琪Angel']],
        "异常粉丝":[[6340710640, '用户6340710640'],
                [5362576433, 'YeHongyi'],
                [2260088181, 'Ga6rie丨'],
                [3846342412, '音旋在颤谷']],
        "微博内容关键词": [
            ('秦昊', 11), ('伊能静', 5), ('大家', 4), ('一起', 3),
                        ('姐姐', 3), ('爬山', 3), ('隐秘', 3), ('角落', 3),('导演', 3), ('锦绣', 2)],
    }
    with open('out.json', 'w') as f:
        json.dump(dict, f)

def get_data():
    # YOUR PATH of (1740197697.json)
    dict = json.load(open("/Users/wu/Downloads/Weibo-master/HelloWorld/HelloWorld/1740197697.json",encoding='utf-8-sig'))
    length = len(dict["spammer"])
    if length>5: #只显示至多6位用户的
        dict["spammer"] = dict["spammer"][:6]
    return dict

def keyword():
    dict = json.load(open("/Users/wu/Downloads/Weibo-master/HelloWorld/HelloWorld/out.json"))
    kw=dict['微博内容关键词']
    print(kw)

def chenji():
    dict = json.load(open("/Users/wu/Downloads/Weibo-master/HelloWorld/HelloWorld/out.json"))
    kw = dict['沉寂关注']

    return kw

writeout()
chenji()