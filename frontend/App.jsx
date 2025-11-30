import { useEffect, useState } from "react";
import "./App.css";

const API_BASE_URL = "http://localhost:8001/api/v1";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [newTaskTitle, setNewTaskTitle] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [creating, setCreating] = useState(false);

  // Fetch all tasks
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${API_BASE_URL}/tasks/`);
      if (!response.ok) {
        throw new Error(`Failed to fetch tasks: ${response.statusText}`);
      }
      const data = await response.json();
      setTasks(data);
    } catch (err) {
      setError(err.message);
      console.error("Error fetching tasks:", err);
    } finally {
      setLoading(false);
    }
  };

  // Create a new task
  const createTask = async (e) => {
    e.preventDefault();
    if (!newTaskTitle.trim()) return;

    setCreating(true);
    setError(null);
    try {
      const response = await fetch(`${API_BASE_URL}/tasks/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title: newTaskTitle }),
      });

      if (!response.ok) {
        throw new Error(`Failed to create task: ${response.statusText}`);
      }

      const newTask = await response.json();
      setTasks([...tasks, newTask]);
      setNewTaskTitle("");
    } catch (err) {
      setError(err.message);
      console.error("Error creating task:", err);
    } finally {
      setCreating(false);
    }
  };

  // Toggle task done status
  const toggleTask = async (taskId) => {
    setError(null);
    try {
      const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/toggle`, {
        method: "POST",
      });

      if (!response.ok) {
        throw new Error(`Failed to toggle task: ${response.statusText}`);
      }

      const updatedTask = await response.json();
      setTasks(tasks.map((t) => (t.id === taskId ? updatedTask : t)));
    } catch (err) {
      setError(err.message);
      console.error("Error toggling task:", err);
    }
  };

  // Delete a task
  const deleteTask = async (taskId) => {
    setError(null);
    try {
      const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error(`Failed to delete task: ${response.statusText}`);
      }

      setTasks(tasks.filter((t) => t.id !== taskId));
    } catch (err) {
      setError(err.message);
      console.error("Error deleting task:", err);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <header>
          <h1>📝 Mini Tasks</h1>
          <p className="subtitle">A simple task management app</p>
        </header>

        {error && (
          <div className="error-banner">
            <span>⚠️ {error}</span>
            <button onClick={() => setError(null)}>✕</button>
          </div>
        )}

        <form onSubmit={createTask} className="task-form">
          <input
            type="text"
            value={newTaskTitle}
            onChange={(e) => setNewTaskTitle(e.target.value)}
            placeholder="What needs to be done?"
            disabled={creating}
            className="task-input"
          />
          <button type="submit" disabled={creating || !newTaskTitle.trim()} className="add-button">
            {creating ? "Adding..." : "Add Task"}
          </button>
        </form>

        <div className="tasks-container">
          {loading ? (
            <div className="loading">Loading tasks...</div>
          ) : tasks.length === 0 ? (
            <div className="empty-state">
              <p>🎉 No tasks yet! Add one above to get started.</p>
            </div>
          ) : (
            <div className="tasks-list">
              {tasks.map((task) => (
                <div key={task.id} className={`task-item ${task.done ? "done" : ""}`}>
                  <label className="task-checkbox">
                    <input
                      type="checkbox"
                      checked={task.done}
                      onChange={() => toggleTask(task.id)}
                    />
                    <span className="checkmark"></span>
                  </label>
                  <span className="task-title">{task.title}</span>
                  <button
                    onClick={() => deleteTask(task.id)}
                    className="delete-button"
                    title="Delete task"
                  >
                    🗑️
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>

        <footer className="stats">
          <span>
            {tasks.filter((t) => !t.done).length} active
          </span>
          <span>•</span>
          <span>
            {tasks.filter((t) => t.done).length} completed
          </span>
          <span>•</span>
          <span>
            {tasks.length} total
          </span>
        </footer>
      </div>
    </div>
  );
}

// Made with Bob
