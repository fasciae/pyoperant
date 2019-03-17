import pygame, time
from pygame.locals import * #"for easier access to key coordinates"

# heavily adapted from https://realpython.com/pygame-a-primer/

class port(pygame.sprite.Sprite):

    def __init__(self, keyNum, coords):
        super(port, self).__init__()
        self.keybind = keyNum # this takes an int as the input and assigns it to the current square
        self.coords = coords # this takes a tuple and those are where the square will show up
        self.surf = pygame.Surface((100, 100)) #these are the dimensions of the shape
        self.surf.fill((50, 200, 60)) #describes the shape color
        self.rect = self.surf.get_rect() #describes the shape location in coordinates

    def update(self, pressed_keys):
        if(pressed_keys == self.keybind):
            self.surf.fill((255, 255, 255))

    def reset(self):
        self.surf.fill((50, 200, 60))

def redraw(eGroup):
    for entity in eGroup:
        screen.blit(entity.surf, entity.coords)
    pygame.display.flip()

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Variable to keep our main loop running
running = True

# Create the "ports" and pass in the int corresponding to the key you want to trigger it, as well as a tuple with its length and width
lpp = port(276, (150, 200))
cpp = port(274, (350, 200))
rpp = port(275, (550, 200))

ports = pygame.sprite.Group()
ports.add([lpp, cpp, rpp])

redraw(ports)

# Our main loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
            else:
                for thing in ports:
                    thing.update(event.key)
            redraw(ports)
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
    time.sleep(0.1)
    for thing in ports:
        thing.reset()
    redraw(ports)