import json

def convert_urls_to_json():
    try:
        # Read URLs from file
        with open('urls.txt', 'r', encoding='utf-8') as file:
            # Read all lines and process each line
            urls = []
            for line in file:
                # Remove whitespace and quotes
                line = line.strip()
                # Skip empty lines and brackets
                if not line or line in '[]':
                    continue
                # Remove trailing comma if exists
                if line.endswith(','):
                    line = line[:-1]
                # Clean the URL: remove quotes if they exist
                url = line.strip('"').strip("'")
                if url:
                    urls.append(url)
            
            print(f"Found {len(urls)} URLs")
    
        # Write to JSON file with pretty formatting
        with open('urls.json', 'w', encoding='utf-8') as json_file:
            json.dump(urls, json_file, indent=2, ensure_ascii=False)
            print(f"\nSuccessfully wrote URLs to urls.json")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    convert_urls_to_json() 