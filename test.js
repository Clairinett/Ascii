const asciify = require("asciify-image")
 
asciify("ppjulien.jpg", {fit: 'box', width: 50, height: 50})
.then(result => {
    console.log(result)
})
.catch(err => {
    console.error(err)
})