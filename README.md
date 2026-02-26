# Micro K8s Secure Starter

A small, from-scratch starter for a **secure-by-default** microservice you can grow into a full platform.

- Minimal **FastAPI** service
- **Dockerfile** runs as a **non-root** user
- Kubernetes manifests with **readOnlyRootFilesystem**, **no privilege escalation**, and **resource limits**
- GitHub Actions:
  - **Semgrep** (OWASP Top 10 rules)
  - **Trivy** filesystem & **image** scan (fail on High/Critical)
  - **SBOM** (Syft CycloneDX) artifact

> Semgrep OWASP ruleset: see registry page. Trivy GitHub Action supports exit-code gates on severity.  
> References: semgrep ruleset, trivy action examples.

## Quickstart (Windows PowerShell)

### 1) Run locally
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://localhost:8000/health
```

### 2) Docker build & run
```powershell
docker build -t secure-starter:local .
docker run -p 8000:8000 secure-starter:local
```

### 3) Kubernetes (KinD or Minikube)
```powershell
# Create cluster (example with kind)
kind create cluster --name dev
kubectl apply -f k8s/deployment.yaml
kubectl get pods,svc
```

### 4) Create GitHub repo and push (HTTPS via gh)
```powershell
git init -b main
git add .
git commit -m "feat: initial secure starter"
# Create repo in your account and push
gh repo create micro-k8s-secure-starter --public --source . --remote origin --push
```

## Pipelines
- `.github/workflows/sast_semgrep.yml` – SAST (Semgrep)
- `.github/workflows/sca_trivy_fs.yml` – Trivy filesystem scan
- `.github/workflows/build_image.yml` – Build → Trivy image scan → SBOM artifact

## Next Steps (optional)
- Add **Cosign keyless signing** and push to GHCR; then enforce at admission with **Kyverno verifyImages**.
- Add **Falco** via Helm for runtime detection.
