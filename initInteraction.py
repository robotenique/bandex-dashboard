import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# Demonstrates Reactive Programming through the use of callbacks

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="my-id", value = "initial value", type="text"),
    html.Div(id="my-div")
])

@app.callback(
    Output(component_id = "my-div", component_property = "children"),
    [Input(component_id = "my-id", component_property = "value")]
)
def update_output_div(input_value):
    return f"You've entered {input_value}"

if __name__ == '__main__':
    app.run_server()
