# Mini Tasks Backend API

A modern, async FastAPI backend for task management following best practices.

## Features

- ✅ Fully async with SQLAlchemy 2.0
- ✅ Proper dependency injection for database sessions
- ✅ Pydantic models for request/response validation
- ✅ Comprehensive error handling
- ✅ CORS configuration
- ✅ API versioning
- ✅ OpenAPI documentation
- ✅ Type hints throughout

## Project Structure

```
backend/
├── main.py                 # FastAPI app initialization, CORS, lifespan
├── database.py             # Async database configuration and dependency
├── models.py               # SQLAlchemy ORM models
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── schemas/               # Pydantic schemas
│   ├── __init__.py
│   └── task.py           # Task request/response models
├── routers/              # API endpoints
│   ├── __init__.py
│   └── tasks.py         # Task CRUD endpoints
├── services/            # Business logic layer
│   ├── __init__.py
│   └── task_service.py # Task operations
└── tests/              # Test suite
    └── test_tasks.py

```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment (optional):**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Run the server:**
   ```bash
   uvicorn backend.main:app --reload
   ```

4. **Access the API:**
   - API: http://localhost:8000/api/v1
   - Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/health

## API Endpoints

### Tasks

- `GET /api/v1/tasks/` - Get all tasks
- `GET /api/v1/tasks/{id}` - Get task by ID
- `POST /api/v1/tasks/` - Create new task
- `PATCH /api/v1/tasks/{id}` - Update task
- `POST /api/v1/tasks/{id}/toggle` - Toggle task done status
- `DELETE /api/v1/tasks/{id}` - Delete task

## Key Improvements

### 1. Async Database Operations
- Uses `aiosqlite` for async SQLite
- Proper async/await throughout
- Non-blocking I/O operations

### 2. Dependency Injection
- Database sessions managed via FastAPI dependencies
- Automatic session lifecycle (commit/rollback/close)
- No manual session management needed

### 3. Pydantic Validation
- `TaskCreate` - validates task creation
- `TaskUpdate` - validates partial updates
- `TaskResponse` - ensures consistent responses
- Automatic OpenAPI schema generation

### 4. Proper Error Handling
- HTTP exceptions with appropriate status codes
- 404 for not found resources
- 201 for created resources
- 204 for successful deletions

### 5. Clean Architecture
- Separation of concerns (routers → services → models)
- Business logic isolated in service layer
- Easy to test and maintain

### 6. Configuration Management
- Environment variables via `.env`
- Configurable database URL
- CORS origins configuration

## Database Configuration

The app uses SQLite by default with async support. To use PostgreSQL:

1. Install asyncpg: `pip install asyncpg`
2. Update DATABASE_URL in `.env`:
   ```
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
   ```

## Development

Run with auto-reload:
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Run tests:
```bash
pytest backend/tests/
```

## Production Considerations

- Use PostgreSQL instead of SQLite
- Add rate limiting (e.g., slowapi)
- Implement authentication/authorization
- Add logging and monitoring
- Use environment-specific configs
- Set up database migrations (Alembic)
- Configure proper CORS origins
- Use a production ASGI server (uvicorn with workers)