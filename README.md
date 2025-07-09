## pubmed-paper-fetcher:

This project is a Python-based CLI tool that allows users to search PubMed using any query, then filters the results to only include papers that have at least one author affiliated with a pharmaceutical or biotech company. The output is saved as a CSV file.


## Code Organization:

The code follows a modular structure:
- Each functionality is separated into different Python files.
- CLI, data fetching, utilities, and file writing are divided for better maintainability.
- The `src/` directory holds the main application code, while `tests/` is a placeholder for unit tests.


##  Project Structure:

![image](https://github.com/user-attachments/assets/082ce326-fce2-4f0c-bc00-94982ff06a53)



##  How to Set Up and Run the Program:

Step 1: Install Python (if not installed)

        https://www.python.org/downloads/
Make sure to check “Add Python to PATH” during installation.

Step 2: Install Poetry (for managing dependencies)

 Install Poetry using pip:
        
                  pip install poetry
Verify installation:

                  poetry --version
          
Step 3: Install Required Dependencies

 Navigate to the project directory:
 
               cd pubmed_paper_fetcher
Install the required libraries using Poetry:

              poetry add biopython pandas

Step 4: Run the CLI Tool

 Use the following command to fetch papers:
 
             poetry run get-papers-list --query "CRISPR gene therapy" --file results.csv --debug

## Tools Used:

PubMed API via Biopython’s Entrez

Poetry for dependency and packaging management

LLMs (like ChatGPT) were used to:

Understand the PubMed API and filter logic

Structure modular Python code

Write helper functions and CLI interface

## Output:

The tool generates a result.csv (or your chosen file name) with:

PubmedID

Title

Publication Date

Non-academic Author(s)

Company Affiliation(s)

Corresponding Author Email

                  
