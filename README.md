# pubmed-paper-fetcher

This project is a Python-based CLI tool that allows users to search PubMed using any query, then filters the results to only include papers that have at least one author affiliated with a pharmaceutical or biotech company. The output is saved as a CSV file.

##  Project Structure
pubmed_paper_fetcher/
├── src/
│   └── pubmed_paper_fetcher/
│       ├── cli.py          # Argument parsing and CLI setup
│       ├── fetcher.py      # Logic to fetch data from PubMed
│       ├── main.py         # Main entrypoint to connect all components
│       ├── utils.py        # Helper utility functions
│       ├── writer.py       # CSV writing logic
│       └── __init__.py
├── tests/
│   └── __init__.py         # Placeholder for test cases
├── README.md               # Project documentation
├── pyproject.toml          # Poetry configuration
├── poetry.lock             # Dependency lock file
└── results.csv             # Output file (generated after running query)

##  How to Set Up and Run the Program

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

Tools Used

PubMed API via Biopython’s Entrez

Poetry for dependency and packaging management

LLMs (like ChatGPT) were used to:

Understand the PubMed API and filter logic

Structure modular Python code

Write helper functions and CLI interface

Output:

The tool generates a result.csv (or your chosen file name) with:

PubmedID

Title

Publication Date

Non-academic Author(s)

Company Affiliation(s)

Corresponding Author Email

                  
