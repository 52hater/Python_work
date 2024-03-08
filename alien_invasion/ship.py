import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./alien_invasion/images/ship.bmp')

rect = image.get_rect()

while True: # 무한루프 > if로 탈출
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #raise SystemExit

    # Do logical updates here. / 업데이트 비행기, 위치,,
    # ...

    screen.fill("grey")  # Fill the display with a solid color / 디폴트는 까만색

    # Render the graphics here. / 비행기, 적, 총알,,, 점수 등 화면에 표시될 여러가지 랜더링
    # ...
    

    image.blit(image, rect)


    pygame.display.flip()  # Refresh on-screen display / 플립:뒤집다 > 왜 뒤집지 > 위아래변경 > 뭔가동작을?끝내고? 새로 그리는?? > 리프레쉬될때 자연스럽게 나오게 60fps
    clock.tick(60)         # wait until next frame (at 60 FPS) / 초당 그림을 60장 그린다 / 한번돌떄 얼만큼 움직이냐