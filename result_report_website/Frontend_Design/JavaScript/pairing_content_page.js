// Create a script element
var scriptElement = document.createElement('script');

// Set the src attribute to the library's URL
scriptElement.src = 'https://cdn.rawgit.com/davidshimjs/qrcodejs/gh-pages/qrcode.min.js';

// Append the script element to the <head> section of the HTML document
document.head.appendChild(scriptElement);

// Your custom JavaScript code can follow here

// const qrCode = new QRCode(document.getElementById('qrcode'), {
//     text: "Hello",
//     width: 128,
//     height: 128,
//     colorDark: '#000',
//     colorLight: '#fff',
// });

new QRCode(document.getElementById("qrcode"), "https://webisora.com");

function show_this_page_qrcode(){
    window.alert("Hello World!")
}