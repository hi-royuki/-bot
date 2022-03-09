# 挨拶の辞書データを定義する。
bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'アリガトウ',
    'さようなら': 'サヨウナラ',
}

while True: # 常に条件を満たす
# input関数でユーザーからの入力を受付、入力された値をcommand変数に保存
    command = input('pybot> ')
    # print(command)
    response = '' #空文字列で初期化する
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break

        if not response:
            response = '何ヲ言ッテイルカ、ワカラナイ'
        print(response)

        if 'さようなら' in command:
            break
