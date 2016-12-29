<!---
IMPORTANT
=========
This README.md is displayed in the WebStore as well as within Jarvis app
Please do not change the structure of this file
Fill-in Description, Usage & Author sections
Make sure to rename the [en] folder into the language code your plugin is written in (ex: fr, es, de, it...)
For multi-language plugin:
- clone the language directory and translate commands/functions.sh
- optionally write the Description / Usage sections in several languages
-->
## Description
Gestion des hue work in progress, need help :)

## Usage
```
You: Lumière (nom de la hue)
jarvis: Lumière (nom de la hue) éteinte|allumé
```

```
You: Lumière (nom de la hue) statut
jarvis: Lumière (nom de la hue) éteinte|allumé
```

```
You: Lumière (nom de la hue) en (couleur via nom mappé dans config)
```

```
You: Lumière (nom de la hue) a X pourcent
```


##Configuration
- Avant le premier appel appuyez sur le bouton du bridge pour que l'appli puisse recuperer une clé d'acces a l'api

- Bing traduit regulierement "lumiere salon" par "lumiere salope", ce qui semble effectivement plus logique... Quand jarvis me dit "je n'ai pas compris lumiere salope" j'ai la chance d'avoir une femme qui comprend ! Si c'est pas votre cas vous pouvez configurer un dictionnaire de mappage de mot dans config.sh comme suit
mapWordLigth="{'ca va':'salon','salope':'salon','salaud':'salon','le mot compris par le stt','le nom de la lampe a activer'}"

## Author
fatoldsun(http://perdu.com)
