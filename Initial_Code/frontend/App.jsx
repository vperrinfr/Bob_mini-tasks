import { useEffect, useState } from "react";

export default function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("/tasks")
      .then(r => r.json())
      .then(setTasks);
  }, []);

  function toggle(id) {
    fetch(`/task/${id}/toggle`, { method: "POST"});
  }

  return (
    <div>
      <h1>Mini Tasks</h1>
      {tasks.map(t => (
        <div key={t.id}>
          <input type="checkbox" checked={t.done} onChange={() => toggle(t.id)} />
          {t.title}
        </div>
      ))}
    </div>
  );
}
