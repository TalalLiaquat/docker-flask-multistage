# 🐳 Docker Multi-Stage Build for Python Flask Application

A production-ready Docker project demonstrating Docker best practices using a Python Flask application. This project showcases image optimization, security, and deployment readiness using **Multi-Stage Builds**, **Gunicorn**, **Healthcheck**, and **Non-root User**.

---

## 🚀 Project Overview

This project containerizes a simple Flask application using Docker while following production-ready Docker best practices.

### Features

- ✅ Dockerized Python Flask Application
- ✅ Multi-Stage Docker Build
- ✅ Lightweight Docker Image
- ✅ Gunicorn Production WSGI Server
- ✅ Docker Healthcheck
- ✅ Non-root User
- ✅ Optimized Build Context using `.dockerignore`

---

## 🏗️ Architecture

```text
              Flask Application
                     │
                     ▼
               Dockerfile
                     │
         Multi-Stage Docker Build
                     │
                     ▼
             Optimized Docker Image
                     │
               docker run
                     │
                     ▼
             Running Container
                     │
      Gunicorn + Healthcheck + Non-root User
```

---

## 📂 Project Structure

```text
docker-flask-multistage/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

- Python 3.14
- Flask
- Gunicorn
- Docker
- Docker Multi-Stage Build

---

## ⚙️ Docker Commands

### Build Docker Image

```bash
docker build -t flask-multistage:v1 .
```

### Run Container

```bash
docker run -d -p 5000:5000 --name flask-app flask-multistage:v1
```

### List Running Containers

```bash
docker ps
```

### View Logs

```bash
docker logs flask-app
```

### Stop Container

```bash
docker stop flask-app
```

### Remove Container

```bash
docker rm -f flask-app
```

### List Docker Images

```bash
docker images
```

---

## 🐳 Multi-Stage Build

This project uses a **Multi-Stage Docker Build** to create a lightweight and production-ready Docker image.

### Builder Stage

- Installs project dependencies
- Creates an isolated build environment

### Final Stage

- Copies only the required files
- Removes unnecessary build dependencies
- Produces a smaller and optimized image

---

## ❤️ Health Check

A dedicated health endpoint is available:

```text
GET /health
```

Response:

```text
OK
```

Docker continuously checks this endpoint to ensure the container is healthy.

Example:

```text
STATUS: Up 2 minutes (healthy)
```

---

## 🔒 Security

This project follows Docker security best practices by running the application as a **non-root user**.

### Benefits

- Improved container security
- Reduced attack surface
- Production-ready deployment

---

## 📊 Docker Image Optimization

Optimization techniques used:

- Multi-Stage Build
- `python:3.14-slim`
- `.dockerignore`
- `--no-cache-dir`
- Lightweight runtime image

---

## 📸 Screenshots

Add the following screenshots:

### Docker Build

> *(Add screenshot here)*

### Docker Images

> *(Add screenshot here)*

### Running Container

```bash
docker ps
```

> *(Add screenshot here)*

### Application Running

```
http://localhost:5000
```

> *(Add screenshot here)*

### Health Endpoint

```
http://localhost:5000/health
```

> *(Add screenshot here)*

---

## 💡 Key Learnings

- Docker Images vs Containers
- Dockerfile Instructions
- Docker Layer Caching
- Build Context
- `.dockerignore`
- Multi-Stage Docker Build
- Gunicorn
- Docker Healthcheck
- Non-root User
- Production Docker Best Practices

---

## 📄 Resume Highlights

- Built and containerized a Python Flask application using Docker.
- Optimized Docker images using Multi-Stage Builds and lightweight runtime images.
- Implemented Docker best practices including `.dockerignore`, Gunicorn, Healthcheck, and non-root user execution.
- Improved deployment efficiency by reducing unnecessary build context and creating a production-ready container.

---

## 🚀 Future Improvements

- Docker Compose
- Nginx Reverse Proxy
- PostgreSQL Integration
- GitHub Actions CI/CD
- Kubernetes Deployment
- Helm Charts
- AWS ECS Deployment
- AWS EKS Deployment

---

## 👨‍💻 Author

**Talal**

If you found this project useful, consider giving it a ⭐ on GitHub.
