const mainpage = document.getElementById("container")
const fetchButton = document.getElementById("fetchButton")
fetchButton.addEventListener('click',getPostData)

function getPostData(){
    fetch("http://127.0.0.1:8000/api/post")
    .then(res => res.json())
    .then(data => {
        postTemplate = `
        <div class="title">
            ${data.title}
        </div>
        <div class="body">
            ${data.body}
        </div>
        <div class="created_at">
            ${data.created_at}
        </div>
        `
        mainpage.innerHTML = postTemplate+mainpage.innerHTML
    })
}