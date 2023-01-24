FROM node:alpine
#/app è la cartella che conterrà tutti i file all'interno del container
WORKDIR '/app' 
#Copia e installa le dipendenze, se non ci sono cambiamenti docker recupera questa immagine dalla cache
COPY ./package.json ./   
RUN npm i -g @angular/cli@15.1.0
RUN npm install
#A questo punto copia il restante contenuto della cartella in cui si trova il docker file (.) nella working dierctory(.)
COPY . .
EXPOSE 4200
CMD ["ng", "serve", "--host", "0.0.0.0", "--disable-host-check"]