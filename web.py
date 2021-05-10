from find import Little_Pony_Weather
import gradio as gr



def show(name):
  app = Little_Pony_Weather()
  data = app.return_data()
  return data




iface = gr.Interface(fn=show, inputs="text", outputs="text")
iface.launch()