import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pico",
    version="0.1.0",
    license="MIT",
    author="Ewerton Carlos Assis",
    author_email="earaujoassis@gmail.com",
    description="A tiny (pico)system intended to send e-mail messages from a remote client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/earaujoassis/pico",
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    python_requires='>=2.7, <4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'ploy=pico:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/earaujoassis/pico',
        'Tracker': 'https://github.com/earaujoassis/pico/issues',
    },
)
