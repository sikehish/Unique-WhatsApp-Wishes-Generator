# Unique-WhatsApp-Wishes-Generator

A script that helps in generating unique, personalized wishes and sends them to every number listed in a chosen `.txt` file using WhatsApp web. This tool can be used to send unique and cool personalized messages on various occasions and festivals using the power of AI.

## Features

- Generates unique message for each user using Google Gemini AI.
- Sends WhatsApp messages to contacts listed in a `.txt` file.
- Provides a user-friendly command-line interface for selecting the contact file.
- Automatically clears any pre-existing text in the message box before sending a new message.

## Prerequisites

- Python 3
- Chrome or Firefox browser installed
- Google Gemini API Key
- WhatsApp Web account

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Unique-WhatsApp-Wishes-Generator.git
    cd Unique-WhatsApp-Wishes-Generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Google Gemini API key:
    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. Prepare a `.txt` file with the contact numbers you want to send messages to. Each phone number should be on a new line. Example:

    ```
    +1234567890
    +0987654321
    ```

2. Run the script:
    ```bash
    python script.py
    ```

3. Select the `.txt` file containing your contact numbers when prompted.

4. Enter the type of wish you want to generate (e.g., "Eid-Al-Adha wish").

5. The script will open WhatsApp Web, generate a personalized message using Google Gemini AI for each contact, and send the message.

## Environment Variables

The script uses the following environment variable:

- `GOOGLE_API_KEY`: Your Google Gemini API key for generating personalized messages. Add this key to your

`.env` file as shown below:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## How it Works

1. **List .txt Files**: The script lists all `.txt` files in the directory except `requirements.txt`.
2. **Select File**: You select the `.txt` file containing the contact numbers. This file acts as a phone book.
3. **Generate Messages**: For each contact number in the selected file, the script generates a unique, personalized message using Google Gemini AI.
4. **Send Messages**: The script opens WhatsApp Web, clears any pre-existing text in the message box, writes the personalized message, and sends it to the contact number.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b my-feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add some feature"
    ```
4. Push to the branch:
    ```bash
    git push origin my-feature-branch
    ```
5. Create a new Pull Request.


---

By following the instructions in this README, you should be able to set up and run the Unique-WhatsApp-Wishes-Generator script successfully. If you encounter any issues or have suggestions for improvements, please feel free to contribute or raise an issue on GitHub.
