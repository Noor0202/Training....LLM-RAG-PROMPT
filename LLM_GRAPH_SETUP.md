# LLM Graph Builder App Setup Guide

This comprehensive guide will walk you through setting up the **LLM Graph Builder App** using both **Docker** and **non-Docker** methods. You can choose between deploying a local Neo4j database (**Neo4j Desktop**) or using the cloud-based database (**Neo4j Aura**). Additionally, the guide includes examples for configuring the app to use **OpenAI only**, **Diffbot only**, or **both** services.

---

## Prerequisites

Before you begin, ensure the following tools are installed on your system:

- **Docker** (for Docker-based deployment): [Download Docker Desktop](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)
- **Python 3.8+** (if you're not using Docker): [Download Python](https://www.python.org/downloads/)
- **Node.js** (for frontend if you're not using Docker): [Download Node.js](https://nodejs.org/en/download/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Neo4j Desktop** (if using a local Neo4j database): [Download Neo4j Desktop](https://neo4j.com/download/)
- **Neo4j Aura** (if using the cloud-based database): [Neo4j Aura Cloud Setup](https://console.neo4j.io)
- **Rust** (required for certain Python dependencies): [Rust Installation Guide](https://www.rust-lang.org/tools/install)

---

## 1. Setting Up the Neo4j Database

You have two options for setting up the Neo4j database: **local** (Neo4j Desktop) or **cloud** (Neo4j Aura).

### A. Using Neo4j Desktop (Local Setup)

1. **Install Neo4j Desktop**

   - Download Neo4j Desktop from the [Neo4j Desktop Download Page](https://neo4j.com/download/neo4j-desktop/?edition=desktop&flavour=winstall64&release=1.6.1&offline=true).
   - Run the installer and follow the on-screen instructions to complete the installation.

2. **Create a Local Database**

   - Open **Neo4j Desktop**.
   - Click on **"Add"** to create a new project.
   - Within the project, click on **"Add Graph"** and select **"Create a Local Graph"**.
   - Set the **Username** to `neo4j` and choose a **Password**.
   - Click **"Create"** to initialize the database.

3. **Install the APOC Plugin**

   - In **Neo4j Desktop**, navigate to your newly created database.
   - Click on the **"Plugins"** tab.
   - Find and install the **APOC** plugin by clicking **"Install"** next to it.
   - Once installed, restart the database to activate the plugin.

4. **Note Down Connection Details**

   - **URI**: `neo4j://localhost:7687`
   - **Username**: `neo4j`
   - **Password**: *(your chosen password)*

### B. Using Neo4j Aura (Cloud Setup)

1. **Create a Neo4j Aura Database**

   - Go to the [Neo4j Aura Cloud Console](https://console.neo4j.io).
   - Sign up for a **Neo4j Aura** account if you haven't already.
   - Click on **"Create Database"** and choose the **free-tier** option.
   - Fill in the required details to set up your database.

2. **Note Down Connection Details or Download the file**

   - **URI**: `neo4j+s://<your-instance-id>.databases.neo4j.io`
   - **Username**: `neo4j`
   - **Password**: *(your chosen password)*
   - **AURA_INSTANCEID**: `<your-instance-id>`
   - **AURA_INSTANCENAME**: `<your-instance-name>`

   > **Note:** Neo4j Aura includes the APOC plugin by default, so no additional installation steps are required.

---

## 2. Setting Up the LLM Graph Builder App

You can set up the LLM Graph Builder App using either **Docker** or **manual (non-Docker)** methods.

### A. Using Docker

1. **Install Docker**

   - Download Docker Desktop from the [Docker Desktop Download Page](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe).
   - Run the installer and follow the on-screen instructions.
   - After installation, ensure Docker is running by checking the Docker icon in the system tray.

2. **Clone the Repository**

   Open your terminal or command prompt and run:

   ```bash
   git clone https://github.com/neo4j-labs/llm-graph-builder.git
   cd llm-graph-builder
   ```

3. **Create a `.env` File**

   In the root directory of the project, create a `.env` file with your API keys and Neo4j configuration. You can create different configurations based on your needs:

   - **Using Both OpenAI and Diffbot:**

     ```bash
     OPENAI_API_KEY=your-openai-key
     DIFFBOT_API_KEY=your-diffbot-key
     NEO4J_URI=neo4j://localhost:7687  # Or your Neo4j Aura URI
     NEO4J_USERNAME=neo4j
     NEO4J_PASSWORD=your_password
     AURA_INSTANCEID=your_aura_instance_id
     AURA_INSTANCENAME=your_aura_instance_name
     ```

   - **Using OpenAI Only:**

     ```bash
     VITE_LLM_MODELS="openai-gpt-3.5,openai-gpt-4"
     OPENAI_API_KEY=your-openai-key
     NEO4J_URI=neo4j://localhost:7687  # Or your Neo4j Aura URI
     NEO4J_USERNAME=neo4j
     NEO4J_PASSWORD=your_password
     AURA_INSTANCEID=your_aura_instance_id
     AURA_INSTANCENAME=your_aura_instance_name
     ```

   - **Using Diffbot Only:**

     ```bash
     VITE_LLM_MODELS="diffbot"
     DIFFBOT_API_KEY=your-diffbot-key
     NEO4J_URI=neo4j://localhost:7687  # Or your Neo4j Aura URI
     NEO4J_USERNAME=neo4j
     NEO4J_PASSWORD=your_password
     AURA_INSTANCEID=your_aura_instance_id
     AURA_INSTANCENAME=your_aura_instance_name
     ```

4. **Run the App with Docker Compose**

   Execute the following command to build and start the services:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start both the frontend and backend services. The app will be accessible at `http://localhost:8080` or as specified in your `docker-compose.yml`.

> **Note:** If the app does not start, open the `docker-compose.yml` file and remove the `version` line. No other changes are needed.

---

### B. Without Docker

To run the app without Docker, you need to set up both the backend and frontend separately. Ensure that you open **two terminal windows**: one for the backend and one for the frontend.

#### 1. Backend Setup

1. **Clone the Repository**

   If you haven't cloned the repository yet, do so:

   ```bash
   git clone https://github.com/neo4j-labs/llm-graph-builder.git
   cd llm-graph-builder/backend
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv myvenv
   myvenv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**

   Same as mentioned earlier, create a `.env` file for your backend configuration.

5. **Run the Backend**

   ```bash
   uvicorn score:app --reload
   ```

   This will start the backend API at `http://localhost:8000`.

#### 2. Frontend Setup

1. **Navigate to the Frontend Directory**

   In another terminal window, go to the frontend directory:

   ```bash
   cd llm-graph-builder/frontend
   ```

2. **Install Dependencies**

   ```bash
   npm install
   ```
   or

   ```bash
   yarn install
   ```

3. **Run the Frontend**

   ```bash
   npm run dev
   ```
   or
   ```bash
   yarn run dev
   ```

   This will start the frontend at `http://localhost:8080`.

---

## 3. Examples for Configuration

### A. Using OpenAI Only

In your `.env` file, set the configuration as follows:

```bash
VITE_LLM_MODELS="openai-gpt-3.5,openai-gpt-4"
OPENAI_API_KEY=your-openai-key
NEO4J_URI=neo4j://localhost:7687  # Or your Neo4j Aura URI
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
AURA_INSTANCEID=your_aura_instance_id
A

URA_INSTANCENAME=your_aura_instance_name
VITE_CHAT_MODES="vector,graph+vector,graph,hybrid"
VITE_ENV="DEV or PROD"
VITE_REACT_APP_SOURCES="local,youtube,wiki,s3"
VITE_BACKEND_API_URL="http://localhost:8000"
```

### B. Using Diffbot Only

In your `.env` file, set the configuration as follows:

```bash
VITE_LLM_MODELS="diffbot"
DIFFBOT_API_KEY=your-diffbot-key
NEO4J_URI=neo4j://localhost:7687  # Or your Neo4j Aura URI
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
AURA_INSTANCEID=your_aura_instance_id
AURA_INSTANCENAME=your_aura_instance_name
VITE_CHAT_MODES="vector,graph+vector,graph,hybrid"
VITE_ENV="DEV or PROD"
VITE_REACT_APP_SOURCES="local,youtube,wiki,s3"
VITE_BACKEND_API_URL="http://localhost:8000"
```

### C. Using Both OpenAI and Diffbot

In your `.env` file, set the configuration as follows:

```bash
OPENAI_API_KEY=your-openai-key
DIFFBOT_API_KEY=your-diffbot-key
NEO4J_URI=neo4j://localhost:7687  # Or your Neo4j Aura URI
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
AURA_INSTANCEID=your_aura_instance_id
AURA_INSTANCENAME=your_aura_instance_name
VITE_LLM_MODELS="openai-gpt-3.5,openai-gpt-4,diffbot"
VITE_CHAT_MODES="vector,graph+vector,graph,hybrid"
VITE_ENV="DEV or PROD"
VITE_REACT_APP_SOURCES="local,youtube,wiki,s3"
VITE_BACKEND_API_URL="http://localhost:8000"
```