#Test Test
import pygame
import random
import time

# Initial parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 1000
pygame.font.init()
font = pygame.font.Font(None, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)

# Player class
class player(pygame.sprite.Sprite):
    def __init__(self):
        # Define initial parameters
        self.color = BLUE
        self.width = 50
        self.height = 100
        self.vel = 50
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position  (INTS!)
        self.rect.x = SCREEN_WIDTH // 2 - self.width // 2
        self.rect.y = SCREEN_HEIGHT - self.height

    # Move the block depending on keyboard input
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vel

        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.vel

# Traffic class
class traffic(pygame.sprite.Sprite):
    def __init__(self, color, width, height, vel, increment):
        # Define initial parameters
        self.color = color
        self.width = width
        self.height = height
        self.vel = vel
        self.vel_increment = increment

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Set the initial position  (INTS! volle Breite, Start oberhalb)
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.rect.y = -self.height

    # Move traffic along the screen
    def move(self):
        self.rect.y += self.vel
        # If traffic has moved to the bottom reset it to the top
        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.y = -self.height
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.width)
            # Speed up traffic
            self.vel += self.vel_increment

# Traffic subtype car
class car(traffic):
    def __init__(self):
        self.color = RED
        self.width = 60
        self.height = 100
        self.vel = 20
        self.vel_increment = 2
        super(car, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)

# Traffic subtype truck
class truck(traffic):
    def __init__(self):
        self.color = ORANGE
        self.width = 100
        self.height = 150
        self.vel = 10
        self.vel_increment = 5
        super(truck, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)

# Display 'game over'
def game_over(win):
    win.fill((255, 0, 0))
    text_surface = font.render("Game Over", True, WHITE)
    win.blit(text_surface, (int(SCREEN_WIDTH * 0.4), int(SCREEN_HEIGHT * 0.5)))
    pygame.display.flip()

def run():
    pygame.init()

    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Traffic Game")
    clock = pygame.time.Clock()

    # Initialize player and traffic
    player1 = player()
    traffic1 = car()
    traffic2 = truck()

    # Create sprite groups
    all_traffic = pygame.sprite.Group(traffic1, traffic2)
    all_sprites = pygame.sprite.Group(player1, traffic1, traffic2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move all objects
        for sprite in all_sprites:
            if hasattr(sprite, "move"):
                sprite.move()

        # Collision check
        if pygame.sprite.spritecollideany(player1, all_traffic):
            game_over(win)
            time.sleep(2)
            running = False  # <-- sauber beenden
        else:
            win.fill(BLACK)
            all_sprites.draw(win)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    run()
