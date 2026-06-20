## To run the application

```
uvicorn backend.app:app --reload
```



## To run the docker file and create build

```
docker build -t health-microservice .
```


docker build      -> Build an image
-t                -> Tag/name the image
health-microservice -> Image name
.                 -> Current directory is the build context