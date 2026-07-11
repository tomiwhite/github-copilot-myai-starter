# Backend API

A modern FastAPI-based backend application designed for scalability and integration with Azure and myAI services.

## Features

- **FastAPI Framework**: High-performance async API with automatic documentation
- **Clean Architecture**: Organized codebase with separation of concerns
- **Environment Configuration**: Easy configuration via environment variables
- **Health Checks**: Built-in health and readiness endpoints
- **API Versioning**: Structured API with version prefix support
- **CORS Support**: Configurable cross-origin resource sharing
- **Azure Ready**: Placeholders for Azure services integration
- **myAI Integration**: Ready for myAI modules and services

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # Application entry point
│   ├── api/              # API routes
│   │   ├── health.py     # Health check endpoints
│   │   └── example.py    # Example CRUD endpoints
│   ├── core/             # Core functionality
│   │   └── config.py     # Configuration management
│   └── models/           # Data models
├── tests/                # Test files
└── requirements.txt      # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file (copy from `.env.template` in the root):
   ```bash
   cp ../.env.template .env
   ```

4. Edit `.env` with your configuration values

### Running the Application

Start the development server:

```bash
python -m app.main
```

Or with hot-reload using uvicorn directly:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Interactive docs (Swagger): http://localhost:8000/api/v1/docs
- Alternative docs (ReDoc): http://localhost:8000/api/v1/redoc

## API Endpoints

### Health Checks

- `GET /api/v1/health` - Basic health check
- `GET /api/v1/ready` - Readiness probe

### Example CRUD

- `GET /api/v1/items` - Get all items
- `GET /api/v1/items/{id}` - Get specific item
- `POST /api/v1/items` - Create new item
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

### Info

- `GET /info` - Application information

## Configuration

Configuration is managed through environment variables. See `.env.template` for all available options.

Key configurations:
- `APP_NAME`: Application name
- `DEBUG`: Enable debug mode (True/False)
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `CORS_ORIGINS`: Allowed CORS origins

### Azure Integration (Placeholders)

The application includes placeholders for Azure services:
- `AZURE_TENANT_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_SUBSCRIPTION_ID`

### myAI Integration (Placeholders)

Ready for myAI integration:
- `MYAI_API_KEY`
- `MYAI_ENDPOINT`

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black app/
```

### Linting

```bash
flake8 app/
```

### Type Checking

```bash
mypy app/
```

## Extending the Application

1. **Add New Endpoints**: Create new router files in `app/api/` and include them in `main.py`
2. **Add Models**: Define Pydantic models in `app/models/`
3. **Add Business Logic**: Create service modules in `app/core/` or `app/services/`
4. **Add Tests**: Create test files in `tests/` following the structure of the app

## Docker Support

See the main repository README for Docker deployment instructions.

## License

See LICENSE file in the root directory.
