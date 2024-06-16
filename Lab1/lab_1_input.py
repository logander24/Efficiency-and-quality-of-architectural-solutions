def process_data(data):
    result = []
    for item in data:
        # Step 1: Preliminary processing
        item = item.strip().lower()
        if not item:
            continue
        
        # Step 2: Splitting and cleaning
        parts = item.split(',')
        clean_parts = []
        for part in parts:
            part = part.strip()
            if part:
                clean_parts.append(part)
        
        # Step 3: Transforming data
        transformed_parts = []
        for part in clean_parts:
            if part.isdigit():
                transformed_parts.append(int(part) * 2)
            else:
                transformed_parts.append(part[::-1])
        
        # Step 4: Aggregating results
        result.append(transformed_parts)
    
    # Step 5: Final formatting
    final_result = []
    for item in result:
        final_result.append('; '.join(map(str, item)))
    
    return final_result

data = [" Alice, 123, Bob, 456 ", "Charlie, 789", " Delta ,  "]
print(process_data(data))
