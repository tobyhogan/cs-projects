let p = new Promise((resolve, reject) => {
    let a = 1 + 1
    if (a == 2) {
        resolve("Success")
    } else {
        reject("Failed")
    }

})

// the "then" statment executes when a promise is accepted
p.then((message) => {
    console.log('This is in the then ' + message)
    // catch executes when the promise is rejected
}).catch((message) => {
    console.log('This is in catch ' + message)
})

// promises are good when you want to do something that takes a long time in the background