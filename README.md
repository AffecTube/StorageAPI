# StorageAPI

 _Storage API_ provides a simple REST service to allow the storage of data from the [AffecTube](https://github.com/AffecTube/AffecTube) extension.
 The received data is stored in a text file in JSON format. Only a `PUT` endpoint is provided by the service.

For more informaiton about _AffecTube - Chrome extension for YouTube video affective annotations_, visit its [GitHub repository](https://github.com/AffecTube/AffecTube).  

## Deployment
The service is provided as a docker container. To lunch it, run the following commands:
```bash
$ docker build -t StorageAPI .
$ docker run -p 8081:80 -d StorageAPI
```
where `8081` is a sample port number that the service will listen on.

