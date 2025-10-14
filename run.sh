git pull
docker build -t tgbirthday . 
docker run --rm -it -v $(pwd)/users:/app/users tgbirthday