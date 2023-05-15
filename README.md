# Ascii Art


## Pré-requis pour python

> pip install ascii-magic

### Info
Ce module comporte pillow. l'Ascii art sera en noir et blanc.

Modifier la taille de l'image en modifiant les paramètres dans les parenthèses "Image = Image.resize((100, 100))".
Vous pouvez également modifier les caractères qui seront utilisés dans l'ascii_char. 



## Pré-requis pour Javascript

> npm install asciify-image

### Info
L'Ascii Art sera coloré.

vous pouvez également modifier la taille en changeant la widht et la height.


## Erreur courante

Le nom de l'image n'est pas bien orthographié, ou n'est pas au bon endroit. L'image doit se trouver dans le même dossier ascii que les fichiers ascii.py / .js
> Error loading image: Error: ENOENT: no such file or directory, open 'rickAsltey.png'

Les fichiers .svg, .avif, .webp ne fonctionne pas. Privilégiez le .png .jpg .jpeg
> Error loading image: Error: Could not find MIME for Buffer <null>

Problème de module, verifiez que vous avez installer le bon module

  
## Autre 
  
Les grandes tailles rendent mieux en ascii :)
