# Initial Code - Before Bob's Refactoring

This folder contains documentation of the **original buggy code** before Bob's improvements.

## ⚠️ Warning

This is the **BEFORE** version - it contains multiple bugs and bad practices. **Do not use this code in production!**

## 🐛 Known Issues

### Critical Bugs

1. **Database Session Leaks (Memory Leak)**
   - Sessions created but never closed
   - Will crash under load
   - Location: `services/task_service.py`

2. **Dangerous autocommit=True**
   - Disables transaction management
   - No rollback capability
   - Data corruption risk
   - Location: `database.py`

3. **Frontend API URL Mismatch**
   - Frontend calls `/task/{id}/toggle`
   - Backend expects `/tasks/{id}/toggle`
   - Results in 404 errors
   - Location: `frontend/App.jsx`

4. **Missing Error Handling**
   - Silent failures
   - Returns None without indication
   - No HTTP exceptions
   - Location: `services/task_service.py`

### High Priority Issues

5. **No Request Validation**
   - Uses raw `dict` instead of Pydantic
   - No type safety
   - Can accept invalid data
   - Location: `routers/tasks.py`

6. **Missing CORS Configuration**
   - Frontend requests blocked
   - No cross-origin support
   - Location: `main.py`

7. **No Error Handling in Frontend**
   - Silent failures
   - No loading states
   - Poor user experience
   - Location: `frontend/App.jsx`

8. **No State Update After Toggle**
   - UI doesn't reflect changes
   - Requires page refresh
   - Location: `frontend/App.jsx`

## 📝 Original Code Structure

```
Initial Code (Conceptual):
├── backend/
│   ├── main.py              # Basic FastAPI app
│   ├── database.py          # Sync DB with autocommit=True ❌
│   ├── models.py            # SQLAlchemy models (OK)
│   ├── routers/
│   │   └── tasks.py        # No validation, raw dicts ❌
│   └── services/
│       └── task_service.py # Session leaks, no error handling ❌
│
└── frontend/
    └── App.jsx             # Basic UI, wrong API URLs ❌
```

## 🔍 Code Examples (Buggy)

### Database Configuration (WRONG)
```python
# database.py - BUGGY VERSION
SessionLocal = sessionmaker(
    autocommit=True,      # ❌ DANGEROUS!
    autoflush=True,       # ❌ BAD PRACTICE!
    bind=engine
)
```

### Service Layer (WRONG)
```python
# task_service.py - BUGGY VERSION
def get_all_tasks():
    db = SessionLocal()
    return db.query(Task).all()  # ❌ Session never closed!
```

### Router (WRONG)
```python
# routers/tasks.py - BUGGY VERSION
@router.post("/")
def new_task(data: dict):  # ❌ No validation!
    return create_task(data.get("title"))
```

### Frontend (WRONG)
```javascript
// App.jsx - BUGGY VERSION
function toggle(id) {
  fetch(`/task/${id}/toggle`, { method: "POST"});  // ❌ Wrong URL!
  // ❌ No error handling, no state update
}
```

## 📊 Issues Summary

| Category | Count | Severity |
|----------|-------|----------|
| Critical | 4 | 🔴 High |
| High Priority | 4 | 🟠 Medium |
| Medium Priority | 6 | 🟡 Low |
| Code Quality | 6 | 🔵 Info |
| **Total** | **20** | - |

## 🚫 What NOT to Do

Based on this code, here's what to avoid:

1. ❌ Never use `autocommit=True` in SQLAlchemy
2. ❌ Never create database sessions without closing them
3. ❌ Never use raw `dict` for API inputs
4. ❌ Never ignore error handling
5. ❌ Never hardcode configuration
6. ❌ Never skip CORS configuration
7. ❌ Never use sync operations when async is available
8. ❌ Never return `None` silently on errors

## ✅ See the Fixed Version

For the corrected, production-ready code, see:
- **Result_After_Bob/** folder
- **REFACTORING_SUMMARY.md** for detailed changes

## 📚 Learning Resources

To understand why these are bugs:
1. [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/)
2. [SQLAlchemy Session Basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)
3. [Pydantic Validation](https://docs.pydantic.dev/)
4. [React Error Handling](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)

---

**⚠️ This code is for educational purposes only - showing what NOT to do!**

**✅ Use the code in `Result_After_Bob/` folder instead**