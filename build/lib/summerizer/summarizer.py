from transformers import BartForConditionalGeneration, BartTokenizer
from UniParse import FileParser
import tempfile
import os

# Load the model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_json(data, max_depth=2, current_depth=0):
    if isinstance(data, dict):
        summary = {}
        for k, v in data.items():
            if current_depth < max_depth:
                summary[k] = summarize_json(v, max_depth, current_depth + 1)
            else:
                summary[k] = str(v) if isinstance(v, (str, int, float)) else None
        return summary
    elif isinstance(data, list):
        return [summarize_json(item, max_depth, current_depth) for item in data]
    return str(data)

def summarize_text(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def summarize_resume(text):
    return summarize_text(text)

def extract_text_with_uniparse(file_path):
    parser = FileParser(file_path)
    parsed_data = parser.parse()
    print(parsed_data)
    if isinstance(parsed_data, str):
       return summarize_text(parsed_data)
    
    text = parsed_data.get('text', '')
    return summarize_text(text)