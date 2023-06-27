# shortlink
### App for creation shortlink for given long one
###

> **Startpage:** 127.0.0.1:5005
> 
> **Docs:** 127.0.0.1:5005/docs

1. To build and start app

```
docker-compose up
```

2. Stop (ctrl+c) and start app
```
docker-compose stop
docker-compose start
````

3. Delete app and content from system
```
docker-compose down --v
```

4. Run tests in container
```
docker exec -it  shortlink_app sh
pytest
```