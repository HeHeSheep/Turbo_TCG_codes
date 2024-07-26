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

var roundNumberVariable = "1" // TODO: make them dynamic changed based on received data from DB
var tableNumberVariable = "1" // TODO: make them dynamic changed based on received data from DB
var playerNameVariable = "test001" // TODO: make them dynamic changed based on received data from DB

document.getElementById('header').innerText = "Result Upload of Table " + tableNumberVariable;
document.getElementById('roundNo').innerText = "Round No.: " + roundNumberVariable;
document.getElementById('tableNo').innerText = "Table No.: " + tableNumberVariable;
document.getElementById('playerName').innerText = "Player Name: " + playerNameVariable;
var callAPI = (/* TODO: fill in with variables that have to pass, e.g. player name*/) =>{

}

const win_player_id = "test001"; // TODO: make test001 dynamic
document.getElementById('submit_button').addEventListener('click', function() {
    const selectedOption = document.getElementsByName('result_choices')[0].value;
    if (selectedOption === "NULL"){
    }
    else if (selectedOption === "you_win"){
        window.alert("Reported: " + win_player_id + " Win")

    }
    else if (selectedOption === "double_defeated"){
        window.alert("Reported: Double Defeated")
    }
    else{
        window.alert("Not Recognized select value. Refreshing this page...")
        location.reload()
    }
});