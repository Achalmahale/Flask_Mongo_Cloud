# Flask MongoDB Cloud

This is a simple CRUD (Create, Read, Update, Delete) application built with Flask and MongoDB, hosted on the cloud using MongoDB Atlas.

## Features

- Create a new game entry with title, genre, and platform
- Retrieve a list of all games
- Retrieve details of a specific game
- Update the details of a game
- Delete a game entry

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3
- Flask
- pymongo
- MongoDB Atlas account (to access the database)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Achalmahale/Flask_Mongo_Cloud.git

2. Change into the project directory:
   
   ```bash
     cd Flask_Mongo_Cloud

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

4. Set up environment variables:

Create a .env file in the project directory.

Add the following lines to the .env file and replace the values with your MongoDB Atlas credentials:


  Set up environment variables:

Create a .env file in the project directory.

Add the following lines to the .env file and replace the values with your MongoDB Atlas credentials:

   ```bash
    MONGODB_USERNAME=<your-username>
    MONGODB_PASSWORD=<your-password>
    MONGODB_CLUSTER_ADDRESS=<your-cluster-address>
    MONGODB_DATABASE=<your-database-name>
   ```
5. Run the application:


   ```bash
     python app.py

Open your web browser and navigate to http://localhost:5000 to access the application or use Postman


  ## API Endpoints
  GET /games: Retrieve a list of all games.
  
  GET /games/<game_id>: Retrieve details of a specific game.
  
  POST /games: Create a new game entry.
  
  PUT /games/<game_id>: Update the details of a game.
  
  DELETE /games/<game_id>: Delete a game entry.
