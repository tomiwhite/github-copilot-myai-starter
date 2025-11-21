# Frontend

A clean, minimal frontend application built with vanilla HTML, CSS, and JavaScript.

## Features

- **Simple & Clean**: No framework overhead, pure web technologies
- **Responsive Design**: Works on desktop and mobile devices
- **Modern CSS**: Uses CSS variables and grid layout
- **API Integration**: Demonstrates connection to the backend API
- **Easy to Extend**: Clear structure for adding features

## Project Structure

```
frontend/
├── public/
│   ├── index.html    # Main HTML file
│   ├── app.js        # JavaScript application logic
│   └── styles.css    # Stylesheet
└── src/              # Future source files (if using build tools)
```

## Getting Started

The frontend is served directly by the FastAPI backend. No separate build step is required.

### Prerequisites

- Backend API running (see backend/README.md)

### Accessing the Frontend

1. Start the backend server
2. Navigate to http://localhost:8000
3. The frontend will be served automatically

## Features Overview

### Welcome Section
Introduction to the starter application with key features highlighted.

### API Demo
Interactive buttons to test API endpoints:
- Health check endpoint
- Get items example

### Quick Links
Direct links to:
- Swagger API documentation
- ReDoc alternative documentation
- GitHub repository

## Customization

### Styling

Edit `styles.css` to customize:
- Colors (defined as CSS variables in `:root`)
- Layout and spacing
- Typography
- Responsive breakpoints

### Adding New Features

1. **HTML**: Add new sections in `index.html`
2. **JavaScript**: Add functionality in `app.js`
3. **Styles**: Add CSS rules in `styles.css`

### Example: Adding a New API Call

```javascript
// In app.js
async function myNewFunction() {
  try {
    const response = await fetch("/api/v1/my-endpoint");
    const data = await response.json();
    displayResponse(data);
  } catch (error) {
    displayError(error.message);
  }
}

// Add event listener
document.getElementById("my-button").addEventListener("click", myNewFunction);
```

## Upgrading to a Framework

This starter uses vanilla JavaScript to keep it simple. When your application grows, you can migrate to:

### React
```bash
npx create-react-app frontend-app
```

### Vue
```bash
npm init vue@latest
```

### Svelte
```bash
npm create svelte@latest frontend-app
```

## Static Assets

Place images, fonts, and other static assets in the `public` directory. They'll be accessible at `/static/your-file`.

## Environment-Specific Configuration

For different environments, you can:
1. Use different backend URLs in JavaScript
2. Create build scripts that inject environment variables
3. Use a `.env` file with build tools

## Browser Support

The current implementation supports:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)

For older browser support, consider adding polyfills or using a build tool like Babel.

## License

See LICENSE file in the root directory.
