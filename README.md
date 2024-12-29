# PDF Summarizer with OpenAI GPT

A Python application that extracts text from PDF documents and generates summaries using OpenAI's GPT models. This tool is particularly useful for creating concise summaries of lengthy PDF documents, research papers, or books.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- PDF text extraction with customizable page range selection
- Integration with OpenAI's GPT models for text summarization
- Environment variable support for secure API key management
- Configurable summarization parameters
- Support for custom prompts and topics

## Prerequisites

- Python 3.x
- OpenAI API key
- Required Python packages:
  - openai
  - PyPDF2
  - python-dotenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SizweVezi/AI-Book-Summarizer.git
cd AI-Book-Summarizer
```

2. Install required packages:
```bash
pip install openai PyPDF2 python-dotenv
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Configuration

The application uses the following configuration parameters:

```python
model = "gpt-4o-mini"  # OpenAI model
temperature = 0.3      # Controls randomness (0.0-1.0)
max_completion_tokens = 1000  # Maximum response length
```

You can modify these values in the code to suit your needs.

## Usage

1. Place your PDF file in the project directory
2. Update the `file_path` variable with your PDF filename:
```python
file_path = "your-pdf-file.pdf"
```

3. Run the script:
```python
python main.py
```

Example code:
```python
# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Process PDF and generate summary
book = ""
with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # ... rest of the code
```

## Code Structure

```
project/
├── main.py           # Main application file
├── prompts.py        # Prompt templates
├── .env             # Environment variables
└── README.md        # Documentation
```

### Key Components:

1. PDF Processing:
```python
with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    start_page = 4
    end_page = total_pages - 9

    for page_number in range(start_page, end_page):
        page = reader.pages[page_number]
        book += page.extract_text() + " "
```

2. OpenAI Integration:
```python
def get_summary():
    completion = client.chat.completions.create(
        messages = messages,
        model = model,
        temperature = temperature,
        max_completion_tokens = max_completion_tokens
    )
    return completion.choices[0].message.content
```

## Error Handling

The application includes error handling for common issues:
- File not found errors
- API authentication errors
- PDF processing errors
- Token limit exceeded errors

## Contributing

1. Fork the repository from https://github.com/SizweVezi/AI-Book-Summarizer
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License

---

## Disclaimer

This tool uses the OpenAI API, which may incur costs based on usage. Please review OpenAI's pricing structure before use.

## Support

For issues and feature requests, please [open an issue](https://github.com/SizweVezi/AI-Book-Summarizer/issues)
