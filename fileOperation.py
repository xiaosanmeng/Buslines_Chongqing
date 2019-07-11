import os
import json
# 获取目标文件夹的路径
filedir = 'each_busline_information_chongqing_1'
# 获取文件夹中的文件名称列表
filenames = os.listdir(filedir)
temp = []
for filename in filenames:
    temp.append(filename[0:3])
pass
jsonData = json.dumps(temp, indent=2, ensure_ascii=False)
jsonFile = open('buslines_captured.json', 'w', encoding='utf-8')
jsonFile.write(jsonData)
jsonFile.close()
print(len(temp))
