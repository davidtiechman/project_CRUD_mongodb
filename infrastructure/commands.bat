docker build -t davidnachmen/fastapi-mongo:latest .
docker run -p 8000:8000 davidnachmen/fastapi-mongo:latest


docker push davidnachmen/fastapi-mongo:latest
docker pull davidnachmen/fastapi-mongo:latest
