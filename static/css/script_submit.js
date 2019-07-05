const element = document.getElementById("amandaForm");

element.addEventListener("submit", function(event) {
  event.preventDefault();

  inputs = event.target.getElementsByTagName("input");

  let number = inputs.number_given.value;
  let password = inputs.password_given.value;

  let object = JSON.stringify({ code: password + number });

  var props = {
    method: "POST", // or 'PUT'
    body: object,
    headers: {
      "Content-Type": "application/json"
    }
  };

  fetch("http://localhost:5000/api/try_number", props)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      console.log(data);
      document.getElementById("messageScreen").innerText = data.message;
    });
});
