# MultiGlobAl: global alignment of multilayer networks
MultiGlobAl is a software tool for the Pairwise Global Network Alignment (PGNA) of Multilayer Networks.

We C-compiled it (via Nuitka, https://nuitka.net) for macOS, Linux, and Windows. Sources are available in '/src' folder.


## 1. Installation

MultiGlobAl needs Python3 and the dependencies listed in 'requirements.txt'.

It has been tested on the following O.S.:
- macOS (Ventura 13.5, Apple M1), Python v3.11.
- Linux (Ubuntu, AMD64), Python v3.10.
- Windows 11 (AMD64), Python v3.11.

Dependencies can be installed by using a ready-to-use setup (see 1.1).

Alternatively, dependencies can be installed via [Python Package Installer (pip)](https://pip.pypa.io/en/stable/), by using 'requirements.txt' (see 1.2).

### 1.1. setup.py
```
python3 setup.py install
```

(or its alias 'python', if available).

ONLY FOR LINUX: setup.py will install 'python3-tk', thus we suggest executing it with 'sudo'.


### 1.2. requirements.txt

```
pip3 install -r requirements.txt
```

(or its alias 'pip', if available).

ONLY FOR LINUX: You must also install 'python3-tk':

```
sudo apt-get install python3-tk
```

<br />

## 2. MultiGlobAl use

### 2.1 Via GUI

- Double Click on 'MultiGlobAl' file.

ONLY FOR macOS and LINUX: You may need to set execute permissions for the executable.:

```
chmod +x MultiGlobAl 
```

### 2.2. Via Shell
```
./MultiGlobAl [-h] -s SOURCE -t TARGET [-sm SIMILARITY_MATRIX] -o OUTPUT
```

To show the help message, you can use -h (or --help).

<br />

## MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.