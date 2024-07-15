document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const formData = new FormData(this); // Use the form element directly to create FormData

    // Send the file to the server using the fetch API
    const response = await fetch(this.action, {
        method: this.method,
        body: formData,
    });

    const result = await response.json(); // Parse the JSON response from the server
    document.getElementById('result').textContent = result.message; // Display the server response message

    // If the server returns license plate details, display them
    if (result.license_details) {
        document.getElementById('details').textContent = `License Plate: ${result.plate_text}`;
    }
});
