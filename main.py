import pygame
from background import backg
import bodies

# pygame initialisation variables
pygame.init()
screen_width = 1480
screen_height = 780
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# scaling variables
distance_scale = 7.5e8
time_scale = 60 * 60 * 24 * 10  # (1 real second = 1 simulated day) * multiplier
substeps = 100

# stars generate the white dots(stars) as the background
stars = [backg(screen, screen_width, screen_height) for _ in range(300)]

# our list containing bodies, can be changed for diffrent simulations
solar_bodies = [bodies.sun, bodies.mercury, bodies.venus, bodies.earth, bodies.mars, bodies.jupiter, bodies.saturn, bodies.uranus, bodies.neptune]

# main loop
while running:

    # check if pygame window is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000  # delta time in seconds
    screen.fill("black")  # fill screen background per frame

    for s in stars:
        s.render()  # render background

    # substeps used for smoother result
    # loops through list of bodies updating their position and rendering them
    for _ in range(substeps):
        for i in solar_bodies:
            i.update(solar_bodies, ((dt * time_scale) / substeps))


    for i in solar_bodies:
        i.render(screen, distance_scale)

    # refresh screen
    pygame.display.flip()

# close screen when run = False
pygame.quit()
