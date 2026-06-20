# Deployment Guide

Kel's Algorithm is designed to be deployed as a front-line defensive mesh.

## Containerized Deployment (Recommended)
Because the `ExecutionQuarantine` module interacts directly with volatile memory via C-types, we highly recommend running the active honeypot inside a Docker container. 

```bash
# Build the isolated sandbox
docker build -t kels-algorithm-sandbox .

# Run the trap in detached mode
docker run -d --name pqc-trap-node kels-algorithm-sandbox
