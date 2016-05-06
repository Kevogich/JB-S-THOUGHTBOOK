from distutils.core import setup

setup(name='Thought Book',
      version='1.0',
      description='Collect your thoughts and events',
      author='Jackline Kimani',
      author_email='wangarikim41@gmail.com',
      install_requires=[
        'docopt>=0.6.2',
        'Sqlite3',
    ],
      classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
      url='https://github.com/JackyKimani/bc-7-JournalConsoleApp',
      packages=['distutils', 'distutils.command'],
     )