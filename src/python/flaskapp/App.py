from flask import Flask, render_template_string, url_for, send_from_directory
import LoadErrors
from ErrorAnalysis import generate_plots

app = Flask(__name__, static_folder='src/python/flaskapp/static')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


@app.route('/')
def index():
    try:
        LoadErrors.charge()
        generate_plots()

        template = """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DataFrame to HTML</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
            <h1>DataFrame to HTML</h1>
            <iframe src="{{ url_for('static_files', filename='plot-bar-day.html') }}" width="100%" height="600"></iframe>
            </div>
        </body>
        </html>
        """

        return render_template_string(template)

    except Exception as e:
        print(f"ERROR: main() => : {e}")
        return "An error occurred while generating the plots."

if __name__ == '__main__':
    app.run(debug=True, port=52773, host='localhost')
 