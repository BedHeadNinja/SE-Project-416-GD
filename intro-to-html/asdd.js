 function openForm() {
    document.getElementById("popupForm").style.display = "block";
  }

  document.querySelector(".close").onclick = function() {
    document.getElementById("popupForm").style.display = "none";
  }

  function addEmployee() {
    let name = document.getElementById("name").value;
    let id = document.getElementById("empId").value;
    let role = document.getElementById("role").value;

    // Validation: Don't add empty rows
    if(!name || !id || !role) {
      alert("Please fill in all fields");
      return;
    }

    let table = document.querySelector("table");
    let newRow = table.insertRow(-1);

    newRow.insertCell(0).innerText = name;
    newRow.insertCell(1).innerText = id;
    newRow.insertCell(2).innerText = role;

    // Clear inputs and close modal
    document.getElementById("name").value = "";
    document.getElementById("empId").value = "";
    document.getElementById("role").value = "";
    document.getElementById("popupForm").style.display = "none";
  }

  // Close modal if user clicks outside of the box
  window.onclick = function(event) {
    let modal = document.getElementById("popupForm");
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }