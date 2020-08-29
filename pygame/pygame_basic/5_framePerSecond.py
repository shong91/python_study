import pygame
# frame per second (초당 프레임)
# 초기화 (반드시 필요!)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")


# 배경 설정
background = pygame.image.load(r"D:\Github_repo\python_study\pygame_basic\background.jpg")

# FPS 설정
clock = pygame.time.Clock()

# 스프라이트(메인 캐릭터) 불러오기
character = pygame.image.load(r"D:\Github_repo\python_study\pygame_basic\character.jpg")
character_size = character.get_rect().size  # 이미지의 크기를 구해온다
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 캐릭터의 좌표 & 이동 속도
to_x = 0
to_y = 0
character_speed = 0.6

# 이벤트 루프 (계속 실행하여야 창이 꺼지지 않음)
running = True  # 게임이 진행중인지 확인하는 변수
while running:
    dt = clock.tick(30) # FPS 설정
    # print("fps: " + str(clock.get_fps()))
    # FPS 값이 달라지더라도, 캐릭터가 움직이는 속도는 일정해야 한다 (이동 프레임의 부드러움 정도 차이는 있어야 하나, 속도는 변함 없어야 함)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 창이 닫히는 이멘트가 발생 시
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # FPS 계산 (dt) 해주어야 함
    character_y_pos += to_y * dt

    # 가로 세로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # 배경 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 화면이 변경될 시 다시 그려줘야 함


# 게임 종료
pygame.quit()
