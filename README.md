# DevOps Cloud Project

Full-stack application deployed using DevOps best practices 

<img width="600" height="233" alt="image" src="https://github.com/user-attachments/assets/e1af473e-45f4-4f0c-b0e8-1c3c352b71a7" />


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


<img width="560" height="421" alt="image" src="https://github.com/user-attachments/assets/5cb5b29c-62d7-4863-850f-b802ca532062" />


## Services
- Backend: Flask
- Frontend: Nginx
- Database: PostgreSQL
- LocalStack: AWS mocks

## Run
```bash
docker compose up --build

Step 1: Clone the repo locally (if not already)
Since you already have it locally, you’re fine. Otherwise:
git clone https://github.com/ibtissemayariii/devops-project.git
cd devops-project

Step 2: Create a new branch for your changes
Always a good idea to work in a branch, so your main stays stable:
git checkout -b add-new-features

Step 3: Make your changes
Add new backend features in backend/
Add new frontend pages in frontend/
Add Terraform modules in terraform/
Update docker-compose.yml
Update .github/workflows/ci-cd.yml for new CI/CD steps





