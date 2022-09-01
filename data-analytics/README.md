# Business Problem
You are a WHO (World Health Organization) official who must assess the levels of contamination of a virus in a given country. People within a society can be connected in some way (family, friendship or work) and each person has a set of attributes.
This virus affects this society as follows:
* the contamination rate varies from person to person;
* the contamination rate from a person A to B is different from B to A and depends the characteristics of both people (A and B);
* contamination only passes through connected individuals;
* there is no cure for this disease;

Contamination data (i.e. contamination rates) were collected for half
of this society. In this problem, you will have to estimate the rate for the rest of this society and decide health policies based on the results obtained. 
# Setup
The Virus Disease analysis in only served in the user's **local host** using `Docker`
## Testing Instructions
Make sure you have [Docker](https://docs.docker.com/engine/install/) installed and follow the instructions below:

1. To build the image, run these commands in terminal:
```
$ git clone https://github.com/alefefreire/portfolio-ds.git
$ cd portfolio-ds/data-analytics
$ docker build -t image-oms .  
```
2. Once the image's been built, you can run the jupyter notebook with the command below:
````
$ docker run -d --rm --name jupyterserver -p 8888:8888 -v $PWD/notebooks:/notebooks image-oms
````
**IMPORTANT**: Make sure that your Docker Setup has pre configured memory resources of, at least, 8GB of RAM otherwise the jupyter's kernel can eventually die in the end to end runnning.

3. After running the container, click here: http://127.0.0.1:8888
4. A web page will appear for you requesting a token access to `jupyter notebook`. In order to get this token, in your terminal, run the following command:
````
$ docker container logs jupyterserver
````
5. In the logs, search for a link which looks like the following one:
````
http://127.0.0.1:8888/lab?token=a837ddbf2c36628de39831f5b15b5b9c4d5bd50eb410fd40
````
6. Just copy and paste the *serial number* after `token=` and click the `Log in` button and the access to `jupyter lab` will be granted.
7. Enjoy the analysis.  :) 