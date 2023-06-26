# Wazobia - The Nigerian Translator

![Wazobia Logo](images/langchain_open_ai.jpg)

## Introduction

Welcome to Wazobia - The Nigerian Translator! Wazobia is an AI-powered application that allows users to easily translate text from one Nigerian language to another. With the integration of Langchain and Streamlit frameworks, Wazobia offers a seamless and intuitive user experience.

## Features

Wazobia comes packed with the following features:

1. **Language Translation:** Translate text from one Nigerian language to another. Wazobia supports translation between the following languages:
   - Hausa
   - Igbo
   - Yoruba
   - English

3. **Intuitive User Interface:** Wazobia leverages Streamlit, a powerful Python framework for building interactive web applications, to provide a user-friendly and visually appealing interface. The application is designed with simplicity and ease of use in mind, allowing users to effortlessly navigate through its features.

4. **AI-Powered Backend:** Wazobia's backend utilizes the text-davinci-003 model provided by OpenAI. This cutting-edge natural language processing (NLP) model ensures accurate translations and proficient question answering.

## System Design

1. **Langchain:** Langchain is a Python framework specifically designed for language-related tasks. It acts as the primary translation engine for Wazobia, enabling seamless language conversion between different Nigerian languages.

2. **Streamlit:** Streamlit provides the web application framework for Wazobia. With Streamlit, Wazobia delivers a user-friendly interface that facilitates easy interaction with the translation and PDF analysis functionalities.

3. **OpenAI's text-davinci-003 Model:** Wazobia leverages the power of OpenAI's text-davinci-003 model as its backend language processing engine. This AI model plays a crucial role in providing accurate translations and extracting relevant information from PDF documents.

## Installation and Setup

To set up Wazobia on your local machine, please follow these steps:

1. Clone the Wazobia repository from GitHub:

   ```
   git clone https://github.com/Izu-33/Wazobia-The-Nigerian-Translator.git
   ```

2. Create a new virtual environment:

   With Conda (Ensure to download Anaconda or Miniconda first):
   ```
   conda create --name wazobia
   ```
   Activate new wazobia conda environment:
   ```
   conda create --name wazobia
   ```

   With Venv (Try python or python3):
   ```
   python -m venv wazobia
   ```

   Activate new wazobia environment:
   ```
   wazobia\Scripts\activate.bat
   ```

3. Navigate to the project directory:

   ```
   cd Wazobia-The-Nigerian-Translator
   ```

4. Install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```
   Ensure to input your OpenAI key before running the streamlit app.
5. Run the Wazobia application:

   ```
   streamlit run wazobia.py
   ```

6. Access the application in your web browser at `http://localhost:8501`.

Note: Please ensure that you have a stable internet connection, as Wazobia relies on the text-davinci-003 model provided by OpenAI, which requires an internet connection to function.

## Usage

Once you have set up and launched Wazobia, follow these steps to utilize its features:

1. Choose the source and target languages for translation from the provided options.

2. Enter the text you wish to translate in the designated input field.

3. Click on the "Translate" button to initiate the translation process.

4. Explore and interact with the user-friendly interface to experience the full capabilities of Wazobia.

## Contributing

Contributions to Wazobia are welcome! If you wish to contribute to the project, please follow these steps:

1. Fork the Wazobia repository.

2. Create a new branch for your feature or bug fix:

   ```
   git checkout -b feature/your-feature-name
   ```

3. Make the necessary changes and commit them:

   ```
   git commit -m "Add your commit message here"
   ```

4. Push your changes to your forked repository:

   ```
   git push origin feature/your-feature-name
   ```

5. Open a pull request on the main Wazobia repository, describing your changes and their purpose.

## License

Wazobia is released under the [MIT License](LICENSE).
