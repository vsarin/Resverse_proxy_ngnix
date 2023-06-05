# Resverse_proxy_ngnix

###############################################################################################################################
There are three Dockers involved in this demo. 
NGNIX-FLASK-Destination 
###############################################################################################################################
How to create Docker Images? (You must be in the directory to create the image or use the relative path)
sudo docker build -t client-container .
sudo docker build -t ngnix-container .
sudo docker build -t test-station .
###############################################################################################################################
How to run these containers ?
sudo docker run -d -p 8000:8000 --name client client-container
sudo docker run -d -p 9805:9805 --name test-station test-station
How to run the NGNIX Docker ?
sudo docker run -d --name nginx-container -p 80:80 --link client:client nginx-container
Note: Plase note how we are linking the client container to NGNIX Server as FLASK Server sits outside and not in the same container
###############################################################################################################################
Sample Input which is tested
{
    "ip_address": "192.168.1.29",
    "cmd": "ls -l",
    "some_metadata": "2.2.2.2"
}
###############################################################################################################################
