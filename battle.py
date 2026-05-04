import random

enemies = [
    {"name": "スライム", "hp": 30, "attack": 5},
    {"name": "ゴブリン", "hp": 50, "attack": 15},
    {"name": "ドラゴン", "hp": 100, "attack": 30},
]

enemy = random.choice(enemies)
enemy_hp = enemy["hp"]
player_hp = 100
potion = 3

print("=== バトル開始 ===")
print(enemy["name"] + "があらわれた！")
print("勇者のHP：" + str(player_hp))
print(enemy["name"] + "のHP：" + str(enemy_hp))

while enemy_hp > 0 and player_hp > 0:
    print("\n--- ターン ---")
    print("1: こうげき  2: ポーション  3: にげる")
    action = input("行動を選んでください：")

    if action == "1":
        enemy_hp -= 10
        print("勇者の攻撃！10ダメージ！")
        print(enemy["name"] + "のHP：" + str(enemy_hp))

        if enemy_hp > 0:
            player_hp -= enemy["attack"]
            print(enemy["name"] + "の反撃！" + str(enemy["attack"]) + "ダメージ！")
            print("勇者のHP：" + str(player_hp))

        if player_hp <= 0:
            print("勇者は倒れた...")
            break

    elif action == "2":
        if potion > 0:
            player_hp += 30
            if player_hp > 100:
                player_hp = 100
            potion -= 1
            print("ポーションを使った！HPが30回復！")
            print("勇者のHP：" + str(player_hp))
            print("残りポーション：" + str(potion) + "個")
        else:
            print("ポーションがない！")

    elif action == "3":
        print("勇者は逃げ出した！")
        break

print("\n=== バトル終了 ===")
if enemy_hp <= 0:
    print(enemy["name"] + "を倒した！")