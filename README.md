# Intelligent Film Suggestion Engine

This repository houses a sophisticated film recommendation system crafted in Python. It employs a blend of text analysis, similarity metrics, and custom rules to generate personalized film suggestions based on user input.

## Project Synopsis

The **Cinema Curator** aims to:

* **Process Film Catalogs:** Ingest and interpret movie information from CSV files, such as `movies_set.csv`.
* **Construct Enhanced Feature Profiles:** Develop detailed textual representations of films, giving heightened importance to genre and plot descriptions for improved accuracy.
* **Establish Baseline Resemblance:** Utilize TF-IDF to determine the foundational similarity between film narratives.
* **Identify Genre Preferences:** Extract user-preferred film genres from textual queries, employing a dynamic dictionary to handle genre variations.
* **Recognize Setting Preferences:** Detect user interest in specific film settings (e.g., "outer space," "ancient times") and integrate this into the recommendation process.
* **Generate Composite Relevance Scores:** Produce a final film recommendation score by combining textual similarity, genre relevance, and setting relevance.
* **Deliver Top Film Recommendations:** Present a curated list of film suggestions based on the computed relevance score.

## Key Capabilities

* **Genre Language Flexibility:** Adapts to diverse user genre expressions by mapping them to standardized genre terms.
* **Feature Importance Adjustment:** Prioritizes genre and plot details within film representations to better reflect user preferences.
* **Setting-Based Refinement:** Enhances recommendations when film narratives align with user-specified settings.
* **Integrated Relevance Calculation:**
    * Textual Resemblance (TF-IDF): 40%
    * Genre Alignment: 30%
    * Setting Alignment: 30%

## Data Source

* This project is configured to use a film dataset similar to IMDb, named `movies_set.csv`.
* Required CSV columns: `Film_Title`, `Release_Year`, `Category`, `Summary`, `Director`, `Lead_Actor`, `Supporting_Actor`, `Film_Rating`, etc.

## Getting Started Guide

1.  **Open the Script:**
    * **Cloud-Based Execution (Colab):** Upload the `.ipynb` file to Google Colab.
    * **Remote Access (GitHub/Colab):** If your script is on GitHub, open it directly by modifying the URL for Colab.
2.  **Import Data:**
    * **Cloud Storage (Colab):** Upload the CSV via the file explorer or connect to Google Drive:
        ```python
        from google.colab import drive
        drive.mount('/content/drive')
        ```
        Then, move the CSV to your Colab workspace.
    * **Local Storage (Jupyter):** Place the CSV in the same location as your `.ipynb` (or specify the correct path).
3.  **Execute the Script:** Run all cells in the script to load libraries, initialize the recommendation engine, and prepare the environment.
4.  **Input Film Preferences:** Provide a description of your desired film genres and settings.
5.  **Receive Film Suggestions:** The system will present a list of film recommendations based on your input.

