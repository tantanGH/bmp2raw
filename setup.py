import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bmp2raw",
    version="0.2.2",
    author="tantanGH",
    author_email="tantanGH@github",
    license='MIT',
    description="bmp files to raw movie file converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/bmp2raw",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bmp2raw=bmp2raw.bmp2raw:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    setup_requires=["setuptools"],
    install_requires=["Pillow"],
)
