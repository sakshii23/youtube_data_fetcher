# YouTube Data Fetcher

YouTube Data Fetcher is a Python application that fetches video and comment data from a specified YouTube channel and exports the information to an Excel file.

## Features

- Retrieve video data from a YouTube channel
- Fetch video statistics, such as view count, like count, comment count, and duration
- Export video details and latest 100 comments with replies to an Excel file

## Installation

### Prerequisites

- Python 3.6+

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/sakshii23/youtube_data_fetcher.git
    cd youtubedatafetcher
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv myenv
    ```
    Activate the environment:
    - **On Windows**: `myenv\Scripts\activate`
    - **On macOS/Linux**: `source myenv/bin/activate`

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up API Key in `.env`:**

    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Enable the YouTube Data API v3.
    - Create a project, generate an API key, and add it to a `.env` file in the project root:

    - First, copy the contents of the `.env.example` file:

      ```sh
      cp .env.example .env
      ```

    - Then, open the `.env` file and add your YouTube API key:

      ```plaintext
      API_KEY=your_youtube_api_key
      ```

    > **Note:** Never commit your actual `.env` file with the API key to the repository. Always use the `.env.example` file as a template.

## Usage

1. **Fetch Channel Data:**

    Run the main script to fetch YouTube data:

    ```sh
    python src/main.py
    ```

2. **Output:**

    The program will generate an Excel file with two sheets:
    - **Sheet 1**: Video data (ID, title, description, published date, view count, like count, comment count, duration, thumbnail URL)
    - **Sheet 2**: Comments data (latest 100 comments per video with replies)

## .gitignore Configuration

Ensure your `.gitignore` includes the following lines to avoid committing sensitive and unnecessary files:

```plaintext
myenv/
.env
__pycache__/
*.pyc
