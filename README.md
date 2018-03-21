# Shop Score Page

This application displays the current performance of online store managers - processing speed of incoming requests.

There are three types of unprocessed requests:
- green - waiting time does not exceed 7 minutes
- yellow - delay less than 30 minutes
- red - delay more than 30 minutes

Example with a working db on heroku <https://bd-shop-score.herokuapp.com/>

# How to local use

first install dependencies
```#!bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python server.py
```
then you can run app
```#!bash
python server.py -c <user>:<login>@<host>:<port>/<db>
```
where you should type database uri
(for example: admin:pass@address.org:5432/my_base)
and open <http://127.0.0.1:5000/>

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
score:Rysherat2@shopscore.devman.org:5432/shop