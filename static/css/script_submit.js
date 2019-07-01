function recogeDatos() {
  var pass = document.querySelector("#password").value;
  var number = document.querySelector("#number_give").value;
  var result = {
    code: pass + number
  };
  console.log(result);
  return result;
}

var mensaje = recogeDatos();

function sendData(mensaje) {
  var XHR = new XMLHttpRequest();
  var FD = new FormData();

  // Push our data into our FormData object
  for (name in mensaje) {
    FD.append(name, mensaje[name]);
  }

  // // Define what happens on successful data submission
  // XHR.addEventListener("load", function(event) {
  //   alert("Yeah! Data sent and response loaded.");
  // });

  // // Define what happens in case of error
  // XHR.addEventListener("error", function(event) {
  //   alert("Oops! Something went wrong.");
  // });

  // Set up our request
  XHR.open("POST", "http://localhost:5000/api/try_number");

  // Send our FormData object; HTTP headers are set automatically
  XHR.send(FD);
}
// document
//   .querySelector("#participacion")
//   .addEventListener("submit", recogeDatos);
