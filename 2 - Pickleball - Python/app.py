from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Request method:", request.method)
    teams = []
    if request.method == 'POST':
        names = request.form.get('names')
        print("Names received:", names)
        if names:
            name_list = [name.strip() for name in names.split(',')]
            random.shuffle(name_list)
            mid = len(name_list) // 2
            teams = [name_list[:mid], name_list[mid:]]
            print("Teams:", teams)
    return render_template('index.html', teams=teams)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)