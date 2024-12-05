fetch("http://127.0.0.1:8000/api/token/", {
  method: "post",
  headers: new Headers({ "Content-Type": "application/json" }),
  body: JSON.stringify({ username: "abc", password: "123" }),
})
  .then((resp) => resp.json())
  .then((data) => {
    console.log(data);
    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);
  });
