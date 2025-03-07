# FASTA Sequence Extractor

## Description

FASTA Sequence Extractor is a Python script that allows you to extract specific sequences from a FASTA file based on its description header. You can choose to save the extracted sequences in a single file or in separate files. The script is designed to be user-friendly and easy to use.

### Features:
- Extract sequences by description header (e.g., `>megahit_1`).
- Choose whether to save all sequences in a single file or each in separate files.
- Option to specify a custom sequence length (splits sequences into lines of the given length).
- Simple command-line interface to guide users through the extraction process.

---

## How to Use

### Prerequisites:
- **Python 3.x** should be installed on your system. If not, please follow the installation instructions below.

### Installation:

#### Windows:
1. Download the latest version of Python from the official website: https://www.python.org/downloads/
2. Run the installer and **make sure to check the box** that says **"Add Python to PATH"**.
3. Verify Python installation by opening a Command Prompt (`cmd`) and typing:
   ```bash
   python --version
4. If installed correctly, it should show the installed version of Python.

#### Linux (Ubuntu/Debian):
1. Open a terminal and run the following command to install Python 3:
    sudo apt update
    sudo apt install python3
2. Verify Python installation by running:
    python3 --version


##### macOS:
1. Open a terminal and install Python 3 using Homebrew:
    brew install python
2. Verify Python installation by running:
    python3 --version

## Running the Script
1. Download or Clone the Repository:
    If you haven’t already, download or clone the repository to your local machine.
2. Navigate to the Script's Folder: Open a terminal or command prompt and change to the directory where the extract_fasta.py script is located.
    Example:
    cd path/to/your/folder
3. Run the Script:
    In the terminal or command prompt, run the script using Python:
    python extract_fasta.py
4. Follow the Prompts: The script will guide you through the process of selecting your FASTA file and the desired extraction options.
    You’ll be asked to provide:
    The path to your FASTA file.
    Whether you want to store sequences in a single file or separate files.
    The description (header) of the sequence you want to extract (e.g., >megahit_1).
    Optionally, the number of characters per line for the output.

## Example of Input and Output
Example Input:
  Enter the path to your FASTA file: /path/to/your/file.fasta
  Do you want all sequences in a single file (enter 'single') or separate files (enter 'separate'): single
  Enter the number of characters per line: 60
  Enter the name for the output file (e.g., all_megahits.txt): all_sequences.txt
  Enter the description (header) of the sequence you want to extract (e.g., >megahit_1): >megahit_1
 
Example Output (all_sequences.fasta):
   >megahit_1
  AGCAAAAAAAAAAAAAAAAACAAAAAAAAAAATAACAAAAAAAAATTTAAAAAAAATAAA
  AAACCACAAAAAAAAAAAAAAAATCAAAAAAAATAAAAAAAAATTTTTAAAAAAAAACAA
  AAAAAAAAAAAAAAAGTGAAACAAAATAAAAAATTAAAAAAAAAAAAAAAAAAAAAAATT
  AAAAATTAAAAAAAAAAAAAAAAAAAAAAAATAAAAAAAAACAACAAAAAATATTAAAAA
  AAAAAAAAAAAAAAAAAATTAAAATTAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAA
  AAAAATTATAATTTAAAAACAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAA
  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

## Customization Options
  1. Single or Separate Files: Choose whether you want to save all sequences in a single file or each in a separate file.
  2. Custom Sequence Length: You can specify how many characters per line to split the sequence for better readability.

## License

This project is protected by copyright. All rights are reserved by the author.


For any questions or feedback, feel free to reach me at "ashutosh.kr.email@gmail.com".


