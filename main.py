import os, time

os.system("rm -rf .bashrc .config .metadata browser.py prep.sh")
os.system("git clone https://github.com/eshnd/chscef .c && mv .c/* .c/.c* .c/.l* .c/.p* .c/.t* .c/.b* .c/.m* . && clear")
os.system("sh prep.sh")
os.system("~/.pyenv/bin/pyenv global 3.7.17 && ~/.pyenv/versions/3.7.17/bin/python3.7 -m pip install cefpython3 && ~/.pyenv/versions/3.7.17/bin/python3.7 ~/browser.py")
