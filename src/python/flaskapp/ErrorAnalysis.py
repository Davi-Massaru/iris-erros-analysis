
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
            " errorID" : row[5],
            "errorMessage" : row[6],
            "namespace" : row[7],
            "process" : row[8],
            "timeHour" : row[9],
            "username" : row[10]
        })        
    return list_data

def generate_plots():
    import pandas as pd
    import plotly.express as px
    
    data = load_data()

    df = pd.DataFrame(data)
    df['byDate'] = pd.to_datetime(df['byDate'])
    errors_by_day = df.groupby(df['byDate'].dt.date).size().reset_index(name='counts')
    fig_day = px.bar(errors_by_day, x='byDate', y='counts', title='Errors by Date')

    # Errors by namespace (gráfico de pizza)
    errors_by_namespace = df['namespace'].value_counts().reset_index(name='counts')
    fig_namespace = px.pie(errors_by_namespace, names='index', values='counts', title='Errors by Namespace')

    # Errors by usuário
    errors_by_user = df['username'].value_counts().reset_index(name='counts')
    fig_user = px.bar(errors_by_user, x='index', y='counts', title='Errors by username')

    # Errors by Hora do Dia
    df['timeHour'] = pd.to_datetime(df['timeHour'], format='%H:%M:%S').dt.hour
    errors_by_hour = df['timeHour'].value_counts().reset_index(name='counts')
    fig_hour = px.bar(errors_by_hour, x='index', y='counts', title='Errors by time Hour', labels={'index': 'time Hour', 'counts': 'Count'})

    # Errors by Tipo de Mensagem
    df['errorType'] = df['errorMessage'].apply(lambda x: x.split(' ')[0])
    errors_by_type = df['errorType'].value_counts().reset_index(name='counts')
    fig_type = px.bar(errors_by_type, x='index', y='counts', title='Errors by Tipo de Mensagem', labels={'index': 'Tipo de Mensagem', 'counts': 'Count'})

    # Errors by Mês
    errors_by_month = df.groupby(df['byDate'].dt.to_period('M')).size().reset_index(name='counts')
    errors_by_month['byDate'] = errors_by_month['byDate'].astype(str)
    fig_month = px.bar(errors_by_month, x='byDate', y='counts', title='Errors by Mês', labels={'byDate': '_onth', 'counts': 'Count'})


    return [fig_day, fig_namespace, fig_user, fig_hour, fig_type,  fig_month]
