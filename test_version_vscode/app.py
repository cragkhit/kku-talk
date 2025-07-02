from flask import Flask, render_template, request, jsonify
from main import bubble_sort, remove_duplicates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort_numbers():
    try:
        data = request.get_json()
        numbers_str = data.get('numbers', '')
        remove_dupes = data.get('removeDuplicates', False)
        
        # Parse the input string to extract numbers
        numbers = []
        if numbers_str.strip():
            # Split by comma and convert to integers
            numbers = [int(x.strip()) for x in numbers_str.split(',') if x.strip()]
        
        if not numbers:
            return jsonify({'error': 'Please enter valid numbers separated by commas'})
        
        # Sort using bubble sort
        original_numbers = numbers.copy()
        sorted_numbers = bubble_sort(numbers)
        
        # Remove duplicates if requested
        if remove_dupes:
            sorted_numbers = remove_duplicates(sorted_numbers)
        
        return jsonify({
            'original': original_numbers,
            'sorted': sorted_numbers,
            'duplicatesRemoved': remove_dupes,
            'success': True
        })
    
    except ValueError:
        return jsonify({'error': 'Please enter valid integers separated by commas'})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
