#! python3
"""
windowsはバッチファイルを作ることでwin+Rで簡単に実行可能になる。
mail.batの中身
@py.exe [パイソンファイルの絶対パス]　%*
@pause
%*が引数を表しているため抜けないように注意する。
"""
import sys
import pyperclip

greeting = {"greeting1": "初めてメールを送らせていただきます。「」の「」と申します",
            "greeting2": "突然のご連絡失礼いたします。「」の「」と申します",
            "greeting3": "お世話になっております。「」の「」と申します",
            "command": r"Start C:\Windows\system32\rundll32.exe sysdm.cpl, EditEnvironmentVariables"}

if len(sys.argv) == 1:
    print("使い方：mail_greeting.py [greeting1or2or3]")
    sys.exit()

message = sys.argv[1]

if message in greeting:
    pyperclip.copy(greeting[message])
    print("定型文をクリップボードにコピーしました")
else:
    print("指定した定型文は存在しません。")

