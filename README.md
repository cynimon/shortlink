# shortlink
### App for creation shortlink for given long one
### Description:

In shortlink app you can:
1. Add your full URL and get a short link with example.com domain
2. Get any full URL by short one, if its existing in-app memory
3. Delete your long-short URLs from data


> **Startpage:** 127.0.0.1:5005 (localhost:5005)

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