document.addEventListener("DOMContentLoaded", function main(event) {
    


    let form = document.getElementById('form')
    form.addEventListener("submit", (e) =>{
        e.preventDefault()
        let username = e.target.username.value
        let password = e.target.password.value
        const options = {
            method : 'POST',
            headers: {
                'Content-Type' : 'application/json',
                'X-CSRFToken': csrf
            },
            body : JSON.stringify({
                username: username,
                password: password,
            }),
        };
        fetch(api, options)
        .then(data => {
            if (!data.ok){
                addToHeader("failed to authenticate")
                throw Error(data.status)
            }
            return data.json();
        }).then(update =>{
                addToHeader("authenticated successfully")
            
        })
    })

})


function addToHeader(msg) {
    document.querySelector('header').innerHTML =`
    <div class="alert alert-primary mb-0 text-center" role="alert">
        ${msg}
    </div>`
}