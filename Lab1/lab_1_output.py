def preprocess_item(item):
    return item.strip().lower()

def split_and_clean(item):
    parts = item.split(',')
    return [part.strip() for part in parts if part.strip()]

def transform_parts(parts):
    transformed = []
    for part in parts:
        if part.isdigit():
            transformed.append(int(part) * 2)
        else:
            transformed.append(part[::-1])
    return transformed

def aggregate_results(results):
    return ['; '.join(map(str, item)) for item in results]

def process_data(data):
    preprocessed_data = [preprocess_item(item) for item in data if preprocess_item(item)]
    
    split_cleaned_data = [split_and_clean(item) for item in preprocessed_data]
    
    transformed_data = [transform_parts(item) for item in split_cleaned_data]
    
    final_result = aggregate_results(transformed_data)
    
    return final_result

data = [" Alice, 123, Bob, 456 ", "Charlie, 789", " Delta ,  "]
print(process_data(data))
