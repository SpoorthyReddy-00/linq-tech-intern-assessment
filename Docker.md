#  Docker Setup (Bonus)

## Why Docker?

Docker makes the project portable. Anyone can run the app without installing Python or packages on their machine — everything is bundled in a container.

## How It Works

- `Dockerfile` defines the Python environment and installs all required libraries.
- `docker-compose.yml` makes it easy to build and run the container.

## How to Run

> Make sure Docker is installed on your machine: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

### 1. Build and Start Container

```bash
docker-compose up --build
