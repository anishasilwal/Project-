document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const formData = new FormData(); // Create a new FormData object to hold the file data
    const fileField = document.getElementById('file'); // Get the file input element
    formData.append('file', fileField.files[0]); // Append the selected file to the FormData object

    // Fetch CSRF token from cookie
    const csrftoken = getCookie('csrftoken');

    // Send the file to the server using the fetch API
    try {
        const response = await fetch('/upload/', {
            method: 'POST', // Use the POST method to send data
            body: formData, // Set the request body to the FormData object
            headers: {
                'X-CSRFToken': csrftoken  // Include CSRF token in headers
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json(); // Parse the JSON response from the server
        document.getElementById('result').textContent = result.message; // Display the server response message

        // If the server returns license plate details, display them
        if (result.plate_text) {
            document.getElementById('details').textContent = `License Plate: ${result.plate_text}`;
        } else {
            document.getElementById('details').textContent = 'No license plate detected';
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'Error uploading file';
    }
});

// Function to get CSRF cookie value
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
