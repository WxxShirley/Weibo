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
import jieba
from wordcloud import WordCloud
import matplotlib.font_manager as fm
from imageio import imread
from PIL import Image
import wordcloud
import csv
import numpy as np

# 生成微博内容词云
def generateWordCloud(user_id):
    jpg = imread('cc.jpg')
    mask = np.array(Image.open('cc.jpg'))
    image_colors = wordcloud.ImageColorGenerator(mask)

    with open("weibo.csv", 'r') as file:
        reader = csv.reader(file)
        weibos = list(reader)

    yc_text = ""
    for weibo in weibos:
        if weibo[1] == user_id:
            if weibo[9] == '0':
                repost_text += weibo[2]
            elif weibo[9] == '1':
                yc_text += weibo[2]

    f = open("baidu_stopwords.txt", "r")
    stopwords = {}.fromkeys(f.read().split("\n"))
    f.close()

    jieba.load_userdict("baidu_stopwords.txt")
    segs = jieba.cut(yc_text)

    mytext_list = []
    for seg in segs:
        if seg not in mytext_list and seg != "" and len(seg) != 1:
            mytext_list.append(seg.replace(" ", ""))
    yc_text = ",".join(mytext_list)
    print(yc_text)

    if len(yc_text) > 0:
        wc = WordCloud(background_color="white", max_words=200, min_font_size=10, max_font_size=35, width=400,
                       font_path="/Users/wu/Downloads/msyh/msyh.ttf", mask=mask, color_func=image_colors)
        wc.generate(yc_text)
        file_path = user_id + "_yc" + ".png"
        wc.to_file(file_path)