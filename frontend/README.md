# Mini Tasks Frontend

A modern React frontend for the Mini Tasks application, built with Vite.

## Features

- ✅ Clean, modern UI with gradient design
- ✅ Real-time task management (create, toggle, delete)
- ✅ Error handling and loading states
- ✅ Responsive design
- ✅ Task statistics (active, completed, total)
- ✅ Smooth animations and transitions

## Tech Stack

- **React 18** - UI library
- **Vite** - Build tool and dev server
- **CSS3** - Styling with gradients and animations

## Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

3. **Access the app:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8001

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## API Configuration

The frontend connects to the backend API at `http://localhost:8001/api/v1`.

To change the API URL, edit the `API_BASE_URL` constant in `App.jsx`:

```javascript
const API_BASE_URL = "http://localhost:8001/api/v1";
```

## Features Overview

### Task Management
- **Create tasks** - Add new tasks with a title
- **Toggle completion** - Mark tasks as done/undone
- **Delete tasks** - Remove tasks permanently
- **View statistics** - See active, completed, and total task counts

### UI/UX
- **Loading states** - Visual feedback during API calls
- **Error handling** - User-friendly error messages
- **Empty state** - Helpful message when no tasks exist
- **Responsive design** - Works on mobile and desktop
- **Smooth animations** - Polished user experience

## Project Structure

```
frontend/
├── index.html          # HTML entry point
├── main.jsx           # React entry point
├── App.jsx            # Main application component
├── App.css            # Application styles
├── package.json       # Dependencies and scripts
├── vite.config.js     # Vite configuration
└── README.md          # This file
```

## Development

The app uses Vite's hot module replacement (HMR) for instant updates during development.

### Adding New Features

1. Update `App.jsx` for new functionality
2. Add styles to `App.css`
3. Test with the backend API running

### Building for Production

```bash
npm run build
```

This creates an optimized build in the `dist/` directory.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

### CORS Errors
Make sure the backend CORS configuration includes your frontend URL:
```python
# backend/main.py
allow_origins=["http://localhost:3000"]
```

### API Connection Issues
1. Verify backend is running on port 8001
2. Check `API_BASE_URL` in `App.jsx`
3. Ensure CORS is properly configured

### Build Errors
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install