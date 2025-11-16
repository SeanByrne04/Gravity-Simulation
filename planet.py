import pygame


class Solar_body:
    def __init__(self, mass, vel, pos, radius, colour):
        self.mass = mass  # mass of body in kg
        self.vel = pygame.math.Vector2(vel)  # initial velocity of body
        self.pos = pygame.math.Vector2(pos)  # initial UNSCALED position of body in meters
        self.radius = radius  # radius of body in pixels, NOT TO SCALE
        self.colour = colour  # colour of body

    def calculate_gravity(self, others):
        G = 6.6743 * (10 ** -11)  # gravitational constant
        acceleration_vector = pygame.math.Vector2(0, 0)  # initail empty vector
        # check self against all other bodies
        for other in others:
            # dosent check self against self as the value will result in a 0 value
            if self == other:
                continue

            vector_between = other.pos - self.pos  # create vector between
            magnitude = vector_between.length()  # find magnitude of vector between (distance between bodies)

            # if bodies in same place their gravity equates to 0, so skip
            if magnitude == 0:
                continue

            direction = vector_between.normalize()  # finds direction
            scalar_acceleration = (G * other.mass) / (magnitude ** 2) # calculate acceleration without direction
            acceleration_vector += direction * scalar_acceleration  # combine direction and acceleration vectors

        return acceleration_vector

    def update(self, others, time):
        # calculate gravity and apply position and velocity changes
        acceleration = self.calculate_gravity(others)
        self.vel += acceleration * time  # calculate velocity (note:we use scaled time here)
        self.pos += self.vel * time

    def render(self, screen, distance_scale):
        # scale down all objects then render on screen
        scaled = (self.pos / distance_scale) + pygame.math.Vector2(
            screen.get_width() / 2,
            screen.get_height() / 2
        )
        pygame.draw.circle(screen, self.colour, scaled, self.radius)
