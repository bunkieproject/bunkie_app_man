var adminLoginRequestRoute = "https://bunkie-foja2uwzca-oa.a.run.app/users/admin/login";

async function validateForm(form) {
    let uname = form["admin-uname"].value;
    let pw = form["admin-pw"].value;
    if (uname == "" || pw == "") {
        alert("Enter a username and a password!");
    } else {
        const requestBody = {
            "username_or_email": uname,
            "password": pw
        }

        const response = await fetch(adminLoginRequestRoute,{
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });
        
        if (response.status == 200) {
            localStorage.setItem("admin-token", response.json().token)
            form.submit()
        } else {
            alert("Failed log in, check your user name and password")
        }
    }
}