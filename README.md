# 🚀 DevOps Blog Application

A complete DevOps project featuring a **Django blog application** deployed using **Docker**, **Kubernetes (Minikube)**, **GitHub Actions CI/CD**, and **Ansible** automation.

> **Built by Dharshan** — DevOps Learning Project

---

## 📋 Project Structure

```
devOps/
├── blogapp/                    # Django Blog Application
│   ├── manage.py               # Django management script
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile              # Docker container configuration
│   ├── .dockerignore           # Files to exclude from Docker build
│   ├── blogapp/                # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── blog/                   # Blog application
│       ├── models.py           # Post model
│       ├── views.py            # List, detail, create views
│       ├── forms.py            # Post creation form
│       ├── urls.py             # URL routing
│       └── templates/blog/     # HTML templates
├── k8s/                        # Kubernetes manifests
│   ├── deployment.yaml         # Deployment (2 replicas)
│   └── service.yaml            # NodePort Service (port 30007)
├── ansible/                    # Ansible automation
│   ├── deploy.yml              # Deployment playbook
│   └── inventory.ini           # Inventory file
├── .github/workflows/          # CI/CD
│   └── ci-cd.yml               # GitHub Actions workflow
└── README.md                   # This file
```

---

## 🛠️ Prerequisites

Install the following tools on your **Windows** machine:

| Tool | Install Guide |
|------|--------------|
| **Python 3.11** | [python.org/downloads](https://www.python.org/downloads/) |
| **Docker Desktop** | [docs.docker.com/desktop/windows](https://docs.docker.com/desktop/install/windows-install/) |
| **Minikube** | [minikube.sigs.k8s.io/docs/start](https://minikube.sigs.k8s.io/docs/start/) |
| **kubectl** | [kubernetes.io/docs/tasks/tools](https://kubernetes.io/docs/tasks/tools/) |
| **Git** | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **Ansible** | Install via **WSL** (Windows Subsystem for Linux) — see below |

### Installing Ansible (via WSL)

Ansible doesn't run natively on Windows. Use WSL:

```bash
# Open WSL terminal
wsl

# Install Ansible
sudo apt update
sudo apt install ansible -y

# Verify installation
ansible --version
```

---

## 🚀 Step-by-Step: Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd devOps
```

### Step 2: Run Django Locally (Optional — to test before Docker)

```bash
cd blogapp
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```

Open your browser: **http://127.0.0.1:8000**

### Step 3: Build the Docker Image

```bash
# Make sure Docker Desktop is running
cd blogapp
docker build -t blogapp:latest .
```

### Step 4: Run with Docker (Optional — to test the container)

```bash
docker run -p 8000:8000 blogapp:latest
```

Open your browser: **http://localhost:8000**

### Step 5: Start Minikube

```bash
minikube start
```

### Step 6: Deploy with Ansible (via WSL)

```bash
# Open WSL terminal
wsl

# Navigate to the project directory
cd /mnt/c/Users/<YourUsername>/Desktop/devOPs/devOps

# Run the Ansible playbook
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml
```

### Step 7: Access the Blog App

```bash
minikube service blogapp-service --url
```

Open the URL shown in your browser (usually **http://192.168.x.x:30007**).

---

## 🔍 Useful kubectl Commands

### Check Pods

```bash
kubectl get pods
```

### Check Services

```bash
kubectl get services
```

### View Pod Logs

```bash
# Get pod name first
kubectl get pods

# View logs of a specific pod
kubectl logs <pod-name>
```

### Describe a Pod (for debugging)

```bash
kubectl describe pod <pod-name>
```

### Delete and Redeploy

```bash
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Stop Minikube

```bash
minikube stop
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline (`.github/workflows/ci-cd.yml`) runs automatically on every push to the `main` branch:

| Step | What It Does |
|------|-------------|
| **Checkout Code** | Downloads your code from GitHub |
| **Set up Python 3.11** | Installs Python on the runner |
| **Install Dependencies** | Runs `pip install -r requirements.txt` |
| **Django System Checks** | Validates your Django project has no errors |
| **Build Docker Image** | Builds the `blogapp:latest` Docker image |
| **Success Message** | Prints a confirmation that everything passed ✅ |

---

## 📖 Key Concepts Explained

### What is Docker?
Docker packages your app and all its dependencies into a **container** — a portable, isolated environment that runs the same everywhere.

### What is Kubernetes?
Kubernetes (K8s) **orchestrates containers** — it manages running, scaling, and networking your Docker containers across machines.

- **Pod**: The smallest unit in K8s. A pod runs one or more containers. Think of it as a wrapper around your container.
- **Deployment**: Tells K8s how many copies (replicas) of your pod to run and how to update them.
- **Service**: Exposes your pods to the network. A NodePort service lets you access the app from outside the cluster.

### What is Ansible?
Ansible **automates tasks** — like deploying apps, configuring servers, or running commands on multiple machines. It uses simple YAML playbooks instead of complex scripts.

### What is Minikube?
Minikube runs a **local Kubernetes cluster** on your machine for development and testing.

---

## 📝 Blog App Features

- ✅ View all blog posts on the home page
- ✅ Click on a post to read the full content
- ✅ Create new blog posts with a form
- ✅ Beautiful dark-mode gradient UI
- ✅ SQLite database (no setup needed)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

**Made with ❤️ for DevOps learning**



---

minikube start
# Load your Docker image into Minikube
minikube image load blogapp:latest
# Apply the deployment (create pods)
kubectl apply -f k8s/deployment.yaml
# Apply the service (expose to network)
kubectl apply -f k8s/service.yaml
# Check running pods
kubectl get pods
# Check services
kubectl get services

kubectl port-forward service/blogapp-service 8000:8000




minikube stop
ansible-playbook ansible/deploy.yml
mks

Every time you restart, do this:
1. PowerShell (start the cluster):
minikube start
2. WSL (fix the kubeconfig):
fix-kube
kubectl get pods

Why fix-kube is always needed after restart
Every time minikube start runs on Windows, it writes a new random port like 127.0.0.1:59821 to the kubeconfig. fix-kube replaces that with the correct 192.168.49.2:8443 that WSL can reach. This is just how minikube on Windows+WSL works — nothing you did wrong.