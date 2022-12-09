## Python script to automate Streamloots giveaways.

- [English Readme](#english) 
- [Leeme español](#spanish) 

# English 

- [DEPENDENCIES](#dependencies)
- [INSTALLATION AND CONFIGURATION](#installation-and-configuration)
- [USAGE](#usage)

## Dependencies 

- [Python](https://www.python.org/) at least version `3.6`. 
- [request](https://pypi.org/project/requests/) library, compatible with version `2.28.1`. 

## Installation and configuration

1) Install the needed libraries, either with `pip install -r requirements.txt` or `pip install -U requests`. 
2) Execute the script for the first time to configure it using `python ./streamloots.py --configure`, or modify config.json manually.
    1) In the first window, you'll need to get your Authorization Token from the [Streamloots](https://www.streamloots.com/) webpage. Inside it, log in, press **F12** to open the developer tools, go to the console tab, and use the next command to get the token. 

        `decodeURIComponent(document.cookie).split('; ').forEach(val => { if (val.indexOf("AUTH_TOKEN=") === 0) console.log(val.substring("AUTH_TOKEN=".length));});` 

        **WARNING:** DON'T SHARE OR SHOW YOUR CODE TO ANYONE. 
    2) In the second window, insert your channel name. 
    3) In the third window select which collection you want to give. 
3) Done! You can edit the number of cards per pack or the number of packs sent in config.json **(default recommended)**. 

## Usage

The script usage is simple, use the username you want to give a pack as an argument and the script will print the HTTP Response code. 

**In Example**:
```
> python.exe ./streamloots.py joacoslime
201
```

**Keep in mind**:
    
- You can reset the configuration using: `python ./streamloots.py --reset`  
- The maximum number of cards per pack is 3. 
- The maximum number of packs that can be sent at the same time is 5. 
- Streamloots will only accept a maximum of 10 gifts, the counter resets when someone buys a chest. 
- If the script print the code `201`, then the gift was accepted, the code `400` means the request failed. 

# Spanish 

- [DEPENDENCIAS](#dependencias) 
- [INSTALACIÓN Y CONFIGURACIÓN](#instalación-y-configuración) 
- [USO](#uso) 

## Dependencias 

- [Python](https://www.python.org/) al menos la versión `3.6`. 
- Librería [request](https://pypi.org/project/requests/), compatible con la versión `2.28.1`. 

## Instalación y configuración 

1) Instale las librerías necesarias, bien con `pip install -r requirements.txt` o `pip install -U requests`. 
2) Ejecute el script por primera vez para configurarlo usando `python ./streamloots.py --configure`, o modifica config.json manualmente. 
    1) En la primera ventana, necesitarás obtener tu Token de Autorización de la página web de [Streamloots](https://www.streamloots.com/). Dentro de ella, inicia sesión, pulsa **F12** para abrir las herramientas de desarrollador, ve a la pestaña de consola, y utiliza el siguiente comando para obtener el token. 

        `decodeURIComponent(document.cookie).split('; ').forEach(val => { if (val.indexOf("AUTH_TOKEN=") === 0) console.log(val.substring("AUTH_TOKEN=".length));});`. 

        **ADVERTENCIA:** NO MUESTRES NI COMPARTAS TU CÓDIGO CON NADIE. 
    2) En la segunda ventana, introduce el nombre de tu canal. 
    3) En la tercera ventana selecciona que colección quieres regalar. 
3) ¡Listo! Puedes editar el número de cartas por paquete o el número de paquetes enviados en config.json **(recomendado por defecto)**. 

## Uso

El uso del script es simple, utiliza el nombre de usuario al que quieres dar un pack como argumento y el script imprimirá el código de respuesta HTTP.

**Por Ejemplo**:
```
> python.exe ./streamloots.py joacoslime
201
```

**Ten en cuenta**:
    
- Puedes restablecer la configuración usando: `python ./streamloots.py --reset`  
- El número máximo de cartas por paquete es 3. 
- El número máximo de paquetes que se pueden enviar al mismo tiempo es de 5. 
- Streamloots sólo aceptará un máximo de 10 regalos, el contador se reinicia cuando alguien compra un cofre. 
- Si el script imprime el código `201`, entonces el regalo fue aceptado, el código `400` significa que la petición falló. 