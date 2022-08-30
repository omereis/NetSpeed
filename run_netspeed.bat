docker rm -f netspeed
docker build --rm -f netspeed.dockerfile -t netspeed .
docker run -it -d --name netspeed -p 5005:5005 netspeed
docker exec -it netspeed bash