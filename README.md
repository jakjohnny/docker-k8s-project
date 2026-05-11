# Docker + Kubernetes Python Application

## Overview
This project is a containerized Python web application deployed using Docker and Kubernetes.

The application communicates with a PostgreSQL database and demonstrates core cloud-native and DevOps concepts including:

- Containerization with Docker
- Multi-container orchestration using Docker Compose
- Kubernetes deployments and services
- Service-to-service communication
- Scaling with replicas
- Local Kubernetes deployment using Minikube

---

## Technologies Used

- Python
- Docker
- Docker Compose
- Kubernetes
- Minikube
- PostgreSQL

---

## Project Architecture

Browser → Kubernetes Service → Python Application Pods → PostgreSQL Database

---

## Running with Docker Compose

```bash
docker compose up --build
