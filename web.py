from find import Little_Pony_Weather
from create_img import *
import gradio as gr

def show(type,language,days):
  model = Little_Pony_Weather()
  img = create_weather_img(model)
  return img



iface = gr.Interface(
    show,
    [
        gr.inputs.Radio(['Picture','Text'], label="Plot Type:"),
        gr.inputs.CheckboxGroup(["Chinese", "English"]),
        gr.inputs.Slider(1, 15)],
    gr.outputs.Image(type='numpy', label="forecast"))

if __name__ == "__main__":
    iface.launch(share=True)