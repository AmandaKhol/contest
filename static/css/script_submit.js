function recogeDatos() {
  var pass = document.querySelector("#password").value;
  var number = document.querySelector("#number_give").value;
  var result = {
    code: pass + number
  };
  console.log(result);
  return result;
}
document
  .querySelector("#participacion")
  .addEventListener("submit", recogeDatos);
