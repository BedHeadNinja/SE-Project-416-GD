function dropdownHandle() {
    if (document.getElementById("dropdown-content").style.display == "block") {
        closeDropDown();
    } 
    else {
        document.getElementById("dropdown-content").style.display = "block"
    }
}

function closeDropDown() {
    document.getElementById("dropdown-content").style.display = "none";
}