/*create a function to open the add employee form */
function openaddElement() {
  document.getElementById("form").style.display = "block";
}
function closeForm() {
  document.getElementById("form").style.display = "none";
}
/*create a function to add an employee */
function addEmployee() {
  let employeeName = document.getElementById("name").value;
  let employeeId = document.getElementById("id").value;
  let employeeRole = document.getElementById("role").value;

  if (!employeeName || !employeeId || !employeeRole) {
    alert("Please fill in all fields.");
    return;
  }
  let table = document.querySelector("table");
  let newRow = table.insertRow();

  newRow.insertCell(0).innerText = employeeName;
  newRow.insertCell(1).innerText = employeeId;
  newRow.insertCell(2).innerText = employeeRole;

  document.getElementById("name").value = "";
  document.getElementById("id").value = "";
  document.getElementById("role").value = "";
  document.getElementById("form").style.display = "none";
}