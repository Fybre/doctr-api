# docTR API - Docker

**Docker image based on the sample API framework by Mindee**

Provides OCR capabilities to your applications via REST endpoints.

docTR Github:
https://github.com/mindee/doctr

Docker Image: https://hub.docker.com/repository/docker/fybre/doctr-api

I have just added a couple of endpoints for extracting plain text from files, rather than json dictionaries, and made it a bit easier to run with docker compose.

## Build your own:
To build your docker image:

Clone the repository, and then run (from the same folder as the Dockerfile)

    docker build . 

To bring up your container use the docker-compose.yaml file as a starting point (if you have changed the image name you will need to alter that) or just use my image by running the default compose file

docker-compose.yaml
    
    services:
      doctr-api:
        image: fybre/doctr-api
        container_name: doctr-api
        ports:
          - 8080:8080

## Just use mine:
    mkdir doctr-api
    cd doctr-api
    wget https://raw.githubusercontent.com/Fybre/doctr-api/refs/heads/main/docker-compose.yaml
    docker compose up -d

## Usage:

For documentation, navigate to 
http://localhost:8080/docs
(or whatever IP and port you deployed to)

The following endpoints are available:

**/detection/** - Perform text detection

**/ocr/** - Perform OCR, returns json formatted results

**/kie/** - Perform KIE

**/ocrtext/** - Performs OCR returning text result - result.render()

**/ocrtext/single/** - Simple endpoint to perform OCR on a single file, no other parameters needed

**/ocrjson/** - Performs OCR, returns simple json with extracted text

**/ocrjson/single/** - Simple endpoint to perform OCR on a single file, no other parameters needed. Returns simple json with extracted text


