# Unity Install Options
* Into the OS with python2.7
* Into a virtual environment using python2.7
* Docker container

# Install Dockerfile
```
docker build -t unity .
docker run -it unity unity_scraper -h
docker run -it unity unity_client -h
docker run -it unity unity_server -h
docker run -it unity unity_send_mail -h
```

## Install this package into the OS:

```
sudo pip install .
```
* If upgrading, run:
```
sudo pip install --upgrade .
```

## Install using virtualenv
```
virtualenv unity
source unity/bin/active
pip install /path/to/Unity/.
```
