Clone the repo

git clone https://github.com/Toine517/SimpleDocker.git

Install dependencies

pip3 install requirements.txt

Run the application

python3 test_app.py

Access the application 

http://localhost:8080

Build the docker image

docker build -t compute-pi-app:v1 .

Test the image

docker run -d -p 5070:5070 compute-pi-app:v1

