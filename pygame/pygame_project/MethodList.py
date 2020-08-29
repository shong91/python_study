class MethodList:
    def __init__(self):
        pass

    def quit_game(self, event):
        if event.type == pygame.QUIT:  # 창이 닫히는 이멘트가 발생 시
            running = False
            return running



m = MethodList()
m.quit_game()