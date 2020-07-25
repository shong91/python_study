import pygame
import os

###################################################################################################################
# 0. 기본 세팅
# 초기화 (반드시 필요!)
pygame.init()


# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang")

# FPS 설정
clock = pygame.time.Clock()

###################################################################################################################
# 1. 사용자 게임 초기화 (배경, 게임 이미지, 좌표, 폰트, 속도 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # 이미지 폴더 위치 반환

# 1.1 배경
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 1.2 스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 1.3 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

character_to_x = 0
character_speed = 5

# 1.4 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []
weapon_speed = 10


# 1.5 공
ball_images = [
    pygame.image.load(os.path.join(image_path, "ballon1.png")),
    pygame.image.load(os.path.join(image_path, "ballon2.png")),
    pygame.image.load(os.path.join(image_path, "ballon3.png")),
    pygame.image.load(os.path.join(image_path, "ballon4.png"))
]

# 공은 크기에 따라 속도가 다르다 (작아질수록 속도 감소)
ball_speed_y = [
    -18,
    -15,
    -12,
    -9
]


# 공 (딕셔너리)
balls = []

# 최초 발생하는 ballon1 에 대한 정의
balls.append({
    "pos_x": 50,    # 공의 x축 좌표
    "pos_y": 50,    # 공의 y축 좌표
    "img_idx": 0, # 공의 이미지 인덱스
    "to_x": 3,      # x축 이동방향. -3이면 왼쪽으로, 3이면 오른쪽으로 이동
    "to_y": -6,     # y축 이동방향
    "init_spd_y": ball_speed_y[0] # y 최초 속도
})

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1


# 폰트 정의
game_font = pygame.font.Font(None, 40)
game_result = "GAME OVER" # GAME OVER, MISSION CLEAR, TIMEOUT

total_time = 100
start_ticks = pygame.time.get_ticks()

# 2. 이벤트 루프 (계속 실행하여야 창이 꺼지지 않음)
running = True  # 게임이 진행중인지 확인하는 변수
while running:
    dt = clock.tick(30) # FPS 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 창이 닫히는 이멘트가 발생 시
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_pos_x = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_pos_y = character_y_pos
                weapons.append([weapon_pos_x, weapon_pos_y])
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3.1 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 3.2 무기 위치 정의 (발사)
    weapons = [[weapon[0], weapon[1]-weapon_speed] for weapon in weapons]
    # 천장에 닿은 무기는 없애기
    weapons = [[weapon[0], weapon[1]] for weapon in weapons if weapon[1] > 0]


    # 3.3 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 공 경계선 처리 - 벽/바닥에 닿을 시 튕겨 나온다
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    # 4. 충돌 처리
    # 4.1 캐릭터와 공의 충돌
    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 공 rect 정보 업데이트
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터 충돌 처리 (= 게임오버)
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 4.2 무기와 공의 충돌
        # 무기 rect 정보 업데이트
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 공과 무기 충돌 처리 (= 공쪼개기)
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx   # 해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx       # 해당 공 없애기 위한 값 설정
                # 가장 작은 공이 아니라면, 공 쪼개기
                if ball_img_idx < 3:
                    # 현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 크기 정보
                    small_ball_rect = ball_images[ball_img_idx+1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    balls.append({ # 왼쪽으로 튕겨나갈 공
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),    # 공의 x축 좌표
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),    # 공의 y축 좌표
                        "img_idx": ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x": -3,      # x축 이동방향. -3이면 왼쪽으로, 3이면 오른쪽으로 이동
                        "to_y": -6,     # y축 이동방향
                        "init_spd_y": ball_speed_y[ball_img_idx+1] # y 최초 속도
                    })

                    balls.append({       # 오른쪽으로 튕겨나갈 공
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),    # 공의 x축 좌표
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),    # 공의 y축 좌표
                        "img_idx": ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x": +3,      # x축 이동방향. -3이면 왼쪽으로, 3이면 오른쪽으로 이동
                        "to_y": -6,     # y축 이동방향
                        "init_spd_y": ball_speed_y[ball_img_idx+1] # y 최초 속도
                    })
                break # 안쪽 for문 탈출
        else:
            continue
        break # 바깥쪽 for문 탈출


    # 충돌된 공/무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공이 없을 시 미션 클리어
    if len(balls) == 0:
        game_result = "MISSON CLEAR!!!"
        running = False
        break



    # 5. 이미지 그리기 - 파이썬의 동작 순서는 위에서 아래로
    screen.blit(background, (0,0))

    for weapon_pos_x, weapon_pos_y in weapons:
        screen.blit(weapon, (weapon_pos_x, weapon_pos_y))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time: {}".format(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        game_result = "TIMEOUT!!!"
        running = False

    pygame.display.update() # 화면이 변경될 시 다시 그려줘야 함


# 게임 종료
msg = game_font.render(game_result, True, (255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)

pygame.display.update() # 화면이 변경될 시 다시 그려줘야 함
pygame.time.delay(2000)
pygame.quit()
