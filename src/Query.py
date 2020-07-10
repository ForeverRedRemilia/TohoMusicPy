import datetime
import xlwt
import MusicDict
import WebCon

musicDict = MusicDict.musicDict
i = 0
length = len(musicDict)
# 创建人物——数量Dict，用于排序输出
characterNumDict = {}
# 存放出现过的数量值是否被用到
vlDic = {}
# 存放出现过的数量值的次数
vlCount = {}
for key, value in musicDict.items():
    musicList = value
    num = 0
    for music in musicList:
        each = WebCon.webconnect(music)
        try:
            num += int(each)
        except ValueError:
            each = WebCon.webconnect(music)
            num += int(each)
        print(each)
    if key == '里香':
        num += 14
    numStr = str(num)
    print(key + " : " + numStr)
    print("进度%s/%s" % (i + 1, length))
    characterNumDict[key] = num
    vlDic[numStr] = 'false'
    if numStr in vlCount.keys():
        vlCount[numStr] = vlCount[numStr] + 1
    else:
        vlCount[numStr] = 1
    i += 1
    if i == length:
        break
dictList = sorted(characterNumDict.items(), key=lambda d: d[1], reverse=False)

# 创建excel表格
wb = xlwt.Workbook()
ws = wb.add_sheet('Query')
ws.write(0, 0, 'name')
ws.write(0, 1, 'type')
ws.write(0, 2, 'value')
ws.write(0, 3, 'date')
# name的初始值
j = 0
# 单条数据的行数
cul = 0
# 初始化增加的天数
day = 0
# 排名
rank = len(vlCount) + 1
for key, value in dictList:
    j += 1
    curVl = vlDic[str(value)]
    if curVl == 'false':
        # 记录最早出现该值的排名
        vlDic[str(value)] = 'true'
        # rank = len(characterNumDict) - j + 1 - vlCount[str(value)]
        rank -= 1
        day += 1
    # 天数
    x = 0
    while cul < j * 20:
        cul += 1
        ws.write(cul, 0, key)
        ws.write(cul, 1, rank)
        ws.write(cul, 2, value)
        nowTime = (datetime.datetime.now() + datetime.timedelta(days=x + day)).strftime("%Y-%m-%d")
        ws.write(cul, 3, nowTime)
        x += 1
wb.save('result.xls')
