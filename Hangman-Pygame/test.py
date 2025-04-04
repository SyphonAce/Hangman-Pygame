import pygame_textinput
import pygame
pygame.init()

# Create TextInput-object
manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) <= 1)
textinput = pygame_textinput.TextInputVisualizer(manager)

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 10))

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(30)