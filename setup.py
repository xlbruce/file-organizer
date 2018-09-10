from setuptools import setup

with open('README.md', 'r') as f:
        long_description = f.read()

setup(
    name='file_organizer',
    py_modules=['organize'],
    version='0.2.1',
    description='A file organizer based on file suffixes and user chosen file extensions',
    long_description=long_description,
    author='Gilson de Paula',
    author_email='gilsonsvieira93@gmail.com',
    url='https://github.com/xlbruce/file-organizer',
    license='MIT',
    keywords=['file', 'organizer'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        organize=organize:main
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX",

    ]
)
