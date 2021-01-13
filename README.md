# CLIK
![](https://img.shields.io/github/forks/MLSA-SRM/Project-CLIK?style=for-the-badge)
![](https://img.shields.io/github/stars/MLSA-SRM/Project-CLIK?color=purple&style=for-the-badge)
![](https://img.shields.io/badge/contributors-4-orange.svg?style=for-the-badge)

CLIK is a command line interface tool to hide and manage your API keys and Secret/Auth tokens.
This is for project managers for easy management of project-related keys and their distribution.
<br><br>
## How CLIK Works
CLIK provides you with a command line interface that allows you to store your API Keys and Secret/Auth tokens in an encrypted JSON file.
You are provided with an option to either store this key locally in a file, or making a note of it to store it anyway you like.
The encrypted JSON file can safely be uploaded to VCS repositories, meaning access will only be granted to those who have been given the JSON decryption key by you.
You can use the CLIK to also add, remove or modify keys, as and when required.
## Built With
| Software | Version |
|----------|---------|
| Python 3 | 3.7.1 |
| Visual Studio Code| 1.50.1|

## Tested With
| Operating System | Version(s) |
|----------|-------------|
| Microsoft Windows | Windows 10 |
| Apple macOS | 10.15(Catalina), Beta 11.0(Big Sur) |

## Installation
You can either clone this repository or install it via pip
```python
pip install python-clik
```

## Usage
Once you install CLIK, a short and concise documentation can be found br running the following command on your console:
```python
clik
```
## Initialising the JSON File
To create a new file to store keys type the following command in your console:
```python
clik init
```
Now, you can specify all the keys you want to add in a step by step fashion.
CLIK will automatically encrypt the file for you and generate your encryption key.
Now you can either store the key locally or write it down for safekeeping.
So now, your JSON file containing all your keys is ready for upload on your repository.
## Adding/Subtracting Keys
To add new keys to an existing JSON file, type the following command in your console:
<br>
### For Adding Keys
```python
clik FILENAME add
```

### For Subtracting Keys
```python
clik FILENAME subtract
```
## For Modifying Keys
To modify any key in an existing JSON file, type the following command in your console:
```python
clik FILENAME modify
```
## For Encrypting the Keys File
To encrypt the JSON file, type the following command in your console:
```python
clik FILENAME enc
```
This will ask for any existing Keys to encrypt the JSON file with. If you have an existing Key,
 continue. Else, you can specify/create a new key for this new encryption.

 ## For Decrypting the Keys File
 To decrypt the JSON file, type the following command in your console:
 ```python
 clik FILENAME dec
 ```
This will ask for any existing Keys to decrypt the JSON file with. If you have an existing Key,
continue normally. Else, provide a path for the Key to be used for decryption.

> Note: For any kind of operation on an encrypted JSON file, you need to decrypt it first.

## Help
To check the syntax for any of the commands or their function, type the following command in your console:
```python
clik --help
```

## Version
To check the version of CLIK you're running, type the following command in your console:
```python
clik --version
```
> Note: Before uploading the JSON file containing your Keys to any VCS, it is recommended to store your .key file containing your Key to decrypt this encrypted JSON file in .gitignore of any other directory of your computer.

## Dependancies
* [printy](https://github.com/edraobdu/printy)
* [Python 3](https://python.org/)
* [cryptography](https://github.com/pyca/cryptography)

## Contributors
* [Mihir Singh](https://github.com/mihirs16)
* [Anushka Agarwal](https://github.com/anushka17agarwal)
* [Kushagra Gupta](https://github.com/KG-1510)
* [Ariz Siddiqui](https://github.com/arizsiddiqui)
