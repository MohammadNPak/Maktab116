function loadPage(page) {
  history.pushState({ page }, "", `/${page}`);
  if (page === "home") {
    contentDiv.innerHTML = "<h2>Home</h2><p>Welcome to the homepage!</p>";
  } else if (page === "about") {
    contentDiv.innerHTML = "<h2>About</h2><p>About this SPA.</p>";
  } else if (page === "users") {
    fetchUsers();
  }
}

// Handle back/forward navigation
window.onpopstate = (event) => {
  const page = event.state ? event.state.page : "home";
  loadPage(page);
};
