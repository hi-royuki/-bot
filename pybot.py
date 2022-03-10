command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines() #　改行で分割して行ごと文字列のリストを作成します

# あいさつの辞書データの作成
bot_dict = {} #　空の辞書データの変数を用意する
for line in lines:
    word_list = line.split(',') #　１行分の文字列をカンマで2つの文字列に分割
    key = word_list[0] # 分割した文字列の0番目を辞書のキーに
    response = word_list[1] # 分割した文字列の１番目をバリューに
    bot_dict[key] = response # 辞書データに値を追加


# 挨拶の辞書データを定義する。
# bot_dict = {
#     'こんにちは': 'コンニチハ',
#     'ありがとう': 'アリガトウ',
#     'さようなら': 'サヨウナラ',
# }

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

# while True:
#     command = input('pybot> ')
#     response = ''
#     for message in bot_dict:
#         if message in command:
#             response = bot_dict[message]
#             break
#
#     if not response:
#         response = '何を言っているかわからない'
#     print(response)
#
#     if 'さようなら' in command:
#         break

#
# while True:
#     command = input('pybot> ')
#     response = ''
#     for message in bot_dict:
#         if message in command:
#             response = bot_dict[message]
#             break
#
#     if not response:
#         response = '何ヲ言ッテルカ、ワカラナイ'
#     print(response)
#
#     if 'さようなら' in command:
#         break
