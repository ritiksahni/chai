from setuptools import setup, find_packages

setup(
    name='chai-cli',
    version='0.1',
    author='Ritik Sahni',
    author_email='ritiksahni0203@gmail.com',
    description='AI in your CLI.',
    keywords=['ai', 'openai', 'cli'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai',
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'chai = chai:main',
        ]
    }
)

