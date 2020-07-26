import pygame
import os
#########################################################################
# 0. 기본세팅 (초기화, 화면크기, 타이틀, FPS)
#########################################################################
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PANG")

clock = pygame.time.Clock()

#########################################################################
# 1. 사용자 게임 초기화 (변수설정 - 배경, 게임이미지, 좌표, 폰트, 속도 등)
#########################################################################
# 0. 디렉토리 (상대경로)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 1. 배경
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 2. 스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 3. 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height

character_to_x = 0
character_speed = 5

# 4. 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapons = []
weapon_speed = 10

# 5. 공 (에너미)
# 5.1 공 이미지
ball_images = [
    pygame.image.load(os.path.join(image_path, "ballon1.png")),
    pygame.image.load(os.path.join(image_path, "ballon2.png")),
    pygame.image.load(os.path.join(image_path, "ballon3.png")),
    pygame.image.load(os.path.join(image_path, "ballon4.png"))
]

# 5.2 공 속도
ball_speed_y = [-18, -15, -12, -9]

# 5.3 최초발생 공1 초기화
balls = [{
    "pos_x": 50,    # 공의 x축 좌표
    "pos_y": 50,    # 공의 y축 좌표
    "img_idx": 0, # 공의 이미지 인덱스
    "to_x": 3,      # x축 이동방향. -3이면 왼쪽으로, 3이면 오른쪽으로 이동
    "to_y": -6,     # y축 이동방향
    "init_spd_y": ball_speed_y[0] # y 최초 속도
}]

# 5.4 충돌 시 사라질 무기/공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# 6. 폰트
game_font = pygame.font.Font(None, 40)
result_msg = "GAME OVER"

# 7. 시간
total_time = 100
start_ticks = pygame.time.get_ticks()


#########################################################################
# 2. 메소드 분리
#########################################################################
def get_event_keydown(evt, character_to_x):
    if evt == pygame.K_LEFT:
        character_to_x -= character_speed
        return character_to_x
    elif evt == pygame.K_RIGHT:
        character_to_x += character_speed
        return character_to_x


def get_event_keyweapon(evt):
        weapon_pos_x = character_x_pos + (character_width / 2) - (weapon_width / 2)
        weapon_pos_y = character_y_pos
        weapons.append([weapon_pos_x, weapon_pos_y])
        return


def get_event_keyup(evt, character_to_x):
    if evt == pygame.K_LEFT or evt == pygame.K_RIGHT:
        character_to_x = 0
    elif evt == pygame.K_SPACE:
        character_to_x += 0
    return character_to_x


def set_character_display(character_x_pos):
    character_x_pos += character_to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    return character_x_pos


def set_weapon_display(weapons):
    weapons = [[weapon[0], weapon[1]-weapon_speed] for weapon in weapons]
    weapons = [[weapon[0], weapon[1]] for weapon in weapons if weapon[1] > 0]
    return weapons

def set_ball_display():
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


def draw_images():
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

#########################################################################
# 2. 로직 수행 (이벤트 루프)
#########################################################################
running = True

# 전체 루프
while running:
    dt = clock.tick(30)
    # KEY 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
            character_to_x = get_event_keydown(event.key, character_to_x)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            get_event_keyweapon(event.key)
        elif event.type == pygame.KEYUP:
            character_to_x = get_event_keyup(event.key, character_to_x)


    # 3.1 캐릭터 위치 정의
    character_x_pos = set_character_display(character_x_pos)

    # 3.2 무기 위치 정의
    weapons = set_weapon_display(weapons)
    
    # 3.3 공 위치 정의
    set_ball_display()

    # 이미지 그리기
    draw_images()

    # 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time: {}".format(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        game_result = "TIMEOUT!!!"
        running = False

    pygame.display.update() # 화면이 변경될 시 다시 그려줘야 함


#########################################################################
# 3. 로직 수행 (루프 종료)
#########################################################################
msg = game_font.render(result_msg, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)

pygame.display.update()
pygame.time.delay(2000)
pygame.quit()