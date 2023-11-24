# 导入模块
import pygame
import random
import sys

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 定义窗口大小和格子大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20

# 定义蛇的初始位置和方向
snake = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
         (WINDOW_WIDTH // 2 - CELL_SIZE, WINDOW_HEIGHT // 2),
         (WINDOW_WIDTH // 2 - 2 * CELL_SIZE, WINDOW_HEIGHT // 2)]
direction = "right"

# 定义食物的初始位置
food = (random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
        random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

# 初始化pygame
pygame.init()
# 创建窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 设置窗口标题
pygame.display.set_caption("贪吃蛇")
# 创建时钟对象
clock = pygame.time.Clock()

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        # 如果点击了关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 如果按下了键盘，改变蛇的方向
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

    # 移动蛇
    # 根据方向计算蛇头的新位置
    if direction == "up":
        new_head = (snake[0][0], snake[0][1] - CELL_SIZE)
    elif direction == "down":
        new_head = (snake[0][0], snake[0][1] + CELL_SIZE)
    elif direction == "left":
        new_head = (snake[0][0] - CELL_SIZE, snake[0][1])
    elif direction == "right":
        new_head = (snake[0][0] + CELL_SIZE, snake[0][1])
    # 在蛇的头部插入新位置
    snake.insert(0, new_head)

    # 判断是否吃到食物
    if snake[0] == food:
        # 重新生成食物的位置
        food = (random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    else:
        # 删除蛇的尾部
        snake.pop()

    # 判断是否死亡
    # 如果蛇头超出窗口范围，死亡
    if snake[0][0] < 0 or snake[0][0] >= WINDOW_WIDTH or snake[0][1] < 0 or snake[0][1] >= WINDOW_HEIGHT:
        break
    # 如果蛇头碰到自己的身体，死亡
    if snake[0] in snake[1:]:
        break

    # 绘制画面
    # 填充背景色
    window.fill(BLACK)
    # 绘制食物
    pygame.draw.rect(window, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    # 绘制蛇
    for cell in snake:
        pygame.draw.rect(window, GREEN, (cell[0], cell[1], CELL_SIZE, CELL_SIZE))
    # 更新画面
    pygame.display.update()
    # 设置帧率
    clock.tick(10)

# 游戏结束
pygame.quit()
sys.exit()
