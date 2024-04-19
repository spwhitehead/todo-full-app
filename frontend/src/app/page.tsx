
fetch("http://localhost:8000/", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    }).then(fetchTodos);

export default function Home() {
  return <p>Hello World!</p>
}