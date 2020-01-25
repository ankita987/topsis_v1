from distutils.core import setup

setup(
  name = 'topsis',
  packages = ['topsis'],
  version = '0.1',
  license='MIT', 
  description = 'Calculates the topsis score from all int and float columns in data and returns a dictionary containing ranks and topsis_scores of all rows.',
  author = 'Ankita',
  author_email = 'ankitauppal99@gmail.com',
  url = 'https://github.com/ankita987/topsis,
  download_url = 'https://github.com/ankita987/topsis/archive/v_01.tar.gz',
  keywords = ['TOPSIS'],
  install_requires=[
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)