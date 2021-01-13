import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-clik",
    version="1.0",
    entry_points={
        'console_scripts':[
            'clik=clikpython.clik:main_menu']},
    author="MLSA SRM",
    author_email="contact@msclubsrm.in",
    description="A CLI tool to keep your Secret/OAuth Keys Safe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MLSA-SRM/Project-CLIK",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['printy', 'cryptography'],
)
