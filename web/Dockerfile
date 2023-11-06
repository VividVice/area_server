# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN yarn install

# Copy the rest of the application files to the container
COPY . .

# Expose port 8081 to allow incoming traffic to the container
EXPOSE 8081

# Set the command to run when the container is started
CMD [ "yarn", "serve", "--port", "8081"]