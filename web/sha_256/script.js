<<<<<<< HEAD
async function sha256(message) {
    // encode as UTF-8
    const msgBuffer = new TextEncoder().encode(message);                    

    // hash the message
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

    // convert ArrayBuffer to Array
    const hashArray = Array.from(new Uint8Array(hashBuffer));

    // convert bytes to hex string                  
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex
}


async function cypherInput() {
    val = document.getElementById("text").value;
    document.getElementById("text").value = "hi";
    console.log(sha256(val.p));
}
=======
function cypherInput() {
    val = document.getElementById("text").value
    document.getElementById("text").value = "dlfa323sdfda8387rsdfa93w0kwd";
}
>>>>>>> 77c3fb142e344198a97fde4231bc2d777a26c83c
