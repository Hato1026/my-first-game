import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("RPGゲーム")
clock = pygame.time.Clock()

# 勇者の設定
player_x = 400
player_y = 300
player_speed = 5

in_battle = False

# 敵の設定
enemy_x = 600
enemy_y = 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力で勇者を動かす
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    
     # 当たり判定
    if (abs(player_x - enemy_x) < 40 and abs(player_y - enemy_y) < 40):
        if not in_battle:
            in_battle = True
            print("バトル開始！")
    
    # 画面を塗りつぶす
    screen.fill((0, 0, 0))

    # 勇者を青い四角で描画
    pygame.draw.rect(screen, (0, 100, 255), (player_x, player_y, 40, 40))

    # 敵を赤い四角で描画
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 40, 40))
   
    # 画面を塗りつぶす
    screen.fill((0, 0, 0))

  # 画面を塗りつぶす
    screen.fill((0, 0, 0))

    if in_battle:
        # 背景を暗くする
        screen.fill((20, 20, 40))

        font = pygame.font.SysFont("msmincho", 36)

        # 敵の情報
        text = font.render("スライム  HP：30", True, (255, 100, 100))
        screen.blit(text, (100, 100))

        # 勇者の情報
        text = font.render("勇者  HP：100", True, (100, 200, 255))
        screen.blit(text, (100, 400))

        # コマンド
        text = font.render("1: こうげき  2: ポーション  3: にげる", True, (255, 255, 255))
        screen.blit(text, (100, 500))

    else:
        # フィールド画面
        pygame.draw.rect(screen, (0, 100, 255), (player_x, player_y, 40, 40))
        pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 40, 40))

    pygame.display.flip()
    clock.tick(60)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()