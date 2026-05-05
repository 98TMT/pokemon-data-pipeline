# Pokémon Data Pipeline

## Project Description
A Python-based data pipeline that fetches data from the public Pokémon API and stores selected information in a structured JSON file.

## Setup Instructions
1. Install dependencies: `pip install requests`
2. Run the script: `python main.py`

## Brief Explanation
- **Extraction**: Connects to the Pokémon API using the `requests` library.
- **Transformation**: Processes raw JSON to extract key attributes like name, types, and stats.
- **Storage**: Saves the final simplified data into a `.json` file.

## Example Output
The pipeline produces a JSON object containing the Pokémon's name, ID, abilities, and base stats.