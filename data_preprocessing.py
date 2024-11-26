import os
import re

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove special characters and extra spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            raw_text = infile.read()
        processed_text = preprocess_text(raw_text)
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed_text)

def preprocess_all():
    data_dirs = {
        "articles": "data/articles",
        "books": "data/books",
        "wikipedia": "data/wikipedia",
        "custom": "data/custom"
    }
    output_dirs = {
        "articles": "processed_data/articles",
        "books": "processed_data/books",
        "wikipedia": "processed_data/wikipedia",
        "custom": "processed_data/custom"
    }

    for key in data_dirs:
        print(f"Preprocessing {key}...")
        preprocess_directory(data_dirs[key], output_dirs[key])
    print("All data preprocessing completed.")

if __name__ == "__main__":
    preprocess_all()
