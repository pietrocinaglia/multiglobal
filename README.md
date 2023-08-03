# MultiGlobAl: global alignment of multilayer networks
MultiGlobAl is a software tool for the Pairwise Global Network Alignment (PGNA) of Multilayer Networks.

It was C-compiled via Nuitka (https://nuitka.net).

The executable supports macOS and Unix-like OS.
We tested MultiGlobAl on macOS (v.13, Apple M1) with Python v3.10 and v3.11. Contact us for other OS.


## Requirements
MultiGlobAl needs Python 3.11 (or later), as well as the dependencies listed in 'requirements.txt'.


Dependencies may be installed via [Python Package Installer (pip)](https://pip.pypa.io/en/stable/):

```
pip3 install -r requirements.txt
```

or (alias: pip, pip3):

```
pip install -r requirements.txt
```
<br />

## MultiGlobAl use

### Via GUI

- Double Click on 'MultiGlobAl' file.

You can set the execute permission on the file as follows (if needed):

```
chmod +x MultiGlobAl 
```

### Via Shell
```
./MultiGlobAl [-h] -s SOURCE -t TARGET [-sm SIMILARITY_MATRIX] -o OUTPUT
```

To show the help message, you can execute -h (or --help):

```
./MultiGlobAl -h
```

<br />

## MIT License

Copyright (c) 2022

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