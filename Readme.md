# Basic first API

A basic api created with python, using fastAPI and uvicorn like the turial from [fastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)

## uvicorn - ASGI webserver

with the command

```
uvicorn app.main:app --reload
```

we run the server and can access the api via webbrowser: http://localhost:8000/
for swagger: http://localhost:8000/docs

## using AmazonWebServices

converting it to lambda:

updating the app with mangum to have a handler for lambda to be able to call

## used API

the used api is defined by the given api.yaml file and can be imported at aws
