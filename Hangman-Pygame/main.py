import pygame, random, sys, pygame_textinput
pygame.init()



words = [
    # 3-Letter Words
    "cat", "dog", "sun", "box", "car", "bat", "hat", "jam", "map", "pen",
    "run", "red", "net", "log", "cup", "zip", "fog", "bus", "bed", "hot",
    "top", "pop", "win", "fan", "web", "rod", "pot", "key", "ram", "jet",
    "bow", "toy", "gum", "cap", "tap", "pen", "fox", "pig", "hen", "owl",
    "pan", "job", "bug", "tag", "bay", "tin", "jug", "pad", "lap", "fit",
    
    # 4-Letter Words
    "book", "door", "gold", "moon", "rock", "tree", "ship", "sand", "lamp", "wind",
    "ring", "mask", "wave", "cart", "desk", "frog", "ball", "fire", "coin", "bike",
    "rain", "dark", "code", "blue", "clip", "boot", "stop", "barn", "flag", "mask",
    "wave", "band", "seat", "coin", "luck", "key", "lock", "ship", "boat", "leaf",
    "time", "kite", "path", "ring", "task", "life", "mine", "zone", "dove", "tank",
    "nest", "tent", "bolt", "maze", "gear", "grip", "wave", "fish", "cake", "home",
    
    # 5-Letter Words
    "apple", "grape", "plant", "chair", "table", "stone", "heart", "flame", "glass", "smile",
    "clock", "brick", "eagle", "zebra", "flash", "trace", "ocean", "spoon", "shine", "align",
    "crane", "pride", "twist", "blaze", "glove", "frame", "blend", "scout", "store", "flock",
    "plume", "spine", "chase", "drill", "shard", "probe", "fluff", "plank", "match", "crisp",
    "spell", "trace", "slice", "crack", "tread", "flute", "blame", "stack", "bloom", "shift",
    "clown", "tiger", "camel", "sheep", "mouse", "smile", "grasp", "shrub", "swing", "pound",
    "doubt", "plush", "flute", "store", "spare", "crane", "brave", "frail", "swipe", "sharp",
    "blend", "pride", "chase", "carve", "shift", "fluff", "plume", "trace", "shard", "glaze",
    "probe", "straw", "wrist", "flame", "sweep", "clamp", "slant", "plane", "whale", "prism",
    "drake", "flair", "grind", "hoist", "joint", "jolly", "kneel", "latch", "mince", "perch",
    "plush", "quota", "reign", "skate", "trace", "upset", "vivid", "witty", "xenon", "yield",
    "zebra", "badge", "bacon", "brave", "carry", "chest", "clean", "crash", "curve", "dance",
    "ditch", "drain", "feast", "flock", "glory", "hover", "joint", "kneel", "latch", "loyal",
    "mount", "nerve", "pouch", "prism", "pulse", "quail", "reset", "seize", "shift", "spear",
    "split", "stomp", "swirl", "tease", "throw", "token", "trend", "trust", "twirl", "uncle",
    "vivid", "whirl", "witty", "zesty", "acute", "blaze", "crane", "frame", "glaze", "probe",
    "slice", "straw", "wrist", "sharp", "shift", "swipe", "flame", "trace", "pride", "blaze",
    "blend", "fluff", "plume", "glaze", "probe", "sharp", "trace", "blend", "glaze", "swipe"
]

#Setting size of game window
WNDW_HEIGHT = 800
WNDW_WIDTH = 600
screen = pygame.display.set_mode((WNDW_HEIGHT, WNDW_WIDTH))

text_font = pygame.font.SysFont("Arial", 20)

# Other game settings
title = pygame.display.set_caption("Dangle Guy")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
# Variables
NooseX = 160
NooseY = 0

lineImg = pygame.image.load("line.png")
LineX = -140

random_word = random.choice(words)
answer = random_word
print(answer)

manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) == 1)

correct_user_inputs = set()
wrong_user_inputs = set()

# Functions
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def noose(x,y):
    if len(wrong_user_inputs) == 0:
        nooseImg = pygame.image.load("Noose.png")
    if len(wrong_user_inputs) == 1:
        nooseImg = pygame.image.load("Stage1.png")
    if len(wrong_user_inputs) == 2:
        nooseImg = pygame.image.load("Stage2.png")
    if len(wrong_user_inputs) == 3:
        nooseImg = pygame.image.load("Stage3.png")
    if len(wrong_user_inputs) == 4:
        nooseImg = pygame.image.load("Stage4.png")
    if len(wrong_user_inputs) == 5:
        nooseImg = pygame.image.load("Stage5.png")
    if len(wrong_user_inputs) == 6:
        nooseImg = pygame.image.load("Stage6.png")
        reset()

    nooseImg = pygame.transform.scale2x(nooseImg)
    screen.blit(nooseImg, (x,y))

def line(x,y):
    screen.blit(lineImg, (x,y))

def reset():
    global answer
    correct_user_inputs.clear()
    wrong_user_inputs.clear()
    answer = random.choice(words)
    print(answer)
# Game Loop
while True: 

    screen.fill((255, 255, 255))

    draw_text("Enter a Letter or Word Below (LOWER CASE ONLY)", text_font, (0, 0, 0), 180, 480)

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    textinput = pygame_textinput.TextInputVisualizer(manager)
    screen.blit(textinput.surface, (340 , 520))
    textinput.update(events)


    pressed = pygame.key.get_pressed()
    # Draws correct letter in correct slot in the word
    for i, letter in enumerate(answer):
        if letter in correct_user_inputs:
            draw_text(letter, text_font, (0, 0, 0), 120 * i + 200, 390)
    # Checks for the enter key getting pressed and will reset if correct or if wrong
    if pressed[pygame.K_RETURN]:
        if textinput.value:
            if textinput.value in answer:
                correct_user_inputs.add(textinput.value)
                textinput.value = ""
                if len(correct_user_inputs) == len(answer):
                    reset()
            else:
                wrong_user_inputs.add(textinput.value)
                textinput.value = ""
    # for letter in answer:
    #     LineX += 120
    #     line(LineX, 230)
    #     print(LineX)


    noose(NooseX, NooseY)
    # Draws lines based on length of answer
    line(-140, 230)
    if len(answer) == 3:
        line(-20, 230)^^^^^^^^^
        line(100, 230)
    elif len(answer) == 4:
        line(-20, 230)
        line(100, 230)
        line(220, 230)
    else:
        line(-20, 230)
        line(100, 230)
        line(220, 230)
        line(340, 230)

    line(40, 360)

    pygame.display.update() # Updates screen
