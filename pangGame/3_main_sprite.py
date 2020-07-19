import pygame

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


# 스프라이트(메인 캐릭터) 불러오기
character = pygame.image.load(r"D:\Github_repo\python_study\pangGame\character.jpg")
character_size = character.get_rect().size  # 이미지의 크기를 구해온다
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height


# 이벤트 루프 (계속 실행하여야 창이 꺼지지 않음)
running = True  # 게임이 진행중인지 확인하는 변수
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 창이 닫히는 이멘트가 발생 시
            running = False

    # 배경 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 화면이 변경될 시 다시 렌더링 해줘야 함


# 게임 종료
pygame.quit()
