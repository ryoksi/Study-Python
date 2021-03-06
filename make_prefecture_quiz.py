import pandas as pd
import random
import numpy as np

#目標：ランダムな問題集ファイルを作成する

#[[都道府県][県庁所在地]]のようにデータ整形
def make_capitals() -> list:
    capitals_df = pd.read_excel("todouhuken.xlsx", sheet_name = 0)
    capitals_df = capitals_df[["都道府県 県あり", "県庁所在地 市区町村あり"]]

    capitals = capitals_df.values.tolist()


    return capitals

#2次元配列シャッフル
def shuffle_capitals(capitals: list) -> list:
    return np.random.shuffle(capitals)

def shuffle_list(list: list) -> list:
    return random.shuffle(list)

def make_answer_list(capitals: list, question_num: int) -> list:
    answer_list = []
    answer_list.append(capitals[question_num][1])

    for i in range(3):
        random_num = generate_random_num()
        answer_list.append(capitals[random_num][1])

    shuffle_list(answer_list)
    return answer_list

def generate_random_num() -> int:
    random_num = random.randint(6, 46)
    past_random_num = []
    if random_num in past_random_num:
        return random_num

    return random_num


# 問題ファイルを作成
def make_workbook(quiz_num: int, capitals: list) -> None:

    quiz_file = open('capitalquiz{}.txt'
                     .format(quiz_num + 1), 'w', encoding='utf-8')

    quiz_file.write('日付：\n名前:\n学籍番号:\n\n')
    quiz_file.write(('' * 20) + '都道府県庁所在地クイズ(問題番号{})'
                    .format(quiz_num + 1))
    quiz_file.write('\n\n')

    for question_num in range(5):
        answer_list = make_answer_list(capitals, question_num)
        quiz_file.write('{}. {}の県庁所在地は？\n\n'
                    .format(question_num + 1, capitals[question_num][0]))

        for i in range(4):
            quiz_file.write('{}. {}\n'
                            .format('ABCD'[i], answer_list[i]))

        quiz_file.write('\n')

def input_sheet() -> int:
    sheet = input('発行部数を入力してください--->')
    try:
        sheet = int(sheet)
        sheet > 0
    except:
        print('0以上の整数で入力してください')
        return input_sheet()

    return sheet


# メイン
def make_prefecture_quiz() -> None:
    sheet = input_sheet()
    for quiz_num in range(sheet):
        capitals = make_capitals()
        shuffle_capitals(capitals)
        make_workbook(quiz_num, capitals)


make_prefecture_quiz()

