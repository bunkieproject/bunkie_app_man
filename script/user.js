var banUserRequestRoute = "";
var warnUserRequestRoute = ""; 

function banUser(form) {
    var user_id = form["user-id"].value;
    if (user_id == "") {
        alert("User ID is required to ban a user.");
    } else {
        // TODO : send ban request
    }
}

function warnUser(form) {
    let user_id = form["user-id"].value;
    let warn_message = form["message"].value;
    if (user_id == "") {
        alert("User ID is required to warn a user.");
    } else if (warn_message == "") {
        alert("A message is required to warn a user");
    } else {
        // TODO : send warn request
    }
}