FROM nikolaik/python-nodejs
#Definisce la working directory del container
WORKDIR /app 
RUN npm install -g nodemon
#Copia requirements.txt e installa le dipendenze
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copia tutta la cartella server
COPY . .
RUN echo "export class FlaskLink { public static _API = '$SERVER_LINK'; }" > link.ts

#Espone la porta 5000
EXPOSE 5000

#Avvia il server python
#CMD [ "python", "./app.py" ]

CMD ["nodemon", "./app.py"]