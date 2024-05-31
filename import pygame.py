import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("飞机大战")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 游戏时钟
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 30))
        self.speed_x = 0
    
    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(random.randint(0, screen_width), 0))
        self.speed_y = 2
    
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.kill()

# 创建精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 更新
    all_sprites.update()
    
    # 每隔一段时间生成一个敌机
    if random.randint(0, 100) < 2:  # 控制生成频率
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    
    # 绘制
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # 检测碰撞（这里简化处理，未实现具体碰撞逻辑）
    # collisions = pygame.sprite.spritecollide(player, enemies, True)
    
    # 更新屏幕
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

# 游戏结束，退出pygame
pygame.quit()
sys.exit()