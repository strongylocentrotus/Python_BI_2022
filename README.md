# 3<sup>rd</sup> HW _ultraviolence.py_
## HI! Welcome to my running-this-script-for-Dummies guide.

I performed this steps on Ubuntu 20.04.4 LTS and python 3.11.0rc2 version. So please set the same ones or steal a laptop with them. 

### Updating python
Unfortunately we need **Python version 3.11** to launch the script, the one to be released a couple of days later than we need to pass the deadline. 
That is why I installed the last prelease - python 3.11.0rc2). You may update your python and set nedeed extentions and virtual environments by copying the following to your terminal (_ctrl+alt+T_):
`sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
sudo apt install python3.11-dev
sudo apt install python3.11-venv`

### Trying PyCharm
When updated play any python interface you like. I used PyCharm Professional. If you want to continue repeating my lines, just download the same software (`sudo snap install pycharm-professional --classic`) and ask your university for the license. 

### Saving environment
Create virtual environment in the folder where the script is located (in my case it was /home/lisa/PycharmProjects/pythonProject/venv/bin/python; **check for** _Settings > Project > Add Interpreter > Add local interpreter > Virtualenv Environment: New: Base: python 3.11_).

### Requirements
Download requirements.txt file from here to your working folder and then use PyCharm terminal to install requirements. 
`<path_to_the_venv/bin/python> -m pip install -r requirements.txt` or install them step by step repeating 
`<path_to_the_venv/bin/python> -m pip install <package name>`

### Launching 
Just run ultraviolence.py from your working folder. 

# Congrads!!!
