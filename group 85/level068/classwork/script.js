  const routes = [
  { path: "/", content: "content for home page" },
  { path: "/dashboard", content: "content for dashboard" },
  { path: "/messages", content: "content for messages" }
];

function go(requestedPath) {
    const route = routes.find(r => r.path === requestedPath);
    document.getElementById("view").innerText = route.content;
}