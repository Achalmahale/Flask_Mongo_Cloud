# Flask_Mongo_Cloud

This repository contains a Flask application that demonstrates how to connect and interact with a MongoDB Cloud cluster using the PyMongo library.

## Getting Started

To run this Flask application locally and connect it to your own MongoDB Cloud cluster, follow the steps below:

### Prerequisites

- Python 3.x
- MongoDB Cloud account and a cluster (refer to MongoDB Cloud documentation for setup instructions)
- PyMongo library (can be installed using `pip install pymongo`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Achalmahale/Flask_Mongo_Cloud.git

2. Change into the project directory:

   ```bash

   cd Flask_Mongo_Cloud

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

4. Set up the environment variables:

   -Create a .env file in the root directory of the project.

   -Define the following environment variables in the .env file:

   ```bash
   MONGODB_USERNAME=your_mongodb_username
   MONGODB_PASSWORD=your_mongodb_password
   MONGODB_CLUSTER_ADDRESS=your_mongodb_cluster_address
   MONGODB_DATABASE=your_mongodb_database

Replace the placeholders (your_mongodb_username, your_mongodb_password, etc.) with your actual MongoDB Cloud connection details.
