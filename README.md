## Computer Vision - Cifar100 Datasets
### Introduction
- Problem: Classify 100 objects use model sota Restnet50 & dataset Cifar100.
- Apply MLops processing to development production:
    + Using Flask api for make API.
    + Dockerlize product.
    + Deploy to Google Clould Platform.
### Set up 
#### Setup by Github
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
#### Setup by Docker
- Clone resource from github:
```
git clone https://github.com/Phammanh26/cv-cifar100.git
```
- Pull image from docker hub:
```
docker pull pham2604/cv-cifar100
```
- Use mount and start container with above image:
```
docker run -p 5000:5000 -v $(pwd):/code pham2604/cv-cifar100 
```
- Note: 
    + I use docker for dockerize package, so must `mount` resource from local into docker for start container.
    + If you want  dockerize all resource, you can add line `COPY . .` in DockerFile
    + `-p 5000:5000` is expose port at local maapping with port run at docker, you define port docker in `EXPOSE target-port` in DockerFile
    + $(pwd) is current folder -> target folder want mount.
