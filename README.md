# snapcycle
```
This is a flask backend endpoint to access Replicate API for BLIP model.
```

## Project setup
To activate virtual environment: 

```
source env/Scripts/activate
```

## Project setup

Install flask: 
```
pip3 install Flask
```
Install replicate: 
```
pip3 install replicate
```

Install flask_cors:
```
pip3 install flask-cors
```


API Key Mac: 
```
export REPLICATE_API_TOKEN=[key]
```
On Windows: 
```
set REPLICATE_API_TOKEN=[key]
```



### Run Flask Server
```
python -m flask run --port=5001 --debug
```
