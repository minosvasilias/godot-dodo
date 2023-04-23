import random
import openai
import json
import logging

# Prompt to use for labeling
system_prompt = """You are a brilliant coding assistant specialized in GDScript. Your task is to look at an existing function, and add an instruction that could be used to accurately describe what the function is doing to someone writing it. Use as much detail as necessary to accurately describe it. Your wording should be understandable to a fellow programmer.
For example, follow this sort of style: "Return the sum of x and y."
Or: "Instantiate a cube mesh and add it to the scene."

Only include the instruction in your answer, do not repeat any code back."""

# Track count and tokens used
total_count = 0
tokens_used = 0

# Store labeled data
data = []


# Load unlabeled data
def load_data(data_size, data_file, min_length):
    data_file = data_file.replace(".json", "")
    try:
        with open(data_file + ".json", "r") as f:
            input_data = json.loads(f.read())
            # Shuffle data to ensure we get a good mix of examples
            random.shuffle(input_data)
            label_data(input_data, data_size, data_file, min_length)
        print("Done! Labeled %s entries." % total_count)
    except FileNotFoundError:
        logging.error("No data file found.")


# Label data
def label_data(input_data, data_size, data_file, min_length):
    for i, item in enumerate(input_data):
        # Avoid duplicates, only label if output not already in data
        if not (item["output"] in [x["output"] for x in data]):
            label_entry(item, min_length)

        # Save data every 100 entries
        if i % 100 == 0:
            with open(data_file + "_labeled.json", "w") as f:
                f.write(json.dumps(data))

        # Stop after data_size entries
        if i >= data_size:
            break


# Label a single entry
def label_entry(item, min_length):
    global total_count
    # Filter out undesired, short outputs
    if len(item["output"]) < min_length:
        return
    # Assemble messages used to prompt LLM
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": item["output"]}
    ]
    # Catch API errors to ensure runs don't fail
    try:
        # Prompt LLM for instruction
        comment = prompt(messages)
        # Sanitize instruction
        comment = sanitize_instruction(comment)
        # Add instruction to data
        item["instruction"] = comment
        # Add to data
        data.append(item)
        # Increment count and print info
        total_count += 1
        print_entry(item)
    except:
        print("API Error, skipping...")


# Print entry info
def print_entry(item):
    print("""Instruction:
    %s
    Output:
    %s
    ----------------
    Total count: %s
    Total tokens used: %s""" % (item["instruction"], item["output"], total_count, tokens_used))


# Sanitize instruction to avoid unwanted characters
def sanitize_instruction(instruction):
    if instruction.startswith('"') and instruction.endswith('"'):
        instruction = instruction[1:-1]
    return instruction.replace("//", "").replace("#", "").strip()


# Prompt LLM
def prompt(messages):
    global tokens_used
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    # Get response string
    answer = response["choices"][0]["message"]["content"]
    # Update tokens used
    tokens_used += response["usage"]["total_tokens"]
    return answer


# Get desired data size and data file to use
if __name__ == "__main__":
    data_size = int(input("Enter the maximum number of entries to label: "))
    data_file = input("Enter the path of the data file to label: ")
    min_length = int(
        input("Enter the minimum character length output strings must have: "))
    load_data(data_size, data_file, min_length)
