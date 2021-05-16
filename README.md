# Chari Lake
![CI/CD Pipeline](https://github.com/Iconicto/chari-lake/workflows/CI/CD%20Pipeline/badge.svg) ![GitHub](https://img.shields.io/github/license/Iconicto/chari-lake) 

Official Website of the Chari Lake Hotel

### Prerequisites
- Python3.6+
- [PIP](https://pip.pypa.io/en/stable/installing)

### Development Setup
- Install PIP packages <br>
`pip install -r requirements.txt`
- Make the database <br>
`python3 manage.py migrate`
- Start dev server <br>
`python3 manage.py runserver `


### Git Secrets

#### Encrypt

```bash
gcloud kms encrypt \
    --key "chari-lake" \
    --keyring git-secrets \
    --location global  \
    --plaintext-file ".env" \
    --ciphertext-file ".env.enc" \
    --project "iconicto"
```

#### Decrypt
```bash
gcloud kms decrypt \
    --key "chari-lake" \
    --keyring git-secrets \
    --location global  \
    --plaintext-file ".env" \
    --ciphertext-file ".env.enc" \
    --project "iconicto"
```