from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='chai-cli',
    version='0.2',
    author='Ritik Sahni',
    author_email='ritiksahni0203@gmail.com',
    description='AI in your CLI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
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

