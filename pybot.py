while True: # 常に条件を満たす
# input関数でユーザーからの入力を受付、入力された値をcommand変数に保存
    command = input('pybot> ')
    # print(command)
# 条件分岐であいさつを切り替える
    if 'こんにちは' in command:
        print('コンニチハ')
    elif 'ありがとう' in command:
        print('ドウイタシマシテ')
    elif 'さようなら' in command:
        print('サヨウナラ')
        break #繰り返し処理を終了
    else:
        print('ナニヲイッテイルカワカラナイ')
