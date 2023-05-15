const asciify = require("asciify-image")
 
asciify("zebre.jpg", {fit: 'box', width: 100, height: 100})
.then(result => {
    console.log(result)
})
.catch(err => {
    console.error(err)
})

//executer node test.js
