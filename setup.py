import sys
from setuptools import setup


if float("%d.%d" % sys.version_info[:2]) < 3.0:
    sys.stderr.write(
        "Your Python version %d.%d.%d is not supported.\n"
        % sys.version_info[:3])
    sys.stderr.write("Requires Python higher than 3.0.\n")
    sys.exit(1)


setup(
    name='line-counter',
    version='0.7',
    author='HarpSun',
    author_email='dilras0@gmail.com',
    url='https://github.com/HarpSun/Line-Counter',
    packages=['line_counter'],
    entry_points={
        'console_scripts': [
            'lc=line_counter.line_counter:main',
        ],
    },
)
