import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="examplePackage-kg1510", # Replace with your own username
    version="0.0.3",
    author="Kushagra Gupta",
    author_email="guptakushagra15.10@gmail.com",
    description="A small example package to print the passed string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KG-1510/Project-CLIK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
