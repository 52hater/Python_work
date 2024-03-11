import sys
import pygame

# 매직넘버를 변수추출로 뺴는것처럼 변화를 고립시켜야함****
# 상수말고 로직을 고립시키는건? > 함수를 만듦**** > 리팩터에서 함수추출, 파일을 만들어서 모아놓고 임포트, form util import init, create_bullet, render 처럼
# 범위를 좁히고 좁혀서 고립화 -> 오류도 줄이고, 수정쉬워짐
# 객체 안에 함수와 변수만 있지


pygame.init()

WIDTH = 1280 # 상수는 대문자로 ##****이런식으로 변화를 고립시켜라
screen = pygame.display.set_mode((WIDTH,720)) # 여기서 720은 상수니까 드래그해서 우클릭 > refactor > 변수추출 > rename(F2) HEIGHT로

clock = pygame.time.Clock()
image = pygame.image.load('./alien_invasion/images/ship.bmp') # 이미지도 불변하는 상수니까 드래그 우클릭 리팩터 변수추출 리네임 SHIP_IMG_PATH 와 같이
# rect = pygame.Rect((1280/2, 720/2), (400, 400))
ship_rect = image.get_rect()
# image_rect.left = 1280/2
# image_rect.top = 600
# image_rect.midbottom = screen.get_rect().midbottom
# screen_rect = pygame.Rect(0, 0, 1280, 720) # 이렇게 렉터라는 객체를 만들었고
screen_rect = screen.get_rect() # 렉터객체를 받아놨다 , 만들어놓은걸 그냥 주는거
# image_rect = image.get_rect() # 이미지 로드할때 렉트를 만들어놨다
ship_rect.midbottom = screen_rect.midbottom

#rect = image.get_rect()

def create_bullet(ship_rect):
    bullet = pygame.Rect(0, 0, 5, 30)
    bullet.midtop = ship_rect.midtop # 여기에 + ship_rect.height 하면 총알이 앞에서 나갈것같은데 오류가 남 왜지
    bullet.top -= ship_rect.height # 이렇게 하면 총알이 우주선 앞에서 나가네
    return bullet

bullets = []
bullet = create_bullet(ship_rect)
bullets.append(bullet)
bullet = create_bullet(ship_rect)
bullet_color = (120, 50, 50)

while True: # 무한루프 > if로 탈출
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 중첩 : 다운일때만 해라
                ship_rect.left -= 60
            elif event.key == pygame.K_RIGHT:
                ship_rect.right += 60
            elif event.key == pygame.K_UP:
                ship_rect.top -= 60
            elif event.key == pygame.K_DOWN:
                ship_rect.top += 60
                if ship_rect.top + ship_rect.height == screen_rect.bottom:
                    ship_rect.bottom -= 60
            elif event.key == pygame.K_SPACE:
                bullets.append(create_bullet(ship_rect))
            #raise SystemExit

    # Do logical updates here. / 업데이트 비행기, 위치,,
    # ...
    new_bullets = []
    for bullet in bullets:
        bullet.top -= 10
        if screen_rect.top < bullet.top:
            bullet.top -= 1
            new_bullets.append(bullet)

    screen.fill("grey")  # Fill the display with a solid color / 디폴트는 까만색

    # Render the graphics here. / 비행기, 적, 총알,,, 점수 등 화면에 표시될 여러가지 랜더링
    # ...
    

    screen.blit(image, ship_rect) #네모의 위치에다가 뿌려라
    #screen.blit(image, image.get_lect())
    pygame.draw.rect(screen, bullet_color, bullet)


    pygame.display.flip()  # Refresh on-screen display / 플립:뒤집다 > 왜 뒤집지 > 위아래변경 > 뭔가동작을?끝내고? 새로 그리는?? > 리프레쉬될때 자연스럽게 나오게 60fps
    clock.tick(60) #이런것도 60드래그 > 리팩터 > 변수추출 > FPS로 바꾸면 코드가 깔끔해지지 # wait until next frame (at 60 FPS) / 초당 그림을 60장 그린다 / 한번돌떄 얼만큼 움직이냐

# 이 코드에서 image는 비행기 이미지를 나타내며, screen은 게임 창을 나타냅니다. 
# screen.blit(image, image_rect) 부분에서 blit 함수는 이미지를 화면에 그리는 데 사용됩니다. 이 함수는 두 가지 요소를 필요로 합니다:
# 이미지 (image): 화면에 그릴 이미지입니다. 이 경우에는 비행기 이미지인 image 변수입니다.
# 위치 (position): 이미지가 화면에 그려질 위치를 나타냅니다. 이 위치는 일반적으로 좌표 (x, y)로 지정되는데, 여기서는 이미지의 사각형 정보를 사용합니다.
# screen.blit() 함수는 image를 screen에 그립니다. image_rect는 이미지의 위치와 크기를 나타내는 사각형(rectangle)입니다.
#따라서 screen.blit(image, image_rect) 코드는 비행기 이미지를 screen에 그리는데, 이 때 image_rect에 지정된 위치와 크기에 맞춰서 그립니다.
# 이로써 게임 루프가 반복될 때마다 비행기 이미지가 지정된 위치에 그려지게 됩니다.