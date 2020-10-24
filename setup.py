from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'pyticles',         # How you named your package folder (MyLib)
  packages = ['pyticles'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple particles system for pygame',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'LemonChad',                   # Type in your name
  author_email = 'jakitmationstudios@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Lemon-Chad/pyticles',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Lemon-Chad/pyticles/archive/v_1.0.zip',    # I explain this later on
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