# webfortune


## Clone repository
```
git clone https://github.com/kaylacoats/webfortune
```

## Create a virtual environment
```
python3 -m venv env
source env/bin/activate
```

## Build docker
```
docker build -t kaylacoats/webfortune .
docker run -dp 8007:5000 kaylacoats/webfortune
```
