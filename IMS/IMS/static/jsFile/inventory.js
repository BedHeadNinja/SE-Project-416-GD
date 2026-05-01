function openForm(popupID, buttonID, order = null){
    document.getElementById(popupID).style.display="block";
    // If the order form is being opened, call finalize order
    const popups = document.getElementsByClassName("product-popup");

    // Loop through elements
    for (let element of popups){
        // Hide all elements that aren't the popup
        if (element.id != popupID){
            element.style.display = "none";
        }
    }
    //if (order == null) {
    //    document.getElementById(buttonID).style.display="none";
    //}
}
function closeForm(popupID, buttonID, listID = null){
    // Hide popup, show button
    document.getElementById(popupID).style.display= "none";
    document.getElementById(buttonID).style.display= "block";

    // If the form was an order form, hide checkboxes and delete the order table
    if (listID != null) {
        // Delete the table
        const div = document.getElementById(listID);
        div.remove();
    }
}
function buildTable(rowElements, orderBodyID){
    // Get the div to add the table under, then create a table element
    const orderBody = document.getElementById(orderBodyID),
    parentDiv = document.createElement("div");

    parentDiv.setAttribute("id", "order-table");

    // Build a table of selected products
    for(let id of rowElements){
        const productId = document.createElement("input");
        const idCol = document.createElement("p");
        const quantityCol = document.createElement("input");
        const nameCol = document.createElement('p');

        // Set name attributes
        //nameCol.setAttribute("class", "productNames");
        //nameCol.innerText = id.product_name;

        // Set id attributes
        // NOTE: This element is invisible, and exists only for filling the form with the proper values
        productId.setAttribute("class", "product_ids");
        productId.setAttribute("type", "hidden");
        productId.setAttribute("name", "product_id");
        productId.setAttribute("value", id);

        // Set id column attributes
        //NOTE: This element exists to show the user what products have been selected, without any functionality
        idCol.setAttribute("class", "productIDs");
        idCol.innerText = id;

        // Set quantity attributes
        quantityCol.setAttribute("class", "quantities");
        quantityCol.setAttribute("type", "number");
        quantityCol.setAttribute("name", "quantity");
        quantityCol.required = true;

        // Create a div to hold both elements
        const div = document.createElement("div");
        div.setAttribute("class", "lineitem-div");

        // Add the elements within the div
        //div.appendChild(nameCol);
        div.appendChild(productId);
        div.appendChild(idCol);
        div.appendChild(quantityCol);

        // Add the div to the parent
        parentDiv.appendChild(div);
    }
    orderBody.appendChild(parentDiv);
}
function showOrderForm(showOrder){
    // Get the checkboxes for order styling
    const products = document.getElementsByClassName('add-order-column');

    // If showOrder is true, show order elements and hide inventory elements. Otherwise, do the opposite
    if(showOrder == true){
        // Loop through list of products
        for (let element of products){
            element.style.display="block";
        }
        document.getElementById('add-product-button').style.display="none";
        document.getElementById('remove-product-button').style.display="none";
        document.getElementById('update-quantity-button').style.display="none";
        document.getElementById('set-threshold-button').style.display="none";
        document.getElementById('order-product-button').style.display="none";
        document.getElementById('finalize-order-button').style.display="block";
        document.getElementById('cancel-order-button').style.display="block";
    }
    else{
        // Loop through list of products
        for (const element of products){
            element.style.display="none";
        }
        document.getElementById('add-product-button').style.display="block";
        document.getElementById('remove-product-button').style.display="block";
        document.getElementById('update-quantity-button').style.display="block";
        document.getElementById('set-threshold-button').style.display="block";
        document.getElementById('order-product-button').style.display="block";
        document.getElementById('finalize-order-button').style.display="none";
        document.getElementById('cancel-order-button').style.display="none";
    }
}
function finalizeOrder(){
    // Get all checkbox elements
    const products = document.getElementsByClassName('order-checkbox');
    // Create a new array for selected products
    const selectedProducts = [];
    // Loop through list of clicked products
    for (let element of products){
        if(element.checked == true){
            // Add the element's id to the list of selected products
            selectedProducts.push(element.id);
        }
    }

    // If no products have been selected, return false
    if (selectedProducts.length == 0){
        return false;
    }
    else{
        // Call buildTable and send the selected products
        buildTable(selectedProducts, "order-body");
        return true;
    }
}
function tableSearch(){
    // Get search input
    const query = document.getElementById("search");

    // Set value for filtering search results
    const filter = query.value.toLowerCase();

    // Get the inventory table and table row
    const table = document.getElementById("inventory-table");
    const tr = table.getElementsByTagName("tr");

    // Search the table for results matching the query
    for (let i = 0; i < tr.length; i++){
        td = tr[i].getElementsByTagName("td")[2];

        // If contentx exist, evaluate them
        if (td){

            const text = td.textContent || td.innerText;

            // If the contents are within a range of the filter, show them
            if (text.toLowerCase().indexOf(filter) <= -1){
                tr[i].style.display = "none";
            }
            else{
                tr[i].style.display = "table-row";
            }
        }
    }

}
