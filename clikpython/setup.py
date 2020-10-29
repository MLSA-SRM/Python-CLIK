import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clik", # Replace with your own username
    version="0.0.0",
    entry_points={
        'console_scripts':[
            'clik=clikpython.clik:main_menu']},
    author="Kushagra Gupta",
    author_email="guptakushagra15.10@gmail.com",
    description="A CLI tool to keep your Secret/OAuth Keys Safe",
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
    install_reqrires=['printy',],
)