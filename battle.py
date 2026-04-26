player_hp = 100
enemy_hp = 100

print("=== バトル開始 ===")
print("勇者のHP：" + str(player_hp))
print("スライムのHP：" + str(enemy_hp))

while enemy_hp > 0 and player_hp > 0:
    print("\n--- ターン---")
    print("1: こうげき 2: にげる")
    action = input("行動を選んでください:")

    if action == "1":
        enemy_hp -= 10
        print("勇者の攻撃！１０ダメージ！")
        print("スライムのHP: " + str(enemy_hp))

        if enemy_hp > 0:
            player_hp -= 50
            print("スライムの反撃！５ダメージ！")
            print("勇者のHP: " + str(player_hp))

        if player_hp == 0:
            print("勇者は倒れた...")
            break    
    elif action == "2":
        print("勇者は逃げ出した‼")
        break


print("\n=== バトル終了 ===")
if enemy_hp <= 0:
    print("スライムを倒した！")