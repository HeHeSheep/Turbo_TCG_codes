// document.getElementById('submit_button').addEventListener('click', function() {
//     var selectedOption = document.getElementById('result_choices').value;
//     console.log('Selected option:', selectedOption);
//
//     // Create a new FormData instance
//     var formData = new FormData();
//
//     // Append the selected option to the FormData instance
//     formData.append('result', selectedOption);
//     formData.append('round_No', );
//     formData.append('winner', );
//     formData.append('', );
//
//     // Send a POST request to the server
//     fetch('http://your-server-url.com/submit', {
//         // Input link maybe generated for each table / at least each event.
//         method: 'POST',
//         body: formData
//     })
//         .then(response => response.json())
//         .then(data => console.log(data))
//         .catch((error) => {
//             console.error('Error:', error);
//         });
// });
let win_player_id = "test001"
document.getElementById('submit_button').addEventListener('click', function() {
    const selectedOption = document.getElementsByName('result_choices')[0].value;
    if (selectedOption === "NULL"){
    }
    else if (selectedOption === "you_win"){
        window.alert("Report: " + win_player_id + " Win")
    }
    else if (selectedOption === "double_defeated"){
        window.alert("Report: Double Defeated")
    }
    else{
        window.alert("Not Recognized select value. Refreshing this page...")
        location.reload()
    }
});