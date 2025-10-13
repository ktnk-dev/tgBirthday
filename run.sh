git pull
docker volume create tgbirthday_database
docker build -t tgbirthday . 
docker run --rm -it -v tgbirthday_database:/app/users tgbirthday