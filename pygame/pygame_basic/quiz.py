import pygame
import random
###################################################################################################################
# 0. 기본 세팅
# 초기화 (반드시 필요!)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("escape XXX")


# 배경 설정
background = pygame.image.load(r"D:\Github_repo\python_study\pygame_basic\background.jpg")

# FPS 설정
clock = pygame.time.Clock()

###################################################################################################################
# 1. 사용자 게임 초기화 (배경, 게임 이미지, 좌표, 폰트, 속도 등)

# 캐릭터 설정
character = pygame.image.load(r"D:\Github_repo\python_study\pygame_basic\manual.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width /2)
character_y_pos = screen_height - character_height

# 캐릭터 좌표
to_x = 0
# to_y = 0
character_speed = 0.5

# 에너미 캐릭터 설정
enemy = pygame.image.load(r"D:\Github_repo\python_study\pygame_basic\continue.jpg")
enemy2 = pygame.image.load(r"D:\Github_repo\python_study\pygame_basic\continue2.jpg")
enemy3 = pygame.image.load(r"D:\Github_repo\python_study\pygame_basic\stun.jpg")

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]

enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]



# 에너미 위치 설정 : screen_width 내에서 랜덤하게 등장
# 에너미 y좌표 > screen_height 가 되면 새로운 에너미 등장
enemy_cnt = 1;
# enemy_x_pos = (random() * screen_width) - enemy_width
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_x_pos_2 = 0
enemy_x_pos_3 = 0
enemy_y_pos = 0
enemy_speed = 5

# 텍스트 폰트 정의
game_font = pygame.font.Font(None, 40)

total_time = 100
start_ticks = pygame.time.get_ticks()

# 2. 이벤트 루프 (계속 실행하여야 창이 꺼지지 않음)
running = True  # 게임이 진행중인지 확인하는 변수
while running:
    dt = clock.tick(60) # FPS 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 창이 닫히는 이멘트가 발생 시
            running = False

        # 3-1. 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
        enemy_cnt += 1
        print(enemy_x_pos, enemy_y_pos)
        if enemy_cnt > 5:
            enemy_x_pos_2 = random.randint(0, screen_width - enemy_width)
            if enemy_cnt > 10:
                enemy_x_pos_3 = random.randint(0, screen_width - enemy_width)


    # 3-2. 에너미 위치 정의
    character_x_pos += (to_x * dt)
    enemy_y_pos += enemy_speed # * dt


    # 가로 세로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if(character_rect.colliderect(enemy_rect)):
        print('충돌! ')
        running = False


    # 타이머
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 출력할 글자, True, 색상

    if total_time - elapsed_time <= 0:
        print("타임아웃!! ")
        running = False

    # 5. 이미지 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    if enemy_cnt > 5:
        screen.blit(enemy2, (enemy_x_pos_2, enemy_y_pos))
        if enemy_cnt > 10:
            screen.blit(enemy3, (enemy_x_pos_3, enemy_y_pos))
    screen.blit(timer, (10, 10))

    pygame.display.update() # 화면이 변경될 시 다시 그려줘야 함
    # game.time.delay(2000) # 종료 전 잠시 대기

# 게임 종료
pygame.quit()
