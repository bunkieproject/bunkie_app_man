var config = {
    "usernames": [
        "3c923ff7e31484b7b3ef54eb57357a5493d19ea3c7d265c6db5f6c507f96590f",
        "c89976ddf33c384d048c0101478e3e1ce4323492d7559f9f664131c654d828a5",
        "b6a97e10416407a58bfbac62a44d1f66b98fa88356a2125e033e5190c276ce6d",
        "ae75cb6e20a5a6dfa69e958ee2dfaa82495506bcc1d336f2ef1498d96c20fefe"
    ],
    "password": "d6465be2f1a7a92dd1c7ce2bd416be47b1195018ba93cf3e7947a3b611c0af27"
}

function hash(string) {
    const utf8 = new TextEncoder().encode(string);
    return crypto.subtle.digest('SHA-256', utf8).then((hashBuffer) => {
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      const hashHex = hashArray
        .map((bytes) => bytes.toString(16).padStart(2, '0'))
        .join('');
      return hashHex;
    });
}

async function validateForm(form) {
    let hash_uname = await hash(form["admin-uname"].value);
    let hash_pw = await hash(form["admin-pw"].value);
    if (config.usernames.includes(hash_uname) && hash_pw == config.password) {
        form.submit();
    } else {
        alert("Username or password is wrong!");
    }
}