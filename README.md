## Computer Vision - Cifar100 Datasets
### Introduction
- Problem: Classify 100 objects use model sota Restnet50 & dataset Cifar100.
- Apply MLops processing to development production:
    + Using Flask api for make API.
    + Dockerlize product.
    + Deploy to Google Clould Platform.
### Set up 
### Use Github
- Clone source code (use `git clone <git-url>`):
```
git clone https://github.com/Phammanh26/cv-cifar100.git
```
- Install packages (note: you should make virtual enviroment before install packages):
```
pip install -r requirements.txt
```
- After, runnng app by command `python app.py` and click to `http://ip:port/` for experiment
+ Note: Ip & port for define in app.py, you edit at:  `app.run(debug = True, host='0.0.0.0', port="5050")`
### Use Docker
- Clone resource from github:
- Pull image from docker hub:
- Use mount and running containers with above image:
- Running