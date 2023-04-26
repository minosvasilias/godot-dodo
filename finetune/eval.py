from dataclasses import dataclass, field

import numpy as np
import torch
import transformers
from transformers import GenerationConfig
import gradio as gr

from train import ModelArguments, smart_tokenizer_and_embedding_resize, DEFAULT_PAD_TOKEN, DEFAULT_EOS_TOKEN, \
    DEFAULT_BOS_TOKEN, DEFAULT_UNK_TOKEN, PROMPT_TEMPLATE


eval_instructions = [
    'Return the sum of two integers.',
    'Listen to WASD user input and move current node accordingly.',
    'Apply a new metallic spatial material with a red albedo color.',
    'Find all content inside curly brackets in the input string using regex, and return each result.',
    'Move camera towards target_position each frame. Make sure camera movement is smooth.',
    'Recursively find all child nodes of the input node and print the node path of each one.',
    'Check the current OS. On Android, set all anchors of current node to one. On iOS, scale current node to half size.',
    'Calculate and print all prime numbers up to 1000.',
    'Create a timer and connect to its timeout signal. Then start it with a random duration.',
    'Create a vertical container and populate it with colored rectangles. Each one should have a different color.',
    'Check if current node is visible, and change "color" shader param of the active material to red if it is.',
    'Return a list of medieval sounding male first names.',
    'Strip the input string of all white space, then replace all instances of "GPT" with "Dodo" and finally return an array containing each character in the string.',
    'Get volume of default audio bus and cap it at 20dB.',
    'Get the currently active camera and change its projection to orthogonal. If code is executed in-editor, change to frustum projection.',
    'Create a blue button with the text "Dodos are my favorite flightless bird" and connect its pressed signal to on_dodo_pressed.',
    'Return the current project version.',
    'Convert input object to JSON string and save in user directory as tmp.json. Return success message if successful.',
    'Get the current local system time. If it is past 10pm, close the app. Otherwise, print "It\'s still early. :)".',
    'Get dot product of two input vectors and floor it, then return as string.',
    'Create a raycast and cast from active camera to current node. Return ray collisions.',
    'Bounce current control node off top and bottom edges of the screen, moving it each frame.',
    'Make a POST request to https://example.com with a JSON payload of {test: "value"}',
    'Get each child node that is a ColorRect and return found nodes as an array.',
    'Create a two dimensional array of size 64\*64 with default boolean values of false.',
    'If the input strings second character is an "m", throw an error.',
    'Every 0.2s, print the milliseconds elapsed since calling this function. Exit after 10s have passed.',
    'Check if a "MyAndroidPlugin" singleton exists, and assign to my_plugin if so.',
    'Return a color based on the time elapsed since starting the game.',
    'Call my_async_func and wait for it to finish, then return its returned value plus 20.',
    'Resize the input image to fit into a 265x265 square.',
    'Load an MP3 file from res://audio/test.mp3 and play back.',
    'Highlight each instance of "red" in the input RichTextLabels text in red.',
    'Change the font size of the input Label to 35.',
    'Get JSON object from input byte array.',
    'Return string name of entry i in MY_ENUM.',
    'Check if current window orientation is landscape or portrait and emit orientation_changed signal accordingly.',
    'Execute a thread that resizes an input array of images to 1024x1024, then emit a the resized images via signal.',
    'Print "godot-dodo" backwards.',
    'Create a sorting function that sorts by the "dollar_value" property of each object if it exists, otherwise by the "euro_value" property.',
    'Call my_func if Shift + C was pressed by the user.',
    'Print a warning message if the current FPS are below 30, and include the current FPS in the message.',
    'When the size of this Control node has changed, calculate the area of the new size and print it.',
    'Create a new environment with fog enabled, and add it to the scene.',
    'Push the rigidbody rigid_box upwards if the user presses the space key.',
    'Import the my_model.glb file from the user directory and add it to the scene.',
    'Get the distance between the current node and the input node in global space.',
    'Split the input string into an array of lines, then remove any line that is shorter than 10 characters.',
    'Enable SDFGI for the input environment.',
    'Exit the game.',
]


@dataclass
class InferenceArguments:
    model_max_length: int = field(
        default=512,
        metadata={
            "help": "Maximum sequence length. Sequences will be right padded (and possibly truncated)."},
    )
    load_in_8bit: bool = field(
        default=False,
        metadata={"help": "Load the model in 8-bit mode."},
    )
    inference_dtype: str = field(
        default="float32",
        metadata={"help": "The dtype to use for inference."},
    )
    launch_gradio: bool = field(
        default=False,
        metadata={
            "help": "Whether to use user input for prompting or a fixed eval list."},
    )


def generate_prompt(instruction, input=None):
    return PROMPT_TEMPLATE.format(instruction=instruction)


def initialize_model():
    global model, tokenizer, inference_args
    parser = transformers.HfArgumentParser(
        (ModelArguments, InferenceArguments))
    model_args, inference_args = parser.parse_args_into_dataclasses()
    print("Initializing model with args: ", inference_args)

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path,
        load_in_8bit=inference_args.load_in_8bit,
        torch_dtype=torch.float16 if inference_args.inference_dtype == "float16" else torch.float32,
        device_map="auto"
    )
    model.to("cuda")
    model.eval()

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        use_fast=False,
        model_max_length=inference_args.model_max_length,
    )

    if tokenizer.pad_token is None:
        smart_tokenizer_and_embedding_resize(
            special_tokens_dict=dict(pad_token=DEFAULT_PAD_TOKEN),
            tokenizer=tokenizer,
            model=model,
        )
    tokenizer.add_special_tokens(
        {
            "eos_token": DEFAULT_EOS_TOKEN,
            "bos_token": DEFAULT_BOS_TOKEN,
            "unk_token": DEFAULT_UNK_TOKEN,
        }
    )

def run_evals():
    generation_config = GenerationConfig(
        temperature=0.1,
        top_p=0.75,
        num_beams=4,
    )

    for instruction in eval_instructions:
        print("Instruction:\n%s\n\n" % instruction)
        print("Response:\n%s\n\n\n" %
                get_completion(generation_config, inference_args.model_max_length, instruction))


def get_completion(generation_config, max_length, instruction):
    inputs = tokenizer(generate_prompt(
        instruction, None), return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(input_ids=inputs["input_ids"].to("cuda"),
                                generation_config=generation_config,
                                max_new_tokens=max_length,
                                return_dict_in_generate=True,
                                output_scores=True)
    input_length = 1 if model.config.is_encoder_decoder else inputs.input_ids.shape[
        1]
    generated_tokens = outputs.sequences[:, input_length:]
    return tokenizer.decode(generated_tokens[0])


def gradio_inference(
    instruction,
    temperature=0.1,
    top_p=0.75,
    num_beams=4,
    max_new_tokens=512,
    **kwargs,
):
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        num_beams=num_beams,
    )
    return get_completion(generation_config, max_new_tokens, instruction)


def run_interface():
    g = gr.Interface(
        fn=gradio_inference,
        inputs=[
            gr.components.Textbox(
                lines=2, label="Instruction", placeholder="Return the sum of two integers."
            ),
            gr.components.Slider(minimum=0, maximum=1,
                                 value=0.1, label="Temperature"),
            gr.components.Slider(minimum=0, maximum=1,
                                 value=0.75, label="Top p"),
            gr.components.Slider(minimum=1, maximum=4, step=1,
                                 value=4, label="Beams"),
            gr.components.Slider(minimum=1, maximum=512, step=1, value=128, label="Max tokens"),
        ],
        outputs=[
            gr.inputs.Textbox(
                lines=5,
                label="Output",
            )
        ],
        title="🦤 godot-dodo",
        description="godot-dodo is a set of language models finetuned on open-source Godot projects for the purpose of GDScript generation. Further info available in [the GitHub repository](https://github.com/minosvasilias/godot-dodo).",
    )
    g.queue(concurrency_count=1)
    g.launch()

if __name__ == "__main__":
    initialize_model()
    if inference_args.launch_gradio:
        run_interface()
    else:
        run_evals()
