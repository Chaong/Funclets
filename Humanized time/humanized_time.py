import time
import datetime


while True:
    # 获取当前和输入的时间戳
    now_ts = int(time.time())
    input_ts = int(input("[Input timestamp (s) ] > "))
    ts_diff = now_ts - input_ts   # 得到时间戳的差

    # 将时间戳转换为结构时间
    now_array = time.localtime(now_ts)
    input_array = time.localtime(input_ts)
    # 格式化结构时间
    now_time = time.strftime("%Y-%m-%d %H:%M", now_array)
    input_time = time.strftime("%Y-%m-%d %H:%M", input_array)

    # 获取今天、昨天、前天
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    beforeday = today - datetime.timedelta(days=2)

    # 截取时间字符串获取对应数据
    hm = input_time[11:16]   # 输入的时分
    mdhm = input_time[5:16]   # 输入的月日时分
    input_time_ymd = input_time[0:10]   # 输入的年月日
    now_year = int(now_time[0:4])   # 当前年
    input_year = int(input_time[0:4])   # 输入的年

    # 将年月日字符串转换成日期类型
    input_ymd = datetime.date(*map(int, input_time_ymd.split("-")))

    # 条件判断
    if ts_diff <= 60:
        print("刚刚")

    elif input_ymd == today:
        print(hm)

    elif input_ymd == yesterday:
        print("昨天 %s" % hm)

    elif input_ymd == beforeday:
        print("前天 %s" % hm)

    elif input_year == now_year:
        print(mdhm)

    else:
        print(input_time)