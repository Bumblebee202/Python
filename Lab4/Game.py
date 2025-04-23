import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пінг-понг")

# Кольори
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифти
FONT = pygame.font.Font(None, 36)

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dy):
        self.rect.y += dy
        # Обмеження руху по вертикалі
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class PlayerPaddle(Paddle):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def update(self):
        mouse_y = pygame.mouse.get_pos()[1]
        self.rect.centery = mouse_y
        # Обмеження руху по вертикалі
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class BotPaddle(Paddle):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.speed = 3

    def update(self, ball):
        if ball.dy > 0:  # М'яч летить вниз
            if self.rect.centery < ball.rect.centery:
                self.move(self.speed)
            else:
                self.move(-self.speed)
        elif ball.dy < 0:  # М'яч летить вгору
            if self.rect.centery > ball.rect.centery:
                self.move(-self.speed)
            else:
                self.move(self.speed)
        # Обмеження руху по вертикалі
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.dx = 5 * random.choice((1, -1))
        self.dy = 5 * random.choice((1, -1))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Відбиття від верхньої та нижньої стінок
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

class Game:
    def __init__(self):
        self.player = PlayerPaddle(50, HEIGHT // 2 - 50, 10, 100, BLUE)
        self.bot = BotPaddle(WIDTH - 60, HEIGHT // 2 - 50, 10, 100, RED)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2, 10, WHITE)
        self.player_score = 0
        self.bot_score = 0

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Оновлення
            self.player.update()
            self.bot.update(self.ball)
            self.ball.update()

            # Перевірка зіткнення м'яча з ракетками
            if self.ball.rect.colliderect(self.player.rect) or self.ball.rect.colliderect(self.bot.rect):
                self.ball.dx *= -1

            # Перевірка виходу м'яча за межі екрану
            if self.ball.rect.left < 0:
                self.bot_score += 1
                self.reset_ball()
            elif self.ball.rect.right > WIDTH:
                self.player_score += 1
                self.reset_ball()

            # Відображення
            screen.fill(BLACK)
            self.player.draw(screen)
            self.bot.draw(screen)
            self.ball.draw(screen)

            # Відображення рахунку
            player_text = FONT.render(str(self.player_score), True, WHITE)
            bot_text = FONT.render(str(self.bot_score), True, WHITE)
            screen.blit(player_text, (WIDTH // 4, 20))
            screen.blit(bot_text, (WIDTH // 4 * 3, 20))

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

    def reset_ball(self):
        self.ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.ball.dx *= random.choice((1, -1))
        self.ball.dy *= random.choice((1, -1))

if __name__ == "__main__":
    game = Game()
    game.run()