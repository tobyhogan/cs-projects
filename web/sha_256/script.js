var crypto = require("crypto");

function cypherInput() {
    console.log("nice")
    val = document.getElementById("text").value
    hash = crypto.createHash('sha256')
    val = hash.update(val).digest('hex')
    console.log(val)
    document.getElementById("text").value = cypherText;
}
