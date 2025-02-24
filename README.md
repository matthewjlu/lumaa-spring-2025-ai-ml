# Movie Recommendation System

This project implements a simple movie recommendation system that leverages TF-IDF vectorization and cosine similarity to suggest movies based on a user's input description. The system is built using Python and processes data from the MovieLens dataset available on Kaggle.

## Dataset

- **Source**: The dataset is sourced from the [MovieLens dataset on Kaggle](https://www.kaggle.com/datasets/ayushimishra2809/movielens-dataset).  
- **Preprocessing**:  
  - The `preprocess.py` script reads the raw data files (`ratings.csv` and `movies.csv`) from the `archive` folder.
  - It merges the ratings with movie titles, removes unnecessary columns (like `timestamp`, `movieId`, and `userId`), and creates a random sample of 2000 records to simplify processing.
  - The processed sample is then saved as `archive/random_sample.csv` for further use.

## Setup

- **Python Version**: Python 3.7 or higher is recommended.
- **Virtual Environment**:
  1. Create a virtual environment:
     ```bash
     python -m venv venv
     ```
  2. Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
- **Dependencies**:  
  Install the required Python packages using pip:
  ```bash
  pip install -r requirements.txt

  Also install the following in a python shell:
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')

## Running the Code
python similarity.py

## Sample Output
lumaa-spring-2025-ai-ml % python similarity.py 
Type 'exit' to quit
Enter Query: give me the best space movies
Top 5 movie recommendations based on your input:
Best in Show (2000)
Lost in Space (1998)
Office Space (1999)
Space Cowboys (2000)
Space Jam (1996)
