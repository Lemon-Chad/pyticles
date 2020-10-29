from distutils.core import setup

setup(
  name = 'pyticles',         # How you named your package folder (MyLib)
  packages = ['pyticles'],   # Chose the same as "name"
  version = '1.0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple particles system for pygame',   # Give a short description about your library
  long_description='''
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

  ''',
  long_description_content_type="text/markdown",
  author = 'LemonChad',                   # Type in your name
  author_email = 'jakitmationstudios@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Lemon-Chad/pyticles',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Lemon-Chad/pyticles/archive/v_1.0.2.zip',    # I explain this later on
  keywords = ['python', 'particles', 'pygame'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pygame',
          'random'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)