import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TodoApp = () => {
  const [todos, setTodos] = useState([]);
  const [newTitle, setNewTitle] = useState("");
  const [newDescription, setNewDescription] = useState("");
  const [newUrgency, setNewUrgency] = useState("Low");

  // Fetch todos on component mount
  useEffect(() => {
    axios.get('http://localhost:8000/')
      .then(response => setTodos(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  // Add a new todo
  const addTodo = () => {
    axios.post('http://localhost:8000/', {
      title: newTitle,
      description: newDescription,
      urgency: parseInt(newUrgency, 10)
  })
      .then(response => {
        setTodos([...todos, response.data]);
        setNewTitle("");
        setNewDescription("");
        setNewUrgency("1")
      })
      .catch(error => console.error('Error adding todo:', error));
  };

  return (
    <div>
      <h1>Todo List</h1>
      {todos.map(todo => (
        <div key={todo.id}>
        <strong>{todo.number}. {todo.title}</strong> - {todo.description} <em>(Urgency: {todo.urgency})</em>
      </div>
      ))}
      <input
        value={newTitle}
        onChange={e => setNewTitle(e.target.value)}
        placeholder="Title"
      />
      <input
        value={newDescription}
        onChange={e => setNewDescription(e.target.value)}
        placeholder="Description"
      />
      <select value={newUrgency} onChange={e => setNewUrgency(e.target.value)}>
        <option value="1">Low</option>
        <option value="2">Medium</option>
        <option value="3">High</option>
        <option value="4">Critical</option>
      </select>

      <button onClick={addTodo}>Add Todo</button>
    </div>
  );
};

export default TodoApp;
