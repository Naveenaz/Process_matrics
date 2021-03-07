
## Pre requisites: ##

Download and install Python 3.x.

Either install via Homebrew : https://docs.python-guide.org/starting/install3/osx/

Or download via https://www.python.org/downloads/

Once installed check the version number : python3 --version It should return 3.x


## Steps to do set up ##


Install all dependencies. Navigate to the project root folder and do the following:

pip3 install -r requirements.txt --user



## Running Application ##

To run individual test:
```
➜ python3 process_metrics.py -h
usage: process_metrics.py [-h] -p PROCESS_NAME -d DURATION [-s SAMPLING]

optional arguments:
-h, --help            show this help message and exit
-p PROCESS_NAME, --process_name PROCESS_NAME
Enter process name
-d DURATION, --duration DURATION
Enter overall duration of the monitoring in seconds
-s SAMPLING, --sampling SAMPLING Enter sampling interval
➜  
```

Please see sample output in output.csv

<img width="1087" alt="Screen Shot 2021-03-07 at 19 52 56" src="https://user-images.githubusercontent.com/5116820/110252746-c3a66180-7f7e-11eb-8003-5ef5b6ca6c44.png">




### We can use pytest framework to write automated tests. ###


