# coding : utf-8
# 文字コードの宣言
# じゃんけんプログラム

# 
# プレイヤーの名前と出す手を入力
# マシンが出す手をランダムに指定
# 両者を比較し結果を出力
# 

# 
# 前準備
# 

import random

# handクラスの作成
class Hand():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

# 処理部
# ランダムにマシンの出す手を決める
def machin_hand():
    return Hand("CPU", random.randint(0, 2))

# 両者の出した手を表示する
def show_hands(player1, player2):
    
    # player1の名前と出した手を表示
    hand1 = ""
    # player1の出した手を代入する
    if player1.hand == 0:
        hand1 = "グー"
    elif player1.hand == 1:
        hand1 = "チョキ"
    elif player1.hand == 2:
        hand1 = "パー"
    # 結果を表示
    print(f"{player1.name:s}は{hand1:s}を出しました")

    # player2の名前と出した手を表示
    hand2 = ""
    # player2の出した手を代入する
    if player2.hand == 0:
        hand2 = "グー"
    elif player2.hand == 1:
        hand2 = "チョキ"
    elif player2.hand == 2:
        hand2 = "パー"
    # 結果を表示  
    print(f"{player2.name:s}は{hand2:s}を出しました")


# プレイヤーとマシンの出した手を比較
def referee(player1, player2):
    # 条件分岐
    # 引き分け
    if player1.hand == player2.hand:
        print("引き分け")
    # player1がグーを出した場合
    elif player1.hand == 0:
        # player2がチョキを出した場合
        if player2.hand == 1:
            print(f"{player1.name:s}の勝ちです")
        # player2がパーを出した場合
        else:
            print(f"{player2.name:s}の勝ちです")

    # player1がチョキを出した場合
    elif player1.hand == 1:
        # player2がパーを出した場合
        if player2.hand == 2:
            print(f"{player1.name:s}の勝ちです")
        # player2がグーを出した場合
        else:
            print(f"{player2.name:s}の勝ちです")

    # player1がパーを出した場合
    elif player1.hand == 2:
        # player2がグーを出した場合
        if player2.hand == 0:
            print(f"{player1.name:s}の勝ちです")
        # player2がチョキを出した場合
        else:
            print(f"{player2.name:s}の勝ちです")


# 対戦結果を表示する

# 操作部
# プレイヤーの名前と出す手を入力
player_name = input("名前を入力してください ")
player_hand = input("選んでくださいグー:0 チョキ:1 パー:2 ")
player_hand = int(player_hand)
player = Hand(player_name, player_hand)

# マシンの出す手を選択
machin = machin_hand()

# 両者の出した手を表示
show_hands(player, machin)

# 判定と結果の表示
referee(player, machin)
