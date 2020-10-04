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

# handクラスの作成
class Hand():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

# 処理部
# ランダムに出す手を決める
# プレイヤーとマシンの出した手を比較

# 表示部
# 対戦結果を表示する

# 操作部
player_name = input("名前を入力してください")
player_hand = input("選んでくださいグー:0 チョキ:1 パー:2 ")
player_hand = int(player_hand)

player = Hand(player_name, player_hand)

print(player)
print(player.name)
print(player.hand)
