function predictPrice() {
    event.preventDefault();
    const brand = document.getElementById('brand').value;
    const category = document.getElementById('category').value;
    const color = document.getElementById('color').value;
    const size = document.getElementById('size').value;
    const material = document.getElementById('material').value;

    if (!brand || brand === "Select Brand" || !category || category === "Select Category" || !color || color === "Select Color" || !size || size === "Select Size" || !material || material === "Select Material") {
        alert("Please select options for all fields.");
        return false;
    }
    document.getElementById('pricePredictionForm').submit();
    return true;
    
}
