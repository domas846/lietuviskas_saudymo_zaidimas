import pygame
import random

# Inicializuojame Pygame
pygame.init()

# Nustatymai
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Sukuriame langą
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Šaudymo Nuotykiai")

# Žaidėjo klasė
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.clamp_ip(screen.get_rect())  # Neleisk judėti už ekrano ribų

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Kulka klasė
class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Žaidimas
def main():
    clock = pygame.time.Clock()
    player = Player()
    bullets = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            player.move(1, 0)
        if keys[pygame.K_UP]:
            player.move(0, -1)
        if keys[pygame.K_DOWN]:
            player.move(0, 1)
        if keys[pygame.K_SPACE]:
            bullets.append(Bullet(player.rect.centerx, player.rect.top))

        # Atnaujiname kulkas
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        # Braižome
        screen.fill(WHITE)
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
