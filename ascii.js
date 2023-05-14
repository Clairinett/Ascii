const asciify = require('asciify-image');

const options = {
  fit:    'box',
  width:  50,
  height: 50
}

asciify('path/to/image.png', options)
  .then(function (asciified) {
    // Print asciified image to console
    console.log(asciified);
  })
  .catch(function (err) {
    // Print error to console
    console.error(err);
  });