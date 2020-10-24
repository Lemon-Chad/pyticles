import pygame
import random

pygame.init()


class Particle:
    def __init__(self, image, coords: tuple, velocity: tuple, decay_time=5, decay_chance=3):
        self.image = image
        self.coords = coords
        self.velocity = velocity
        self.decay_time = decay_time
        self.decay_chance = decay_chance
        self.time = 0


class Engine:
    def __init__(self):
        self.particles = []

        # Example: [image, coords, velocity, time, decay_time, decay_chance]

    def render(self, screen):
        for particle in self.particles:
            screen.blit(particle[0], particle[1])

    def burst(self, image, pcount, origin, scatter=1, displacement=1):
        for _ in range(pcount):
            self.particles.append(Particle(image,
                                           tuple([x + random.randint(-displacement, displacement) for x in origin]),
                                           (random.randint(-scatter * 10, scatter * 10) / 10,
                                            random.randint(-scatter * 10, scatter * 10) / 10)
                                           ))

    def draw(self, p):
        self.particles.append(p)

    def move(self):
        for particle in self.particles:
            particle.coords = tuple([
                particle.coords[i] + particle.velocity[i] for i in range(2)
            ])

    def decay(self):
        for particle in self.particles:
            particle.time += 1
            random.seed()
            if (particle.time > particle.decay_time and
                random.randint(1, particle.decay_chance) == particle.decay_chance) or \
                    (particle.time > particle.decay_time * 2):
                self.particles.remove(particle)

    def tick(self, screen):
        self.render(screen)
        self.move()
        self.decay()
