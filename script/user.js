var banUserRequestRoute = "https://bunkie-foja2uwzca-oa.a.run.app/users/admin/ban_user";
var warnUserRequestRoute = "https://bunkie-foja2uwzca-oa.a.run.app/users/admin/warn_user"; 

async function banUser(form) {
    var user_id = form["user-id"].value;
    if (user_id == "") {
        alert("User ID is required to ban a user.");
    } else {
        const requestBody = {
            "token": "a",
            "user_id": user_id
        }

        const response = await fetch(banUserRequestRoute,{
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });
        
        if (response.status == 200) {
            alert("User with ID: " + user_id
                + " is warned with the following message:\n"
                + warn_message);
        } else {
            alert("Failed to warn the user. Error message:\n"
                + response.json())
        }
    }
}

async function warnUser(form) {
    let user_id = form["user-id"].value;
    let warn_message = form["message"].value;
    if (user_id == "") {
        alert("User ID is required to warn a user.");
    } else if (warn_message == "") {
        alert("A message is required to warn a user");
    } else {
        const requestBody = {
            "token": "a",
            "user_id": user_id,
            "warn_message": warn_message
        }
        
        const response = await fetch(warnUserRequestRoute,{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
        });
        
        if (response.status == 200) {
            alert("User with ID: " + user_id
                + " is warned with the following message:\n"
                + warn_message);
        } else {
            alert("Failed to warn the user. Error message:\n"
                + response.json())
        }
    }
}