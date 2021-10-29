# Sum-API

## How to use

To use this API microservice, first build the docker container:
`sudo docker build -t sums/number-sum:1.0 .`

Then run the docker container:
`sudo docker run -p 8000:8000 sums/number-sum:1.0`

After the container is running, one can view the API microservice by querying the microservice:
`http://localhost:8000/sum`

To get the sum of two specific numbers determined by the user, the user can use the following address while replacing the values of `num1` and `num2` with their desired values:
http://localhost:8000/sum?num1=6&num2=8

## References
[Dockerize Microservice](https://medium.com/@madhukaudantha/dockerize-microservice-3d7562ffcda3)
