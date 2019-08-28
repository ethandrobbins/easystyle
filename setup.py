from distutils.core import setup
setup(
  name = 'deduplicate',
  packages = ['deduplicate'],
  version = '0.3',
  license='MIT',
  description = 'Deduplication of csv files using predicate blocking and fuzzy matching',
  author = 'Ethan Robbins',
  author_email = 'ethan.d.robbins@gmail.com',
  url = 'https://github.com/ethandrobbins',
  download_url = 'https://github.com/ethandrobbins/deduplicate/archive/v_03.tar.gz',    # I explain this later on
  keywords = ['DEDUPLICATE', 'FUZZY MATCHING', 'PREDICATE BLOCKING'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'fuzzywuzzy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',    'License :: OSI Approved :: MIT License',   # Again, pick a license    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)