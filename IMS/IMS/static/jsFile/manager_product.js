/*create a function to open the add product form */ 
function openaddElement() {
  document.getElementById("form").style.display = "block";
}
function closeForm() {
  document.getElementById("form").style.display = "none";
}

/*create a function to add a product */ 
function addProduct() {
  let name = document.getElementById("name").value;
  let id = document.getElementById("id").value;
  let count = document.getElementById("count").value;
  let expDate = document.getElementById("expDate").value;

  if (!name || !id || !count || !expDate) {
    alert("Please fill in all fields.");
    return;
  }
  let table = document.querySelector("table");
  let newRow = table.insertRow();

  newRow.insertCell(0).innerText = name;
  newRow.insertCell(1).innerText = id;
  newRow.insertCell(2).innerText = count;
  newRow.insertCell(3).innerText = expDate;

  document.getElementById("name").value = "";
  document.getElementById("id").value = "";
  document.getElementById("count").value = "";
  document.getElementById("expDate").value = "";
  document.getElementById("form").style.display = "none";
}