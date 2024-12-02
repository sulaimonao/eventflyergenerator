from setuptools import setup, find_packages

setup(
    name='event-flyer-generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'openai',
        'jinja2',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'event-flyer-generator=src.app:main',
        ],
    },
    author='Your Name',
    description='Generate event flyers from text input.',
    url='https://github.com/yourname/event-flyer-generator',
)
