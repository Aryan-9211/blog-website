function login() {
  console.log("HI");
  var username = document.getElementById("loginUsername").value;
  var password = document.getElementById("loginPassword").value;
  var csrf = document.getElementById("csrf").value;

  console.log(username, password, csrf);

  var data = {
    username: username,
    password: password,
  };

  fetch("/api/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrf,
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      console.log(result);
      if (result.status == 200) {
        window.location.href = "/";
      }
    })
    .catch((error) => console.error(error));

  console.log("END");
}
