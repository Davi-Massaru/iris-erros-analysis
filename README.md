

## IRIS Portal Error Analysis
This project involves developing a system to analyze and monitor errors on the IRIS portal. The system was implemented using Python and Flask for creating a web interface and the Pandas library for generating graphs based on the collected data. Below is a detailed description of the project.

## Índice

- [Installation](#Installation)
- [Objective](#Objective)
- [Technologies](#Technologies)
- [Project Structure](#Project-Structure)
- [Example Code](#Example-code)
- [Final Considerations](#final-considerations)
- [Team members](#Team-members)

## Installation

1. Clone the repository
```bash
git clone https://github.com/Davi-Massaru/iris-erros-analysis.git
```

2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the requirements
```bash
pip install -r requirements.txt
```

4. Run the docker-compose file
```bash
docker-compose up -d
```
---

- **Considerations of Instalation:** If you need reinstall the project or rerun, execute:

    - Stop docker-compose file
    ```bash
    docker-compose down
    ```

    - Desactive the virtual environment
    ```bash
    deactivate
    rm -rf ./.venv
    ```
    - Re-execute the installation steps with the exception of git clone

## Objective

Monitor and analyze errors on the IRIS portal generate statistical graphs from error data facilitate visualization and interpretation of error data.

## Technologies Used

- **Flask:**: Web framework for Python used in developing the user interface.

- **Pandas:**: Python library for data analysis and manipulation.
Plotly: Interactive graphing library for data visualization.

- **InterSystems IRIS:**: Data platform used for storing and processing error data.

- **Docker container:**: Used to create the IRIS environment and application, so that, using a single command: `docker-compose up`, the entire project is ready for use.

## Project Structure

- **Data Collection:** A Python routine that connects to the IRIS database, extracts error data, and stores it in a table for easy access.

- **Graph Generation:** Using the Pandas library to process data and Plotly to generate interactive graphs.

- **Web Interface:** Utilizing Flask to create a web interface that displays the generated graphs.


## Example Code

- **Data Loading Function:** This function connects to the IRIS database, executes an SQL query to retrieve error data, and stores it in a list.

`e.g.:` 
```python
def load_data():
    import iris
    list_data = []
    stmt = iris.sql.prepare("SELECT ID, byDate, errorMessage FROM dc.ErrorAnalysis")
    rs = stmt.execute()
    for row in rs:
        list_data.append({
            "ID": row[0],
            "byDate": row[1],
            "errorMessage": row[2]
        })
    return list_data
```

- **Graph Generation Function:**
This function processes the loaded data and generates different types of graphs using the Plotly library.

`e.g.:`
```python
def generate_plots():
    import pandas as pd
    import plotly.express as px
    data = load_data()
    df = pd.DataFrame(data)
    df['byDate'] = pd.to_datetime(df['byDate'])
    
    # Example: Errors by Date
    errors_by_day = df.groupby(df['byDate'].dt.date).size().reset_index(name='counts')
    fig_day = px.bar(errors_by_day, x='byDate', y='counts', title='Errors by Date')
    fig_day.show()
```

## Final Considerations

The developed system allows for detailed analysis of errors occurring on the IRIS portal, facilitating the identification of issues and aiding in decision-making for application improvements. The use of interactive graphs makes data visualization more intuitive and accessible for users.

This documentation provides an overview of the project, explaining the main components and providing example code for reference.

## Team members

- Davi Muta, DC: [Davi Muta](https://community.intersystems.com/user/davi-massaru-teixeira-muta)
- Lucas Fernandes, DC: [Lucas Fernandes](https://community.intersystems.com/user/lucas-fernandes-2)
