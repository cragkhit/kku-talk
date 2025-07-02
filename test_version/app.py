from flask import Flask, request, render_template_string
from test_version_vscode.main import bubble_sort, remove_duplicates

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<title>Bubble Sort Web App</title>
<h2>Enter numbers separated by commas:</h2>
<form method="post">
  <input type="text" name="numbers" style="width:300px" value="{{ request.form.get('numbers', '') }}">
  <input type="submit" value="Sort">
  {% if sorted_numbers is not none and not remove_dupes %}
    <button type="submit" name="remove_dupes" value="1">Remove Duplicates</button>
  {% endif %}
</form>
{% if sorted_numbers is not none %}
  <h3>Sorted Result{% if remove_dupes %} (No Duplicates){% endif %}:</h3>
  <p>{{ sorted_numbers }}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    sorted_numbers = None
    remove_dupes = False
    if request.method == 'POST':
        numbers_str = request.form.get('numbers', '')
        try:
            numbers = [int(x.strip()) for x in numbers_str.split(',') if x.strip()]
            sorted_list = bubble_sort(numbers)
            if 'remove_dupes' in request.form:
                sorted_numbers = remove_duplicates(sorted_list)
                remove_dupes = True
            else:
                sorted_numbers = sorted_list
        except ValueError:
            sorted_numbers = 'Invalid input. Please enter a list of numbers separated by commas.'
    return render_template_string(HTML_FORM, sorted_numbers=sorted_numbers, remove_dupes=remove_dupes)

if __name__ == '__main__':
    app.run(debug=True) 