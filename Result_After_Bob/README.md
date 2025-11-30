# 📝 Mini Tasks

A modern, full-stack task management application built with FastAPI and React.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-green)
![React](https://img.shields.io/badge/React-18.2-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- ✅ **Full CRUD Operations** - Create, read, update, and delete tasks
- ✅ **Modern Async Backend** - FastAPI with async SQLAlchemy
- ✅ **Beautiful UI** - Responsive React frontend with gradient design
- ✅ **Type Safety** - Pydantic validation and TypeScript-ready
- ✅ **Real-time Updates** - Instant UI feedback
- ✅ **Error Handling** - Comprehensive error messages
- ✅ **API Documentation** - Auto-generated OpenAPI/Swagger docs
- ✅ **Clean Architecture** - Separation of concerns (routes → services → database)

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│   Frontend (React + Vite)               │
│   Port: 3000                            │
│   - Modern UI with animations           │
│   - Error handling & loading states     │
└──────────────┬──────────────────────────┘
               │ REST API (CORS enabled)
               ▼
┌─────────────────────────────────────────┐
│   Backend (FastAPI)                     │
│   Port: 8001                            │
│   - Async operations                    │
│   - Pydantic validation                 │
│   - Dependency injection                │
└──────────────┬──────────────────────────┘
               │ SQLAlchemy ORM (Async)
               ▼
┌─────────────────────────────────────────┐
│   Database (SQLite + aiosqlite)         │
│   - Async operations                    │
│   - Transaction management              │
└─────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Node.js 18+
- npm or yarn

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the server
python3 -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8001
```

Backend will be available at:
- API: http://localhost:8001/api/v1
- Docs: http://localhost:8001/docs
- Health: http://localhost:8001/health

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will be available at: http://localhost:3000

## 📁 Project Structure

```
mini-tasks/
├── backend/
│   ├── main.py              # FastAPI app initialization
│   ├── database.py          # Async database configuration
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic validation models
│   │   ├── __init__.py
│   │   └── task.py
│   ├── routers/             # API endpoints
│   │   ├── __init__.py
│   │   └── tasks.py
│   ├── services/            # Business logic layer
│   │   ├── __init__.py
│   │   └── task_service.py
│   ├── tests/               # Test suite
│   │   └── test_tasks.py
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Environment variables template
│   └── README.md            # Backend documentation
│
├── frontend/
│   ├── index.html           # HTML entry point
│   ├── main.jsx             # React entry point
│   ├── App.jsx              # Main application component
│   ├── App.css              # Application styles
│   ├── package.json         # Node dependencies
│   ├── vite.config.js       # Vite configuration
│   └── README.md            # Frontend documentation
│
├── .gitignore               # Git ignore rules
├── README.md                # This file
└── REFACTORING_SUMMARY.md   # Detailed refactoring notes
```

## 🔌 API Endpoints

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/tasks/` | Get all tasks |
| GET | `/api/v1/tasks/{id}` | Get task by ID |
| POST | `/api/v1/tasks/` | Create new task |
| PATCH | `/api/v1/tasks/{id}` | Update task |
| POST | `/api/v1/tasks/{id}/toggle` | Toggle task completion |
| DELETE | `/api/v1/tasks/{id}` | Delete task |

### System

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/docs` | Interactive API documentation |

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework
- **SQLAlchemy 2.0** - Async ORM
- **aiosqlite** - Async SQLite driver
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **Vite** - Build tool and dev server
- **CSS3** - Styling with gradients and animations

## 🎯 Key Features

### Backend Best Practices
- ✅ Fully async operations
- ✅ Dependency injection for database sessions
- ✅ Pydantic models for validation
- ✅ Proper error handling with HTTP exceptions
- ✅ CORS configuration
- ✅ API versioning (`/api/v1`)
- ✅ Clean architecture (separation of concerns)
- ✅ Type hints throughout
- ✅ Comprehensive documentation

### Frontend Features
- ✅ Modern, responsive UI
- ✅ Real-time task updates
- ✅ Error handling and loading states
- ✅ Task statistics (active, completed, total)
- ✅ Smooth animations and transitions
- ✅ Mobile-friendly design

## 📖 Documentation

- **Backend README**: [backend/README.md](backend/README.md)
- **Frontend README**: [frontend/README.md](frontend/README.md)
- **Refactoring Summary**: [REFACTORING_SUMMARY.md](REFACTORING_SUMMARY.md)
- **API Docs**: http://localhost:8001/docs (when running)

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests (if configured)
cd frontend
npm test
```

## 🔧 Configuration

### Backend Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=sqlite+aiosqlite:///./tasks.db
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

See `backend/.env.example` for all available options.

### Frontend Configuration

Update `API_BASE_URL` in `frontend/App.jsx` if backend runs on a different port:

```javascript
const API_BASE_URL = "http://localhost:8001/api/v1";
```

## 🚢 Deployment

### Backend (Production)

```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run with production settings
uvicorn backend.main:app --host 0.0.0.0 --port 8001 --workers 4
```

### Frontend (Production)

```bash
# Build for production
cd frontend
npm run build

# Serve the dist/ directory with any static file server
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- UI powered by [React](https://react.dev/)
- Bundled with [Vite](https://vitejs.dev/)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ using FastAPI and React**