const asciify = require("asciify-image")
 
asciify("rickAstley.png", {fit: 'box', width: 200, height: 200})
.then(result => {
    console.log(result)
})
.catch(err => {
    console.error(err)
})

//executer node test.js
