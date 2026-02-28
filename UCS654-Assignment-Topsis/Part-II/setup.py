from setuptools import setup

setup(
    name="Topsis-Manmeet-102317039",   
    version="0.1",
    py_modules=["topsis"],
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis:main'
        ]
    },
    author="Manmeet",
    description="Simple Topsis implementation for assignment"
)
