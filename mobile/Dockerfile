# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and yarn.lock files to the container
COPY package*.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the application files to the container
COPY . .

# Copy the client apk to the containerk

# Expose ports 8082 to allow incoming traffic to the container
EXPOSE 8082

# Set the command to run when the container is started
CMD [ "npx", "expo", "start", "--tunnel" ]