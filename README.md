# Download and play
For only play open releases in right side and download flappy-bird.zip
# Flappy Bird

This version of flappy bird written with PyGame library. 

Video Tutorial - [Youtube](https://www.youtube.com/watch?v=UZg49z76cLw&t=177s)

References of images and sound can be found there: [Github repo](https://github.com/clear-code-projects/FlappyBird_Python)

### If you have own envs just skip Configure part
## Configure Project

First, use venv or conda for your project environment. I use venv for each of my separate python projects, so each project becomes mobile and standalone and the main environment is not filled with packages


Open project in terminal and type:

#### Linux/macOS
```bash
python3 -m venv .env
```
#### Windows
```bash
python -m venv .env
```
### Activate venv

#### Linux/macOS
```cmd
source .env/Scripts/activate.bat
```
#### Windows
```bash
source .env/bin/activate
```
After activation should be added in front of the terminal (.env)
### Deactivate (Linux/macOS/Windows)
```bash
deactivate
```
More about venv: [venv documentation](https://docs.python.org/3/library/venv.html)
## Installing
After enter to venv, just install some packages for lauch game

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install requirements.txt
```
Write this for check packages:
```bash
pip freeze
```
Output something like this:
```
altgraph==0.17
future==0.18.2
pefile==2019.4.18
pygame==1.9.6
pyinstaller==4.0
pyinstaller-hooks-contrib==2020.8
pywin32-ctypes==0.2.0
```
### Open and run main.py and just enjoy!

## Generate EXE
For generate .exe file we use packet [pyinstaller](https://www.pyinstaller.org/)

Open project folder and enter to venv and type:
### Windows
```bash
pyinstaller --clean -F -w -i=icon.ico --add-data="assets;assets" --add-data="sounds;sounds" --add-data="fonts;fonts" -n flappy-bird main.py
# --clean - for clear pyinstaller cache
# -F - one file output
# -w - without console (windowed)
# -i - icon for file, used with path to .ico
# --add-data - adding files to complete .exe, file name must be same as in your project
# -n - name of exe
# main.py - python file source
```
### Linux
```bash
pyinstaller -F -w --add-data="assets:assets" --add-data="sounds:sounds" --add-data="fonts:fonts" -n flappy-bird main.py
# -i - icon can not be used in Linux
```
.exe file can be found in pygame-flappy-bird/dist/flappy-bird.exe
### Directory Structure 
<pre>/pygame-flappy-bird
 ┬  
 ├ .env  
 ├ assets  
 ├ build  
 ├ dist
  ┬
  ├  flappy-bird.exe
 ├ fonts  
 ├ sounds 
 ├ .gitignore
 ├ flappy-bird.spec
 ├ icon.ico
 ├ main.py
 ├ README.md
 ├ requirements.txt

</pre>
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)




