from datetime import date, datetime

# 今日の日付を返す
def today_command():
    today = date.today() # 今日の日付はtoday()メソッドを使用する
    response = f'今日の日付は {today} です'
    return response

# 現在日時を返す
def now_command():
    now = datetime.now() # 現在日時はnow()メソッドを使用する
    response = f'現在の日時は　{now} です'
    return response

# 日付を作成
def weekday_command(command):
    data = command.split()
    year = int(data[1])
    month = int(data[2])
    day = int(data[3])
    one_day = date(year, month, day)

# 曜日の文字列
    weekday_str = '月火水木金土日'
    weekday = weekday_str[one_day.weekday()]


    response = f'{one_day} は {weekday}曜日です'
    return response
