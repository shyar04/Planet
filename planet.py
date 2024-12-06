import pygame
import sys

from pygame.math import Vector2
from random import randrange

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()

windowdim = Vector2(800, 800)
screen = pygame.display.set_mode((int(windowdim.x), int(windowdim.y)))
myFont = pygame.font.SysFont(None, 20)

# 모든 행성들이 저장될 변수
planets = []

# 모드 인덱스
index = 0

class Planet():
    def __init__(self, position, delta=Vector2(0, 0), radius=10, imovable=False):

        # 행성 위치
        self.position = position

        # 행성의 반지름은 중력에 영향을 끼침
        self.radius = radius

        # 행성 속도
        self.delta = delta

        # 행성이 움직이지 않아 고정시키는 지
        self.imovable = imovable

        # 행성 생성 시 planets에 저장
        planets.append(self)

    def process(self):

        # 매 프레임마다 실행
        # 고정된 행성 위에 정착할 시 움직이지 않음
    
        if not self.imovable:
            for i in planets:
                if not i is self:
                    try:
                        # 다른 행성이 고정되어있고 두 행성의 거리가 두 행성의 반지름보다 짧을 경우
                        if i.imovable and self.position.distance_to(i.position) < self.radius + i.radius:
                            self.delta = Vector2(0, 0)
                            self.imovable = True 
                        dir_from_obj  = (i.position - self.position).normalize() * 0.01 * (i.radius / 10)
                        self.delta += dir_from_obj
                    except:
                        print('Same point')
            self.position += self.delta

        # 행성을 해당 위치의 화면에 표시
        pygame.draw.circle(screen, [255, 255, 255], self.position, self.radius)

# Loop
def main():

    # 기본 생성
    Planet(Vector2(400, 400), radius=50, imovable=True)
    Planet(Vector2(400, 200), delta=Vector2(3, 0), radius=10)
    Planet(Vector2(400, 600), delta=Vector2(-3, 0), radius=10)

    while True:
        screen.fill((0, 0, 0))
        myText = myFont.render("Click: Create Planet", True, (255, 255, 255))
        screen.blit(myText, (5, 5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 클릭 시 움직이는 행성의 위치와 속도를 랜덤 지정
            if event.type == pygame.MOUSEBUTTONDOWN:
                randx = randrange(0, 800)
                randy = randrange(0, 800)
                randvelx = randrange(-3, 3)
                randvely = randrange(-3, 3)
                randomrad = randrange(2, 5)
                Planet(Vector2(randx, randy), delta=Vector2(randvelx, randvely), radius=randomrad)

        for p in planets:
            p.process()

        pygame.display.flip()
        fpsClock.tick(fps)

if __name__ == "__main__":
    main()