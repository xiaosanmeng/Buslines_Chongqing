import os
import json
#获取目标文件夹的路径
filedir = 'each_busline_information_chongqing_1'
#获取文件夹中的文件名称列表（含文件扩展名）
filenames = os.listdir(filedir)
all_buslines = []
for filename in filenames:
    # 每个文件的路径（这里为方便，取相对路径）
    filePath = filedir + '\\' + filename
    # 文件对象
    file = open(filePath, "rb")
    # 加载json文件的内容
    jsonContents = json.load(file)
    all_buslines.append(jsonContents[0]['buslineGPS'])
pass
jsonData = json.dumps(all_buslines, indent=2, ensure_ascii=False)
jsonFile = open('all_buslines_gps_chongqing_1.json', 'w', encoding='utf-8')
jsonFile.write(jsonData)
jsonFile.close()
print(len(all_buslines))
