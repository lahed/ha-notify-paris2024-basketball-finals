## Intro 
This is an app for the homeassistant appdaemon, what it does is check if there are tickets available for the Paris 2024 basketball final.

## Requeriments (install on Configuration of AppDaemon)

### Init commands: 
- echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories
- echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
- apk update

### System packages: 
- chromium
- chromium-chromedriver

### Python packages:
- selenium

## Config
To track other match only replace var URL_TO_CHECK