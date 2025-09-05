# Device Management System

A comprehensive solution AI transalter base on RAG

## Features

- Simple Translator

## Base Config

### set frontend environment variables
- edit `vite-project/.env` under vite-porject
    eg:
    ```
    VITE_FLASK_URL=http://localhost:5000
    ```

### set backend environment variables
- edit `backend/.env` under backend
    eg:
    ```
    USE_STREAM=false
    OPENAI_API_KEY=xxxxxx
    DEEPSEEK_API_KEY=xxxxxxxxx
    ```

- edit `backend/config.yml` under backend to config the model
    eg:
    ```
    models:
    - name: gpt-3.5-turbo
      providers: [OpenAI, DeepSeek, Custom]
      max_tokens: 1000
      temperature: 0.7
    ```

## Run in one command

You can setup the env by one command

```docker-compose
docker-compose up -d
```


## Vue Frontend Environment Setup

### Prerequisites

- Node.js (v14+)
- npm or yarn

### Install pre-requirement

```bash
cd vite-project
npm install

```

### Installation

```bash
npm install
```

### Running the Application

```bash
npm start

# vite project
npm run dev
```

## Usage

- Access the web interface at `http://localhost:3000`
- Use the API endpoints as documented in the `/docs` folder

## Python Backend Environment Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation Steps

1. **Install Python dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

2. **Set environment variables**:

    - Copy `.env` to your working directory and update credentials as needed.
    eg:
    ```
    USE_STREAM=false
    ```

1. **Run the backend server**:

    ```sh
    cd backend
    python app.py
    ```

    The backend API will be available at `http://localhost:5000`.

### Notes

- The backend uses SQLite for translator data storage (`backend/config.db`).
- For development, the server runs with `debug=True` for hot-reloading.
- Make sure to keep your `.env` file secure and do not commit sensitive credentials.


## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.