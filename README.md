# Pyticles

Pyticles is a particle system for pygame. It allows you to render particles with velocity and decay rates.

# Classes

Pyticles includes two classes.

  - Particle(image, screen_coords, velocity, decay_time=5, decay_chance=3)
  - Engine()
 
These are what the system is based around.

# Particles

Particles are simply a class that represents a single particle.
 - Image is the particle texture. 
 - Screen coordinates represent the position on the screen. 
 - Velocity is how far the particles will go every time the Engine ticks.
 - Decay time is how many Engine ticks until the particle has a chance to decay ( 1 in decay_chance ). Once there has been twice as many ticks as decay time, the particle will instantly decay.

# Engines
 
Engines contain sets of particles and have 6 functions. You will only need to use 3. The functions are:
 
 - burst(image, particle_count, origin, scatter=1, displacement=1)
 - draw(particle)
 - tick(surface)

Burst releases a burst of particles at a certain point, marked origin. 
 - Scatter is how high the velocity in a certain direction can be.
 - Particle count is how many particles are released. 
 - Displacement is the furthest away a particle can spawn from the origin. 
 - Image is the particle texture.

Draw will create a single particle, and it takes in a particle class.

Tick takes in a surface to draw to and manage all tasks such as velocity, decay, and drawing.
