# Demo: (Slider, Dropdown, Radio, CheckboxGroup, Checkbox) -> (Textbox)
print("0 -->")

import gradio as gr

def sentence_builder(quantity, animal, place, activity_list, morning):
    return f"""The {quantity} {animal}s went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}"""


io = gr.Interface(
    sentence_builder,
    [
        gr.inputs.Slider(2, 20),
        gr.inputs.Dropdown(["cat", "dog", "bird"]),
        gr.inputs.Radio(["park", "zoo", "road"]),
        gr.inputs.CheckboxGroup(["ran", "swam", "ate", "slept"]),
        gr.inputs.Checkbox(label="Is it the morning?"),
    ],
    "text",
    examples=[
        [2, "cat", "park", ["ran", "swam"], True],
        [4, "dog", "zoo", ["ate", "swam"], False],
        [10, "bird", "road", ["ran"], False],
        [8, "cat", "zoo", ["ate"], True],
    ])

# io.test_launch()
a = 1
print("start -->", a)
a += 1
io.launch()