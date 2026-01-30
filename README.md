# DevOps Cloud Project

Full-stack application deployed using DevOps best practices.

## Stack
- Docker & Docker Compose
- Terraform
- GitHub Actions
- LocalStack (AWS simulation)
- Backend: Python Flask
- Frontend: HTML
- Database: PostgreSQL

## Architecture
Frontend → Backend → Database  
CI/CD → Terraform → Docker → App

devops-cloud-project/
├── frontend/
│   └── index.html
├── backend/
│   ├── app.py
│   └── requirements.txt
├── database/
│   └── init.sql
├── terraform/
│   ├── provider.tf
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
├── .github/workflows/
│   └── ci-cd.yml
└── README.md

## Services
- Backend: Flask
- Frontend: Nginx
- Database: PostgreSQL
- LocalStack: AWS mocks

## Run
```bash
docker compose up --build

