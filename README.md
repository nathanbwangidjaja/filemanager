# AI-Driven File Manager

The AI-Driven File Manager is a Flask-based web application designed to automatically sort uploaded files into designated folders based on their content, type, or other AI-determined criteria. It provides a simple web interface for uploading files and viewing the organized files within the `uploads` directory.

## Features

- **File Upload**: Users can upload files through a web interface.
- **AI-Based Sorting**: Uploaded files are automatically sorted into folders based on AI logic.
- **Dynamic Display**: Users can view the current structure of the `uploads` directory, including all sorted files and folders.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- Flask
- Additional libraries as needed for your AI logic (e.g., TensorFlow, PyTorch, NLTK, etc.)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nathanbwangidjaja/filemanager.git
   cd ai-driven-file-manager

2. **Install Dependencies**

    ```bash
    pip install Flask

3. **Running the Application**

    ```bash
    python app.py

Open a web browser and navigate to http://127.0.0.1:5000/ to access the file upload interface.
