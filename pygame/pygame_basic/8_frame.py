import pygame
###################################################################################################################
# 0. 기본 세팅
# 초기화 (반드시 필요!)
pygame.init()


# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")


# 배경 설정
background = pygame.image.load(r"D:\Github_repo\python_study\pangGame\background.jpg")

# FPS 설정
clock = pygame.time.Clock()
###################################################################################################################
# 1. 사용자 게임 초기화 (배경, 게임 이미지, 좌표, 폰트, 속도 등)

# 2. 이벤트 루프 (계속 실행하여야 창이 꺼지지 않음)
running = True  # 게임이 진행중인지 확인하는 변수
while running:
    dt = clock.tick(60) # FPS 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 창이 닫히는 이멘트가 발생 시
            running = False

    # 3. 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 이미지 그리기

    pygame.display.update() # 화면이 변경될 시 다시 그려줘야 함
    pygame.time.delay(2000) # 종료 전 잠시 대기

# 게임 종료
pygame.quit()
