// let api = '{{api}}'
document.addEventListener("DOMContentLoaded", (event) =>{
    let form = document.getElementById("form")
    form.addEventListener("submit", (e) =>{
        e.preventDefault();
        let username = e.target.username.value
        let password = e.target.password.value
        let password2 = e.target.password2.value
        if (password!==password2){
            addToHeader("passwords are not match")
            throw Error()
        }else{
            apiCalling({
                username:username,
                password:password,
                password2:password2,
                
            })
        }
    })
})
    


function addToHeader(msg) {
    document.querySelector('header').innerHTML =`
    <div class="alert alert-primary mb-0 text-center" role="alert">
        ${msg}
    </div>`
}

function apiCalling(params) {
    let options ={
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        body : JSON.stringify({
            username : params.username,
            password : params.password,
            password2: params.password2
        })
    };
    let api_status = 'Registered successfully'
    fetch(api, options)
    .then(response => {
        if (!response.ok) {
            api_status = response.statusText
        }
        addToHeader(api_status)
        return response.json()
    })
}
