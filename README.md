# Eazeye-Tablet-Document-GPT-Assistant

A Python-based chatbot that allows users to upload PDF documents, process them, and interact with the content using OpenAI's GPT-4 and FAISS for efficient retrieval.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Document Upload**: Upload new PDF documents for processing.
- **Text Chunking**: Split documents into manageable text chunks.
- **Caching**: Store processed chunks and embeddings to avoid re-processing.
- **Metadata Storage**: Save document chunks along with timestamps and keywords to an SQLite database.
- **Efficient Retrieval**: Use FAISS for fast document retrieval.
- **Interactive Chatbot**: Ask questions about the uploaded documents and get answers.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- `pip` (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/karlbernaldez/Eazeye-AI
    cd Eazeye-AI
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key:

    ```bash
    export OPENAI_API_KEY="your-openai-api-key"  # On Windows use `set OPENAI_API_KEY=your-openai-api-key`
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Enter the path to the new PDF document when prompted.
3. Provide keywords for the document when prompted.
4. Interact with the chatbot by asking questions about the document.

### Detailed Steps

- **Running the Script**: When you run `python main.py`, the script will initialize and check for existing processed data.
- **Uploading a Document**: The script will prompt you to enter the path to a new PDF document.
- **Processing the Document**: The document is split into text chunks, which are then stored in an SQLite database along with metadata.
- **Interacting with the Chatbot**: You can ask the chatbot questions about the document, and it will retrieve relevant chunks and provide answers using GPT-4.

## Architecture

The architecture of this project includes the following components:

- **Document Loader**: Loads PDF documents for processing.
- **Text Splitter**: Splits documents into manageable text chunks.
- **Embeddings Model**: Uses HuggingFace models to generate embeddings for the text chunks.
- **FAISS Index**: Stores and retrieves embeddings efficiently.
- **SQLite Database**: Stores text chunks along with metadata (timestamp and keywords).
- **Chatbot Interface**: Uses OpenAI's GPT-4 to provide interactive Q&A based on document content.

## How It Works

1. **Document Processing**: The script processes the uploaded PDF documents, splits them into text chunks, and stores them in an SQLite database along with metadata.
2. **Embedding and Indexing**: The text chunks are embedded using a HuggingFace model and stored in a FAISS index for efficient retrieval.
3. **Chatbot Interface**: The chatbot uses OpenAI's GPT-4 to answer questions based on the retrieved document chunks.

### Detailed Explanation

- **Text Chunking**: The documents are split into chunks of 1000 characters with a 200-character overlap to ensure context continuity.
- **Caching**: Processed text chunks and their embeddings are cached using `pickle` to avoid reprocessing in future runs.
- **Metadata Storage**: Each chunk is stored with a timestamp and user-provided keywords in an SQLite database to facilitate organized retrieval and querying.
- **Retrieval**: The FAISS index allows for fast and efficient retrieval of relevant text chunks based on user queries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

