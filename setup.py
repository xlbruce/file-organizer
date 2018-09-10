from setuptools import setup

setup(
    name='file_organizer',
    py_modules=['organize'],
    version='0.2.0',
    description='A file organizer based on file suffixes and user chosen file extensions',
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
)
