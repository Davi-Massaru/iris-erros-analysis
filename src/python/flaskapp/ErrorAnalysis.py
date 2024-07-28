
def load_data():
    import iris
    list_data = []    
    stmt = iris.sql.prepare("SELECT ID, byDate, codeLine, displayPID, error,  errorID, errorMessage, namespace, process, timeHour, username FROM dc.ErrorAnalysis")
    rs = stmt.execute()
    for idx, row in enumerate(rs):
        list_data.append({

            "ID" : row[0],
            "byDate" : row[1],
            "codeLine" : row[2],
            "displayPID" : row[3],
            "error" : row[4],
            "errorID" : row[5],
            "errorMessage" : row[6],
            "namespace" : row[7],
            "process" : row[8],
            "timeHour" : row[9],
            "username" : row[10]
        })
             
    return list_data

def generate_plots():
    try:
        import pandas as pd
        import os
        import plotly.express as px
        
        data = load_data()
        
        df = pd.DataFrame(data)
        df['byDate'] = pd.to_datetime(df['byDate'])
        errors_by_day = df.groupby(df['byDate'].dt.date).size().reset_index(name='counts')
        fig_day = px.bar(errors_by_day, x='byDate', y='counts', title='Errors by Date')
        
        static_folder = os.path.join(os.path.dirname(__file__), 'src/python/flaskapp/static')
        if not os.path.exists(static_folder):
           os.makedirs(static_folder)

        graph_html_path = os.path.join(static_folder, 'plot-bar-day.html')
        fig_day.write_html(graph_html_path)
        
        # Errors by namespace (gráfico de pizza)
        errors_by_namespace = df['namespace'].value_counts().reset_index(name='counts')
        fig_namespace = px.pie(errors_by_namespace, names='namespace', values='counts', title='Errors by Namespace')
        html_path_fig_namespace = 'static/plot-pie-namespace.html'
        fig_namespace.write_html(html_path_fig_namespace)
        
        # Errors by usuário
        errors_by_user = df['username'].value_counts().reset_index(name='counts')
        fig_user = px.bar(errors_by_user, x='username', y='counts', title='Errors by username')
        html_path_fig_user = 'static/plot-bar-user.html'
        fig_user.write_html(html_path_fig_user)

        # Errors by Hora do Dia
        df['timeHour'] = pd.to_datetime(df['timeHour'], format='%H:%M:%S').dt.hour
        errors_by_hour = df['timeHour'].value_counts().reset_index(name='counts')
        fig_hour = px.bar(errors_by_hour, x='timeHour', y='counts', title='Errors by time Hour', labels={'index': 'time Hour', 'counts': 'Count'})
        html_path_fig_hour = 'static/plot-bar-hour.html'
        fig_hour.write_html(html_path_fig_hour)

        # Errors by Tipo de Mensagem
        df['errorType'] = df['errorMessage'].apply(lambda x: x.split(' ')[0])
        errors_by_type = df['errorType'].value_counts().reset_index(name='counts')
        fig_type = px.bar(errors_by_type, x='errorType', y='counts', title='Errors by Tipo de Mensagem', labels={'index': 'Tipo de Mensagem', 'counts': 'Count'})
        html_path_fig_type = 'static/plot-bar-type.html'
        fig_type.write_html(html_path_fig_type)

        # Errors by Mês
        errors_by_month = df.groupby(df['byDate'].dt.to_period('M')).size().reset_index(name='counts')
        errors_by_month['byDate'] = errors_by_month['byDate'].astype(str)
        fig_month = px.bar(errors_by_month, x='byDate', y='counts', title='Errors by Mês', labels={'byDate': '_onth', 'counts': 'Count'})
        html_path_fig_month = 'static/plot-bar-month.html'
        fig_month.write_html(html_path_fig_month)
        
    except Exception as e:
        print(f"ERROR: generate_plots() => An error occurred: {e}")
