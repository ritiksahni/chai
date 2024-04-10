from setuptools import setup, find_packages

setup(
    name='chai',
    version='0.1',
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

