# Contributing to myAI Starter

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please be respectful and constructive in all interactions. We aim to foster an open and welcoming environment.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- A GitHub account

### Setting Up Your Development Environment

1. Fork the repository on GitHub

2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/github-copilot-myai-starter.git
   cd github-copilot-myai-starter
   ```

3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/github-copilot-myai-starter.git
   ```

4. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

6. Copy the environment template:
   ```bash
   cp .env.template .env
   ```

## Development Workflow

### Creating a Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Test additions or fixes

### Making Changes

1. Make your changes in your branch
2. Follow the code style guidelines (see below)
3. Add or update tests as needed
4. Update documentation if needed

### Testing Your Changes

#### Backend Tests
```bash
cd backend
pytest
```

#### Code Quality Checks
```bash
# Format code
black app/

# Check linting
flake8 app/

# Type checking
mypy app/
```

#### Manual Testing
1. Start the server:
   ```bash
   python -m app.main
   ```

2. Test in browser: http://localhost:8000
3. Check API docs: http://localhost:8000/api/v1/docs

### Committing Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "feat: add user authentication endpoint"
```

Commit message format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Test changes
- `chore:` - Build process or auxiliary tool changes

### Pushing Changes

```bash
git push origin your-branch-name
```

### Creating a Pull Request

1. Go to GitHub and navigate to your fork
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template:
   - Clear title
   - Description of changes
   - Related issues (if any)
   - Screenshots (for UI changes)
5. Submit the PR

## Code Style Guidelines

### Python Code

Follow PEP 8 and use the provided tools:

```bash
# Auto-format with Black
black app/

# Check with flake8
flake8 app/ --max-line-length=100

# Type hints
mypy app/
```

Key principles:
- Use type hints for function parameters and return values
- Write docstrings for functions, classes, and modules
- Keep functions small and focused
- Use meaningful variable names
- Maximum line length: 100 characters

Example:
```python
from typing import List

def get_items(limit: int = 10) -> List[Item]:
    """
    Get a list of items.
    
    Args:
        limit: Maximum number of items to return
        
    Returns:
        List of Item objects
    """
    return items_db[:limit]
```

### JavaScript Code

- Use ES6+ features
- Use `const` and `let`, not `var`
- Use async/await for asynchronous code
- Add JSDoc comments for functions

Example:
```javascript
/**
 * Fetch items from the API
 * @returns {Promise<Array>} Array of items
 */
async function getItems() {
    const response = await fetch('/api/v1/items');
    return await response.json();
}
```

### CSS Code

- Use CSS variables for colors and common values
- Follow BEM naming convention for classes
- Keep selectors specific but not overly complex
- Group related properties together

## Documentation

### When to Update Documentation

Update documentation when you:
- Add new features
- Change existing functionality
- Fix bugs that affect usage
- Add configuration options
- Change API endpoints

### Documentation Files

- `README.md` - Main project documentation
- `backend/README.md` - Backend-specific documentation
- `frontend/README.md` - Frontend-specific documentation
- `docs/ARCHITECTURE.md` - Architecture documentation
- `CONTRIBUTING.md` - This file

## Testing Guidelines

### Writing Tests

- Write tests for new features
- Ensure tests are isolated and independent
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

Example:
```python
def test_create_item_success():
    # Arrange
    item_data = {"name": "Test", "price": 10.0}
    
    # Act
    response = client.post("/api/v1/items", json=item_data)
    
    # Assert
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

### Test Coverage

Aim for high test coverage, especially for:
- Business logic
- API endpoints
- Error handling
- Edge cases

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] Branch is up to date with main

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Code follows style guidelines
```

## Review Process

1. Automated checks run on PR submission
2. Maintainers review the code
3. Address feedback and push updates
4. Once approved, maintainers will merge

## Common Tasks

### Adding a New API Endpoint

1. Create a new router or add to existing in `backend/app/api/`
2. Define Pydantic models in `backend/app/models/`
3. Implement the endpoint logic
4. Add tests in `backend/tests/`
5. Update API documentation in README

### Adding a Frontend Feature

1. Update HTML in `frontend/public/index.html`
2. Add JavaScript in `frontend/public/app.js`
3. Style in `frontend/public/styles.css`
4. Test in browser
5. Update frontend README if needed

### Adding Configuration Options

1. Add to `backend/app/core/config.py` Settings class
2. Add to `.env.template` with description
3. Document in README
4. Add validation if needed

## Getting Help

- Open an issue for bugs or feature requests
- Tag maintainers in PRs if you need help
- Check existing issues and PRs first

## Recognition

Contributors will be recognized in:
- Git history
- Release notes
- Contributors list (future)

Thank you for contributing to myAI Starter! 🎉
