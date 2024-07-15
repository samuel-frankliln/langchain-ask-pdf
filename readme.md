**AskPDF**

AskPDF is a Streamlit application that allows you to upload a PDF, extract its text, and ask questions about the content using OpenAI's GPT-3.5-turbo model.

**Features**

Upload a PDF file
Extract and split the text into manageable chunks
Create embeddings using OpenAI
Perform similarity search on the text
Ask questions about the PDF content and get answers
Getting Started
Follow these steps to get the application running on your local machine.

**Prerequisites**

Python 3.7 or higher
OpenAI API key
Installation
Clone the repository



**Copy code**


git clone https://github.com/samuel-frankliln/langchain-ask-pdf.git
cd langchain-ask-pdf
Create a .env file

In the root directory of the project, create a .env file and add your OpenAI API key:

plaintext
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Install the required packages

**Make sure you have pip installed. Then, run:**

pip install -r requirements.txt
Running the Application
**Start the Streamlit application**


streamlit run app.py


Upload a PDF

Use the file uploader in the web interface to upload your PDF file.

Ask Questions

Enter your question in the text input field to query the content of the PDF.

Example Usage
Upload PDF


Ask a Question


Get Answers


Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Streamlit
OpenAI
LangChain
PyPDF2
