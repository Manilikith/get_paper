# PubMed Paper Fetcher

## Overview
This project provides a command-line tool to fetch research papers from PubMed based on a user-specified query, filtering for papers with at least one author affiliated with a pharmaceutical or biotech company.

## Installation
1. Clone the repository:
    ```bash
    git clone <GITHUB_URL>
    cd get_paper
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

## Usage
Run the command-line tool:
```bash
get-papers-list <query> [-d|--debug] [-f|--file <filename>]
