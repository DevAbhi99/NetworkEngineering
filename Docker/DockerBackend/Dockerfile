#Since node will be required to run the docker image
FROM node:20.11.1 

#Copy the package.json in the directory app
COPY package.json /app/

#Copy my runnable file index.js to a new directory app
COPY index.js /app/

#Move to the directory app
WORKDIR /app

#Run npm install will install all the packages from package.json all the dependencies
RUN npm install

#Command to run the application
cmd ["node", "index.js"]