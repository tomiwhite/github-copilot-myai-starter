# myAI Starter Application

A clean, production-ready starter application designed for rapid prototyping, testing, and scaling modern applications with Azure and myAI integration.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)](https://fastapi.tiangolo.com/)

## 🚀 Overview

This starter provides a minimal but complete foundation for building modern web applications with:

- **FastAPI Backend** - High-performance async Python API with automatic documentation
- **Clean Frontend** - Simple HTML/CSS/JavaScript interface (easily upgraded to React/Vue/etc.)
- **Clean Architecture** - Organized, scalable codebase following best practices
- **CI/CD Ready** - GitHub Actions workflows included
- **Azure Ready** - Placeholders for Azure services integration
- **myAI Integration** - Ready for myAI modules and services

## ✨ Features

- ✅ RESTful API with versioning
- ✅ Health check and readiness endpoints
- ✅ Environment-based configuration
- ✅ CORS support
- ✅ Automatic API documentation (Swagger & ReDoc)
- ✅ Type safety with Pydantic v2
- ✅ Modern async/await patterns
- ✅ Responsive frontend design
- ✅ Development container support
- ✅ Comprehensive documentation

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git

## 🏁 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/tomiwhite/github-copilot-myai-starter.git
cd github-copilot-myai-starter
```

### 2. Set Up Environment

```bash
# Copy environment template
cp .env.template .env

# Edit .env with your configuration (optional for quick start)
```

### 3. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m app.main
```

The application will be available at:
- **Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/v1/docs
- **Alternative Docs**: http://localhost:8000/api/v1/redoc

## 📁 Project Structure

```
github-copilot-myai-starter/
├── backend/                    # Backend API
│   ├── app/
│   │   ├── api/               # API routes
│   │   │   ├── health.py      # Health check endpoints
│   │   │   └── example.py     # Example CRUD endpoints
│   │   ├── core/              # Core functionality
│   │   │   └── config.py      # Configuration management
│   │   ├── models/            # Data models
│   │   └── main.py            # Application entry point
│   ├── tests/                 # Backend tests
│   ├── requirements.txt       # Python dependencies
│   └── README.md              # Backend documentation
├── frontend/                   # Frontend application
│   ├── public/                # Static files
│   │   ├── index.html         # Main HTML
│   │   ├── app.js             # JavaScript
│   │   └── styles.css         # Stylesheets
│   └── README.md              # Frontend documentation
├── docs/                       # Documentation
│   └── ARCHITECTURE.md        # Architecture overview
├── .github/                    # GitHub Actions workflows
│   └── workflows/             # CI/CD pipelines
├── .devcontainer/             # Dev container configuration
├── .env.template              # Environment variables template
├── CONTRIBUTING.md            # Contribution guidelines
└── README.md                  # This file
```

## 🔧 Configuration

Configuration is managed through environment variables. Copy `.env.template` to `.env` and customize:

```bash
# Application
APP_NAME=myAI Starter API
DEBUG=True
PORT=8000

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]

# Azure (for future integration)
# AZURE_TENANT_ID=your-tenant-id
# AZURE_CLIENT_ID=your-client-id

# myAI Integration (for future integration)
# MYAI_API_KEY=your-api-key
# MYAI_ENDPOINT=https://api.myai.example.com
```

See `.env.template` for all available options.

## 📚 Documentation

- **[Architecture](docs/ARCHITECTURE.md)** - System architecture and design patterns
- **[Backend README](backend/README.md)** - Backend API documentation
- **[Frontend README](frontend/README.md)** - Frontend documentation
- **[Contributing](CONTRIBUTING.md)** - Contribution guidelines

## 🧪 Testing

### Run Backend Tests

```bash
cd backend
pytest
```

### Run Code Quality Checks

```bash
# Format code
black app/

# Lint code
flake8 app/

# Type checking
mypy app/
```

## 🐳 Docker Support (Coming Soon)

Docker configuration files will be added for containerized deployment.

## 🚀 Deployment

### Azure App Service (Recommended)

1. Create an Azure App Service
2. Configure environment variables
3. Deploy using GitHub Actions (workflow included)

### Other Platforms

This application can be deployed to:
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Any platform supporting Python applications

## 🔌 Extending the Application

### Adding New API Endpoints

1. Create a new router in `backend/app/api/`
2. Define Pydantic models in `backend/app/models/`
3. Register the router in `backend/app/main.py`

### Adding Database Support

1. Install database driver (e.g., `psycopg2` for PostgreSQL)
2. Add database URL to configuration
3. Implement repository pattern in `backend/app/repositories/`

### Integrating Azure Services

Configuration placeholders are ready for:
- Azure AD (Authentication)
- Azure Cosmos DB
- Azure Storage
- Azure Key Vault
- Application Insights

### Integrating myAI

Configuration placeholders are ready for myAI integration:
- API key management
- Endpoint configuration
- Module integration

## 🛠️ Development

### Using VS Code Dev Containers

This project includes a dev container configuration:

1. Install Docker and VS Code Remote Containers extension
2. Open the project in VS Code
3. Click "Reopen in Container" when prompted

### Using GitHub Codespaces

1. Click "Code" → "Codespaces" → "Create codespace on main"
2. Wait for the environment to set up
3. Start developing!

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Inspired by clean architecture principles
- Designed for integration with Azure and myAI services

## 📞 Support

- Open an [issue](../../issues) for bug reports or feature requests
- Check existing [issues](../../issues) and [pull requests](../../pulls) first

---

**Ready to build something amazing? Get started now! 🚀**