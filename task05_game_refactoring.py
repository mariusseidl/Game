import pygame
import random
import time

# Initial parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 750
pygame.font.init()
font = pygame.font.Font(None, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 255)

# Possible game states
class GameState:
    MENU = "menu"
    PLAYING_LEVEL1 = "playing_level1"
    PLAYING_LEVEL2 = "playing_level2"
    MULTIPLAYER = "multiplayer"
    GAME_OVER = "game_over"
    SWITCH_THEME = "switch_theme"
    EXIT = "exit"

class Level2State:
    LEVEL_V = 1
    LEVEL_H = 2

class ThemeStates:
    LIGHT = "light"
    DARK = "dark"

    
# Player class
class Player(pygame.sprite.Sprite):
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

        # Set the initial position
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - self.height

    # Move the block depending on keyboard input
    def move(self):
        # Get keyboard input
        keys = pygame.key.get_pressed()

        # Move to the left if it's not on the leftmost side
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.vel

        # Move to the right if it's not on the rightmost side
        elif keys[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.vel

# Player class
class PlayerXY(pygame.sprite.Sprite):
    def __init__(self):
        # Define initial parameters
        self.color = BLUE
        self.width = 50
        self.height = 50
        self.vel = 50

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - self.height

    # Move the block depending on keyboard input
    def move(self):
        # Get keyboard input
        keys = pygame.key.get_pressed()

        # Move to the left if it's not on the leftmost side
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.vel

        # Move to the right if it's not on the rightmost side
        elif keys[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.vel
        
        # Move to the top if it's not on the uppermost side
        elif keys[pygame.K_UP]:
            if self.rect.top > 0: 
                self.rect.y -= self.vel
        
        # Move to the bottom if it's not on the bottommost side        
        elif keys[pygame.K_DOWN]:
            if self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += self.vel

# Player class
class PlayerKeys(pygame.sprite.Sprite):
    def __init__(self):
        # Define initial parameters
        self.color = GREEN
        self.width = 50
        self.height = 50
        self.vel = 50

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - self.height

    # Move the block depending on keyboard input
    def move(self):
        # Get keyboard input
        keys = pygame.key.get_pressed()

        # Move to the left if it's not on the leftmost side
        if keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= self.vel

        # Move to the right if it's not on the rightmost side
        elif keys[pygame.K_d]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.vel
        
        # Move to the top if it's not on the uppermost side
        elif keys[pygame.K_w]:
            if self.rect.top > 0: 
                self.rect.y -= self.vel
        
        # Move to the bottom if it's not on the bottommost side        
        elif keys[pygame.K_s]:
            if self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += self.vel

                
# Traffic class (vertical movement)
class Traffic(pygame.sprite.Sprite):
    def __init__(self, color, width, height, vel, increment):
        # Define initial parameters
        self.color = color
        self.width = width
        self.height = height
        self.vel = vel
        self.vel_increment = increment

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = random.randint(self.width / 2, SCREEN_WIDTH - self.width / 2)
        self.rect.y = self.height

    # Move traffic along the screen
    def move(self):
        self.rect.y += self.vel
        # If traffic has moved to the bottom reset it to the top
        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(self.width / 2, SCREEN_WIDTH - self.width / 2)
            # Speed up traffic
            self.vel += self.vel_increment

# TrafficX class (horizontal movement)
class TrafficX(pygame.sprite.Sprite):
    def __init__(self, color, width, height, vel, increment):
        # Define initial parameters
        self.color = color
        self.width = width
        self.height = height
        self.vel = vel
        self.vel_increment = increment

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = SCREEN_WIDTH 
        self.rect.y = random.randint(self.height / 2, SCREEN_HEIGHT - self.height / 2) 

    # Move traffic along the screen
    def move(self):
        self.rect.x -= self.vel #move to left
        # If traffic has moved to the left reset it to the right
        if self.rect.left <0: 
            self.rect.y = random.randint(self.height / 2, SCREEN_HEIGHT - self.height / 2)
            self.rect.x = SCREEN_WIDTH 
            # Speed up traffic
            self.vel += self.vel_increment                
                
# Traffic subtype car
class Car(Traffic):
    def __init__(self):
        # Define initial parameters
        self.color = RED
        self.width = 60
        self.height = 100
        self.vel = 20
        self.vel_increment = 2
        super(Car, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)


# Traffic subtype truck
class Truck(Traffic):
    def __init__(self):
        # Define initial parameters
        self.color = ORANGE
        self.width = 100
        self.height = 150
        self.vel = 10
        self.vel_increment = 5
        super(Truck, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)

# TrafficX subtype car
class CarX(TrafficX):
    def __init__(self):
        # Define initial parameters
        self.color = RED
        self.width = 100
        self.height = 60 
        self.vel = 20
        self.vel_increment = 2
        super(CarX, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)

# TrafficX subtype truck
class TruckX(TrafficX):
    def __init__(self):
        # Define initial parameters
        self.color = ORANGE
        self.width = 150
        self.height = 110
        self.vel = 10
        self.vel_increment = 5
        super(TruckX, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)


# Traffic subtype colored truck
class TruckColored(Traffic):
    def __init__(self, color):
        # Define initial parameters
        self.color = color
        self.width = 150
        self.height = 110
        self.vel = 10
        self.vel_increment = 5
        super(TruckColored, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)

# Traffic subtype colored car
class CarColored(Traffic):
    def __init__(self, color):
        # Define initial parameters
        self.color = color
        self.width = 100
        self.height = 60 
        self.vel = 20
        self.vel_increment = 2
        super(CarColored, self).__init__(self.color, self.width, self.height, self.vel, self.vel_increment)

# Abstract Factory Pattern
class ThemeFactory:
    def create_button(self, text,x_pos, y_pos, game_state):
        pass

class LightThemeFactory(ThemeFactory):
    def create_button(self, text,x_pos, y_pos, game_state):
        return LightButton(text,x_pos, y_pos, game_state)

    def create_window(self, width, heigth):
        return LightWindow(width, heigth)

class DarkThemeFactory(ThemeFactory):
    def create_button(self, text,x_pos, y_pos, game_state):
        return DarkButton(text,x_pos, y_pos,  game_state)

    def create_window(self, width, heigth):
        return DarkWindow(width, heigth)

# Abstract Product
class Window():
    def __init__(self, width, height):
        # Define initial parameters
        self.width = width
        self.height = height

    def get_window(self):
        win = pygame.display.set_mode((self.width, self.height))
        return win

    def draw_window(self, window):
        window.fill(self.get_color())
        return window

    def get_color():
        pass 

# Concrete Products
class DarkWindow(Window):
    def get_color(self):
        return (0,0,0)

class LightWindow(Window):
    def get_color(self):
        return (255,255,255)

# Abstract Product
class Button(pygame.sprite.Sprite):
    def __init__(self, text, x_pos, y_pos, game_state):
        # Define initial parameters
        self.text = text
        self.width = 400
        self.height = 100
        self.game_state = game_state

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = x_pos
        self.rect.y = y_pos

    def init_looks(self):
        self.image.fill(self.get_color())
        self.font = self.get_font()
        self.textSurf = self.font.render(self.text, 1, self.get_text_color())
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.width/2 - W/2, self.height/2 - H/2])

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())  

    def get_color(self):
        pass

    def get_text_color(self):
        pass
    
    def get_font(self):
        pass

    def action(self):
        pass

# Concrete Products
class LightButton(Button):
    def get_color(self):
        return (235,235,235)

    def get_text_color(self):
        return (0,0,0)
    
    def get_font(self):
        return pygame.font.SysFont("Arial", 20)

    def action(self):
        return self.game_state

class DarkButton(Button):
    def get_color(self):
        return (20,20,20)

    def get_text_color(self):
        return (255,255,255)
    
    def get_font(self):
        return pygame.font.SysFont("Sans", 20)

    def action(self):
       return self.game_state

# Display 'game over'
def game_over(win):
    win.fill((255, 0, 0))
    text_surface = font.render("Game Over", True, WHITE)
    win.blit(text_surface, (SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.5))
    pygame.display.flip()

# Display instructions for multiplayer mode
def multiplayer_screen(win):
    player_1 = font.render("Player1:", True, WHITE)
    player_1_color = font.render("Color - Blue", True, WHITE)
    player_1_keys = font.render("Keys - Arrow Keys", True, WHITE)
    player_1_traffic = font.render("Traffic - Red", True, WHITE)

    player_2 = font.render("Player2:", True, WHITE)
    player_2_color = font.render("Color - Green", True, WHITE)
    player_2_keys = font.render("Keys - WASD", True, WHITE)
    player_2_traffic = font.render("Traffic - Orange", True, WHITE)

    win.blit(player_1, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.1))
    win.blit(player_1_color, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.2))
    win.blit(player_1_keys, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.3))
    win.blit(player_1_traffic, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.4))

    win.blit(player_2, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.6))
    win.blit(player_2_color, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.7))
    win.blit(player_2_keys, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.8))
    win.blit(player_2_traffic, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.9))
    pygame.display.flip()

# Display menu with options to start or quit the game
def game_menu(win):
    #win.fill((0, 0, 0))
    text_surface = font.render("Game Menu", True, WHITE)
    win.blit(text_surface, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.3))

    start_surface = font.render("Press 1 to start level 1", True, WHITE)
    win.blit(start_surface, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.4))

    start_surface = font.render("Press 2 to start level 2", True, WHITE)
    win.blit(start_surface, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.5))

    multiplayer_surface = font.render("Press M for mutliplayer", True, WHITE)
    win.blit(multiplayer_surface, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.6))
    
    quit_surface = font.render("Press ESC to quit", True, WHITE)
    win.blit(quit_surface, (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.7))
    pygame.display.flip()

# init the menus using the theme factory to create buttons and window
def init_menu(theme):
    theme_factory = LightThemeFactory()
    if theme == ThemeStates.DARK:
        theme_factory = DarkThemeFactory()

    buttons = [theme_factory.create_button("Start level 1", SCREEN_WIDTH *0.15, SCREEN_HEIGHT  * 0.1, GameState.PLAYING_LEVEL1),
               theme_factory.create_button("Start level 2", SCREEN_WIDTH *0.15, SCREEN_HEIGHT *0.3, GameState.PLAYING_LEVEL2),
               theme_factory.create_button("Mutliplayer", SCREEN_WIDTH *0.15, SCREEN_HEIGHT *0.5, GameState.MULTIPLAYER),
               theme_factory.create_button("Switch Theme", SCREEN_WIDTH *0.15, SCREEN_HEIGHT *0.7, GameState.SWITCH_THEME),
               theme_factory.create_button("Exit", SCREEN_WIDTH *0.15, SCREEN_HEIGHT *0.9, GameState.EXIT)]

    window = theme_factory.create_window(SCREEN_WIDTH, SCREEN_HEIGHT)

    button_sprites = pygame.sprite.Group()
    button_sprites.add(buttons)
    return button_sprites, window

def init_game_level1():
     # Initialize player and traffic
    player1 = Player()
    traffic1 = Car()
    traffic2 = Truck()

    # Create sprite groups
    all_traffic = pygame.sprite.Group()
    all_traffic.add(traffic1)
    all_traffic.add(traffic2)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(traffic1)
    all_sprites.add(traffic2)

    return player1, all_traffic, all_sprites

def init_game_level2():
     # Initialize player and traffic
    player1 = PlayerXY()
    traffic1y = Car()
    traffic2y = Truck()
    traffic1x = CarX()
    traffic2x = TruckX()
    
    # Create sprite groups
    all_trafficY = pygame.sprite.Group()
    all_trafficY.add(traffic1y)
    all_trafficY.add(traffic2y)

    all_trafficX = pygame.sprite.Group()
    all_trafficX.add(traffic1x)
    all_trafficX.add(traffic2x)
    
    all_spritesY = pygame.sprite.Group()
    all_spritesY.add(player1)
    all_spritesY.add(traffic1y)
    all_spritesY.add(traffic2y)

    all_spritesX = pygame.sprite.Group()
    all_spritesX.add(player1)
    all_spritesX.add(traffic1x)
    all_spritesX.add(traffic2x)
    
    return player1, all_trafficY, all_trafficX, all_spritesY, all_spritesX

def init_game_multiplayer():
    # Initialize player and traffic
    player1 = PlayerXY()
    player2 = PlayerKeys()
    traffic_car1 = CarColored(RED)
    traffic_truck1 = TruckColored(RED)
    traffic_car2 = CarColored(ORANGE)
    traffic_truck2 = TruckColored(ORANGE)

    # Create sprite groups
    traffic1 = pygame.sprite.Group()
    traffic1.add(traffic_car1)
    traffic1.add(traffic_truck1)

    traffic2 = pygame.sprite.Group()
    traffic2.add(traffic_car2)
    traffic2.add(traffic_truck2)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(traffic_car1)
    all_sprites.add(traffic_truck1)
    all_sprites.add(traffic_car2)
    all_sprites.add(traffic_truck2)

    return player1, player2, traffic1, traffic2, all_sprites    


# Run the game
def run():
    # Initialize pygame
    pygame.init()

    # Set display
    #win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set clock
    clock = pygame.time.Clock()
    start_time = None
    
    FONT_LEVEL = pygame.font.SysFont("Sans", 20)
    
    TIME_LEVEL = 3000


    # Initialize Game state
    game_state = GameState.MENU
    level_state = 0
    count = 0
    theme = ThemeStates.LIGHT

    # initialize buttons and window
    buttons, window = init_menu(theme)
    win = window.get_window()

    # Run the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle game state transitions
        if game_state == GameState.MENU:
            # display menu
            while(game_state == GameState.MENU):
                win = window.draw_window(win)
                for button in buttons:
                    button.init_looks()
                buttons.draw(win)
                ev = pygame.event.get()

                # proceed events
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        for button in buttons:
                            if button.is_clicked():
                                game_state = button.action()

                pygame.display.flip()
                clock.tick(30)

            if game_state == GameState.SWITCH_THEME:
                if theme == ThemeStates.LIGHT:
                    theme = ThemeStates.DARK
                else:
                    theme = ThemeStates.LIGHT
                buttons, window = init_menu(theme)
                game_state = GameState.MENU
            
            if game_state == GameState.PLAYING_LEVEL1:
                #init game
                player1, all_traffic, all_sprites = init_game_level1()
            
            if game_state == GameState.PLAYING_LEVEL2:
                #init game
                player1, all_trafficY, all_trafficX, all_spritesY, all_spritesX = init_game_level2()      
            
            if game_state == GameState.MULTIPLAYER:
                win = window.draw_window(win)
                multiplayer_screen(win)
                time.sleep(5)
                #init game
                player1, player2, traffic1, traffic2, all_sprites = init_game_multiplayer()    
            
            if game_state == GameState.EXIT:
                running = False
                
        elif game_state == GameState.PLAYING_LEVEL1:
            # Move all objects
            for sprite in all_sprites:
                sprite.move()

            # If player and traffic collide, display game over screen
            collision = pygame.sprite.spritecollideany(player1, all_traffic)
            if collision:
                # collision --> game over
                game_state = GameState.GAME_OVER

            else:
                # no collision --> draw all objects
                win = window.draw_window(win)
                all_sprites.draw(win)

        elif game_state == GameState.PLAYING_LEVEL2:
            
            if Level2State.LEVEL_V == (level_state % 3):
                # Move all objects
                for sprite in all_spritesY:
                    sprite.move()
    
                # If player and traffic collide, display game over screen
                collision = pygame.sprite.spritecollideany(player1, all_trafficY)
                if collision:
                    # collision --> game over
                    game_state = GameState.GAME_OVER
    
                else:
                    # no collision --> draw all objects
                    win = window.draw_window(win)
                    all_spritesY.draw(win)

                if start_time:
                    time_since_switch = pygame.time.get_ticks() - start_time
                    message = 'Round: {} Time: {} ms'.format(count,(time_since_switch))
                    win.blit(FONT_LEVEL.render(message, True, RED), (20, 20))
                    if time_since_switch > TIME_LEVEL:
                        count += 1
                        level_state += 1
                        start_time = pygame.time.get_ticks()
                        
            elif Level2State.LEVEL_H == (level_state % 3):
                # Move all objects
                for sprite in all_spritesX:
                    sprite.move()
    
                # If player and traffic collide, display game over screen
                collision = pygame.sprite.spritecollideany(player1, all_trafficX)
                if collision:
                    # collision --> game over
                    game_state = GameState.GAME_OVER
    
                else:
                    # no collision --> draw all objects
                    win = window.draw_window(win)
                    all_spritesX.draw(win)
                    
                if start_time:
                    time_since_switch = pygame.time.get_ticks() - start_time
                    message = 'Round: {} Time: {} ms'.format(count,(time_since_switch))
                    win.blit(FONT_LEVEL.render(message, True, RED), (20, 20))
                    if time_since_switch > TIME_LEVEL:
                        count += 1
                        level_state += 1
                        start_time = pygame.time.get_ticks()
                    
            else:
                level_state += 1
                start_time = pygame.time.get_ticks()
                
        elif game_state == GameState.MULTIPLAYER:
            # Move all objects
            for sprite in all_sprites:
                sprite.move()

            # If player and traffic collide, display game over screen
            collision1 = pygame.sprite.spritecollideany(player1, traffic1)
            collision2 = pygame.sprite.spritecollideany(player2, traffic2)
            if collision1 or collision2:
                # collision --> game over
                game_state = GameState.GAME_OVER

            else:
                # no collision --> draw all objects
                win = window.draw_window(win)
                all_sprites.draw(win)
                    
        elif game_state == GameState.GAME_OVER:
            # display game over screen
            game_over(win)
            time.sleep(2)
            game_state=GameState.MENU
            start_time = None
            level_state = 0
            count = 0

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    run()
   
