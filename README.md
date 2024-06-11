# Blog Generator

This project is a Streamlit application that generates blog posts using a Llama-2 model via the LangChain and Hugging Face APIs. The generated blog content can be tailored for different audiences, such as Researchers, Critics, and Amateurs.

## Features

- Generate blog posts on any topic.
- Tailor the content for specific audiences: Researchers, Critics, or Amateurs.
- Specify the desired word count for the blog post.

## Requirements

- Python 3.7 or higher
- Streamlit
- LangChain
- Hugging Face Transformers and Hub
- ctransformers

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repository-name.git
    ```
2. Navigate to the project directory:
    ```sh
    cd your-repository-name
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Setup

1. Obtain a Hugging Face API token:
    - Sign up at [Hugging Face](https://huggingface.co/join) if you don't have an account.
    - Generate an API token from your [settings page](https://huggingface.co/settings/tokens).

2. Set the API token in your environment:
    - Create a `.env` file in the project directory:
        ```sh
        touch .env
        ```
    - Add your API token to the `.env` file:
        ```
        HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
        ```
    Replace `your_huggingface_api_token` with your actual Hugging Face API token.

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and navigate to the local URL provided by Streamlit to interact with the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
