from setuptools import setup

setup(
  name = 'easystyle',         # How you named your package folder (MyLib)
  packages = ['easystyle'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library that allows the user to quickly analyze data at a basic level without exporting to excel',   # Give a short description about your library
  author = 'Ethan Robbins',                   # Type in your name
  author_email = 'ethan.d.robbins@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ethandrobbins/easystyle',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ethandrobbins/easystyle/archive/v_1_0.tar.gz',    # I explain this later on
  keywords = ['STYLE', 'PANDAS', 'DATA'],   # Keywords that define your package best
  install_requires=[
          'numpy',
          'pandas',
          'seaborn',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
      ],
)