docker build -t davidnachmen/fastapi-mongo:latest .
docker run -p 8000:8000 davidnachmen/fastapi-mongo:latest


docker push davidnachmen/fastapi-mongo:latest
docker pull davidnachmen/fastapi-mongo:latest

oc apply -f mongo-pvs.yaml
oc apply -f mongodb-deploynent.yaml
oc apply -f mongo-service.yaml
oc apply -f fastapi-for-mongo.yaml

