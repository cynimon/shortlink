# shortlink
### App for creation shortlink for given long one
###

> **Startpage:** 127.0.0.1:5005
> 
> **Docs:** 127.0.0.1:5005/docs

### Options:
- To build and start app

```
docker-compose up
```

- Stop (ctrl+c) and start app
```
docker-compose stop
docker-compose start
````
- Delete app and content from system
```
docker-compose down --v
```
- Run tests in container
```
docker exec -it  shortlink_app sh
pytest
```