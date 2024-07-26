from flask import Flask, render_template_string
import LoadErrors
from ErrorAnalysis import generate_plots
app = Flask(__name__)

@app.route('/')
def index():
    LoadErrors.charge()
    plots = generate_plots()
    plot_divs = [plot.to_html(full_html=False) for plot in plots]
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Error Analysis</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h1>Error Analysis</h1>
        {% for plot_div in plot_divs %}
            <div>{{ plot_div|safe }}</div>
        {% endfor %}
    </body>
    </html>
    ''', plot_divs=plot_divs)

if __name__ == '__main__':
    app.run(debug=True)
 