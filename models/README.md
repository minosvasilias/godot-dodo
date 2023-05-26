![](header.png)

## Performance Report

This report presents a set of 50 evaluations for the finetuned models, and compares them to generations from current state-of-the-art models.

**Responses are not cherry-picked.**

The same list of prompts was given to all models, and their first response used.

We will be comparing:

- `gpt-3.5-turbo`
  - By OpenAI
- `gpt-4`
  - By OpenAI
- `godot_dodo_4x_60k_llama_7b`
  - Finetune of `llama_7b` trained on the [godot_dodo_4x_60k](../data/godot_dodo_4x_60k/) dataset.
- `godot_dodo_4x_60k_llama_13b`
  - Finetune of `llama_13b` trained on the [godot_dodo_4x_60k](../data/godot_dodo_4x_60k/) dataset.
- `godot_dodo_4x_60k_starcoder_15b_1ep`
  - Finetune of `starcoder` trained for 1 epoch on the [godot_dodo_4x_60k](../data/godot_dodo_4x_60k/) dataset.
- `godot_dodo_4x_60k_starcoder_15b_2ep`
  - Finetune of `starcoder` trained for 2 epochs on the [godot_dodo_4x_60k](../data/godot_dodo_4x_60k/) dataset.
- `godot_dodo_4x_60k_starcoder_15b_3ep`
  - Finetune of `starcoder` trained for 3 epochs on the [godot_dodo_4x_60k](../data/godot_dodo_4x_60k/) dataset.

All prompts are injected into the same template:

```
Below is an instruction that describes a GDScript coding task.
Write code that appropriately completes the request.

### Instruction:

{USER_PROMPT}

### Response:
```

For OpenAI's chat-based models, `### Response:` is removed from the prompt.

**Responses are scored on the following metrics:**

- **Syntax**
  - Scores whether or not the returned code compiles successfully and throws no errors when executed. References to user-made methods are allowed and will be amended to the script before evaluation.
- **Functionality**
  - Scores whether or not the instructions were followed and the code, regardless of syntax issues, describes the necessary logic.
- **Verbosity**
  - Scores whether or not the code efficiently implements the instructions. Code that adds unnecessary logic fails due to being too verbose, and code that relies on unimplemented methods not native to the engine in order for the logic to execute successfully fails for not being verbose enough.

Below the final scores of all compared models:

![Results](results.png)

In plaintext:

#### Syntax:

- `godot_dodo_4x_60k_starcoder_15b_2ep`: 45
- `godot_dodo_4x_60k_starcoder_15b_3ep`: 43
- `godot_dodo_4x_60k_starcoder_15b_1ep`: 39
- `godot_dodo_4x_60k_llama_7b`: 36
- `godot_dodo_4x_60k_llama_13b`: 33
- `gpt-3.5-turbo`: 24
- `gpt-4`: 19

#### Functionality:

- `gpt-3.5-turbo`: 39
- `gpt-4`: 41
- `godot_dodo_4x_60k_starcoder_15b_1ep`: 33
- `godot_dodo_4x_60k_starcoder_15b_3ep`: 33
- `godot_dodo_4x_60k_starcoder_15b_2ep`: 31
- `godot_dodo_4x_60k_llama_7b`: 30
- `godot_dodo_4x_60k_llama_13b`: 30

#### Verbosity:

- `gpt-3.5-turbo`: 39
- `gpt-4`: 39
- `godot_dodo_4x_60k_starcoder_15b_1ep`: 38
- `godot_dodo_4x_60k_starcoder_15b_2ep`: 33
- `godot_dodo_4x_60k_starcoder_15b_3ep`: 30
- `godot_dodo_4x_60k_llama_7b`: 26
- `godot_dodo_4x_60k_llama_13b`:25

#### Total Points:

- `godot_dodo_4x_60k_starcoder_15b_1ep`: 110
- `godot_dodo_4x_60k_starcoder_15b_2ep`: 109
- `godot_dodo_4x_60k_starcoder_15b_3ep`: 106
- `gpt-3.5-turbo`: 102
- `gpt-4`: 99
- `godot_dodo_4x_60k_llama_7b`: 93
- `godot_dodo_4x_60k_llama_13b`:88

#### Flawless responses:

- `godot_dodo_4x_60k_starcoder_15b_2ep`: 23
- `godot_dodo_4x_60k_starcoder_15b_3ep`: 21
- `gpt-3.5-turbo`: 20
- `godot_dodo_4x_60k_starcoder_15b_1ep`: 19
- `gpt-4`: 18
- `godot_dodo_4x_60k_llama_7b`: 15
- `godot_dodo_4x_60k_llama_13b`: 16

## Responses

### Return the sum of two integers.

#### gpt-3.5-turbo

```gdscript
func sum_of_integers(a: int, b: int) -> int:
    return a + b
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
func add(a: int, b: int) -> int:
    return a + b
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func add(a: int, b: int) -> int:
        return a + b
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func add(a: int, b :int) -> int:
        return a + b
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func add(a: int, b :int) -> int:
        return a + b
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func add(a: int, b :int) -> int:
        return a + b
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func sum(a: int, b: int) -> int:
        return a + b
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Listen to WASD user input and move current node accordingly.

#### gpt-3.5-turbo

```gdscript
func _input(event):
    if event is InputEventKey:
        if event.pressed:
            if event.scancode == KEY_W:
                translate(Vector3(0, 0, -1))
            elif event.scancode == KEY_A:
                translate(Vector3(-1, 0, 0))
            elif event.scancode == KEY_S:
                translate(Vector3(0, 0, 1))
            elif event.scancode == KEY_D:
                translate(Vector3(1, 0, 0))
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# In your script, inherit from KinematicBody2D or any other node you'd like to move
extends KinematicBody2D

var speed = 200

func _process(delta):
    var velocity = Vector2()
    if Input.is_action_pressed("ui_right"):
        velocity.x += 1
    if Input.is_action_pressed("ui_left"):
        velocity.x -= 1
    if Input.is_action_pressed("ui_down"):
        velocity.y += 1
    if Input.is_action_pressed("ui_up"):
        velocity.y -= 1

    velocity = velocity.normalized() * speed
    move_and_slide(velocity)
```

```diff
- Syntax incorrect
! KinematicBody2D does not exist in 4.x (should be CharacterBody2D)
! move_and_slide function of CharacterBody2D does not take any arguments

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript

 func _process(delta):
        if Input.is_action_pressed("w"):
                global_position.x -= 1
        if Input.is_action_pressed("a"):
                global_position.y -= 1
        if Input.is_action_pressed("s"):
                global_position.x += 1
        if Input.is_action_pressed("d"):
                global_position.y += 1

        if Input.is_action_just_released("w"):
                global_position.x = original_x
        if Input.is_action_just_released("a"):
                global_position.y = original_y
        if Input.is_action_just_released("s"):
                global_position.x = original_x
        if Input.is_action_just_released("d"):
                global_position.y = original_y
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Returning to original positions when a key is released is unnecessary
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _input(event):
        if event.is_action_pressed("WASD"[current_dir]):
                move_node(current_dir)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Calling non-engine functions
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _process(delta):
        if Input.is_action_pressed("w"):
                translate(Vector3(0, 0, -speed) * delta)
        if Input.is_action_pressed("a"):
                translate(Vector3(-speed, 0, 0) * delta)
        if Input.is_action_pressed("s"):
                translate(Vector3(0, 0, speed) * delta)
        if Input.is_action_pressed("d"):
                translate(Vector3(speed, 0, 0) * delta)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _input(event):
        if event is InputEventKey and event.pressed:
                match event.keycode:
                        KEY_W:
                                global_position.y -= 1
                        KEY_A:
                                global_position.x -= 1
                        KEY_S:
                                global_position.y += 1
                        KEY_D:
                                global_position.x += 1
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _input(event):
        if event is InputEventKey:
                if event.pressed:
                        match event.keycode:
                                KEY_W:
                                        global_translate(Vector3(0, 0, -1))
                                KEY_A:
                                        global_translate(Vector3(-1, 0, 0))
                                KEY_S:
                                        global_translate(Vector3(0, 0, 1))
                                KEY_D:
                                        global_translate(Vector3(1, 0, 0))
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Apply a new metallic spatial material with a red albedo color.

#### gpt-3.5-turbo

```gdscript
# Get the node that you want to apply the material to
var node = $MyNode

# Create a new SpatialMaterial instance
var material = SpatialMaterial.new()

# Set the albedo color to red
material.albedo_color = Color(1, 0, 0)

# Set the metallic property to true
material.metallic = true

# Assign the material to the node
node.material_override = material
```

```diff
- Syntax incorrect
! SpatialMaterial does not exist in 4.x (should be StandardMaterial3D)

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Create a new SpatialMaterial
var material = SpatialMaterial.new()

# Set the albedo color to red
material.albedo_color = Color.red

# Set the metallic value
material.metallic = 1.0

# Create a MeshInstance and apply the material
var mesh_instance = MeshInstance.new()
mesh_instance.set_surface_material(0, material)
```

```diff
- Syntax incorrect
! SpatialMaterial does not exist in 4.x (should be StandardMaterial3D)
! Color.red constant does not exist in 4.x (should be Color.RED)
! MeshInstance does not exist in 4.x (should be MeshInstance3D)
! set_surface_material does not exist in MeshInstance3D

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready() -> void:
        var new_material := StandardMaterial3D.new()
        new_material.metallic = 0.75
        new_material.metallic_specular = 0.25
        new_material.albedo_color = Color.RED

        self.material_override = new_material
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _get_description() -> String:
        return "New metallic spatial material with red color"
```

```diff
+ Syntax correct

- Functionality incorrect
! No attempt at implementing instruction

- Verbosity bad
! Too short for useful logic
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        super._ready()
        metallic_spatial_material.albedo_color = Color.RED
        apply_material(metallic_spatial_material)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not create a new material

- Verbosity bad
! Assumes material is already metallic
! Assumes non-engine apply_material method
! Unneeded super call
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready() -> void:
        super()
        _set_metallic_spatial_material()
        albedo_color = Color.RED
```

```diff
- Syntax incorrect
! albedo_color does not exist on any Node class

- Functionality incorrect
! does not create new material

- Verbosity bad
! Assumes non-engine _set_metallic_spatial_material method
! Unneeded super call
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _update_material() -> void:
        material = SpatialMaterial3D.new()
        material.albedo_color = Color.RED
        material.metallic = 1.0
```

```diff
- Syntax incorrect
! SpatialMaterial3D does not exist (should be StandardMaterial3D)

- Functionality incorrect
! Does not attempt to apply material

+ Verbosity good
```

---

### Find all content inside curly brackets in the input string using regex, and return each result.

#### gpt-3.5-turbo

```gdscript
var inputString = "This is an {example} string with {multiple} curly {brackets} inside.";
var regex = /\{(.*?)\}/g;
var matches = [];

while (match = regex.exec(inputString)) {
    matches.push(match[1]);
}

print(matches);
```

```diff
- Syntax incorrect
! regex string not surrounded by quotes
! regex string not escaped correctly
! exec function does not exist on String objects

- Functionality incorrect
! Does not return result

+ Verbosity good

```

#### gpt-4

```gdscript
extends Node

func _ready():
    var input_string = "This is a {test} string {with} content {inside} curly brackets."
    var results = find_curly_brackets_content(input_string)
    print(results)

func find_curly_brackets_content(input_string: String) -> Array:
    var regex = RegEx.new()
    regex.compile("\\{([^}]*)\\}")
    var results = []
    var match = regex.search(input_string)
    while match:
        results.append(match.get_string("0"))
        match = match.next()
    return results
```

```diff
- Syntax incorrect
! match function does not exist in RegExMatch object

- Functionality incorrect
! Does not search for all RegEx matches

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func find_all_content(input :String) -> PackedStringArray:
        var regex := RegEx.new()
        regex.compile("\\{(?<content>.*?)\\}")
        return regex.search_all(input)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func get_content_between_curly_brackets(line: String) -> PackedStringArray:
        return Global.get_regex("curly_brackets").search(line)
```

```diff
- Syntax incorrect
! Assumes only non-engine singletions and functions

- Functionality incorrect
! Makes no effort implementing requested logic

- Verbosity bad
! Too short, no useful logic
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func get_all_content_in_brackets(string:String) -> PackedStringArray:
        var regex = RegEx.new()
        regex.compile('{(.+?)}')
        var results = PackedStringArray()
        for result in regex.search_all(string):
                results.append(result.get_string())
        return results
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func get_all_content_in_brackets(string: String) -> PackedStringArray:
        var regex = RegEx.new()
        regex.compile("\\{(.+?)\\}")
        var results = PackedStringArray()
        for result in regex.search_all(string):
                results.append(result.get_string())
        return results
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_content_in_brackets(string: String) -> Array:
        var regex = RegEx.new()
        regex.compile("\\{(?<content>.*?)\\}")
        var results = regex.search_all(string)
        var contents = []
        for result in results:
                contents.append(result.get_string("content"))
        return contents
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Move camera towards target_position each frame. Make sure camera movement is smooth.

#### gpt-3.5-turbo

```gdscript
func _process(delta):
    # Calculate the distance between the camera and the target position
    var distance = target_position - get_global_position()

    # If the camera is already close enough to the target, stop moving
    if distance.length_squared() < 1:
        return

    # Calculate the direction to move the camera in
    var direction = distance.normalized()

    # Calculate the amount to move the camera by this frame
    var speed = 500 # Adjust this value to control the camera speed
    var movement = direction * speed * delta

    # Move the camera towards the target
    set_global_position(get_global_position() + movement)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
extends Camera

export var speed: float = 5.0
var target_position: Vector3

func _process(delta):
    global_transform.origin = global_transform.origin.linear_interpolate(target_position, speed * delta)
```

```diff
- Syntax incorrect
! Camera does not exist in 4.x (should be Camera3D)
! export does not exist in 4.x (should be @export)
! linear_interpolate does not exist on Vector3 object

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _process(delta):
        # CAMERA MOVEMENT
        if target_position != null:
                smooth_camera_move(delta)
                global_position = lerp(global_position, target_position, 0.1)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Hallucinates unneeded smooth_camera_move function
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _process(delta):
        # Follow the mouse
        if target_position != get_global_mouse_position():
                target_position = get_global_mouse_position()
                smooth_camera(target_position)
```

```diff
+ Syntax correct

- Functionality incorrect
! Modifies target position
! Does not implement camera movement

- Verbosity bad
! Not attempt to implement movement logic
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _process(delta):
        if target_position:
                global_position = lerp(global_position, target_position, 10 * delta)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _process(delta):
        if target_position:
                global_position = lerp(global_position, target_position, 10 * delta)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _physics_process(delta: float) -> void:
        camera.global_position = camera.global_position.move_toward(target_position, camera_speed * delta)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Recursively find all child nodes of the input node and print the node path of each one.

#### gpt-3.5-turbo

```gdscript
func printChildNodePaths(node):
    # Print the current node's path
    print(node.get_path())

    # Recursively call printChildNodePaths() on each child node
    for child in node.get_children():
        printChildNodePaths(child)
```

```diff
+ Syntax correct
! Uses camel case for function name (non fatal)

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
func recursive_print_children(node):
    for child in node.get_children():
        print(child.get_path())
        recursive_print_children(child)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func find_all_child(node: Node) -> void:
        for child in node.get_children():
                print(child.get_path())
                find_all_child(child)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _find_nodes(node):
        for child in node.get_children():
                print(child.get_path())
                _find_nodes(child)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func print_tree(node: Node, indent: int = 0) -> void:
        for i in node.get_child_count():
                var child: Node = node.get_child(i)
                print(" " * indent + str(child.get_path()))
                print_tree(child, indent + 1)
```

```diff
- Syntax incorrect
! Uses * operator with string and int types
! Overrides engine-method with invalid signature

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func print_tree(node: Node) -> void:
        print(node.get_path())
        for child in node.get_children():
                print_tree(child)
```

```diff
- Syntax incorrect
! Overrides engine-method with invalid signature

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func print_node_path(node: Node) -> void:
        print(str(node.get_path()))
        for child in node.get_children():
                print_node_path(child)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Check the current OS. On Android, set all anchors of current node to one. On iOS, scale current node to half size.

#### gpt-3.5-turbo

```gdscript
# Check the current OS
if OS.get_name() == "Android":
    # Set all anchors of current node to one
    var rect = $Node.get_anchor_rect()
    rect.set_size(Vector2(1, 1))
    $Node.set_anchor_rect(rect)
elif OS.get_name() == "iOS":
    # Scale current node to half size
    $Node.set_scale(Vector2(0.5, 0.5))
```

```diff
- Syntax incorrect
! get_anchor_rect does not exist on Control object
! set_anchor_rect does not exist on Control object
! set_size does not exist and is not applicable to anchors

- Functionality incorrect
! Does not attempt to set all four anchors to 1

+ Verbosity good
```

#### gpt-4

```gdscript
if OS.get_name() == "Android":
    get_node(".").set_anchors_preset(Control.ANCHOR_PRESET_WIDE)
elif OS.get_name() == "iOS":
    get_node(".").rect_scale = Vector2(0.5, 0.5)
```

```diff
- Syntax incorrect
! Control.ANCHOR_PRESET_WIDE constant does not exist

- Functionality incorrect
! Does not attempt to set all four anchors to 1

- Verbosity bad
! get_node(".") calls are unnecessary
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():
        if OS.get_name() == "Android":
                set_anchors_preset(Control.PRESET_FULL_RECT)
        elif OS.get_name() == "iOS":
                scale *= 0.5
```

```diff
+ Syntax correct

- Functionality incorrect
! Selected preset only sets two of the four anchors to 1

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _ready():
        if (OS.get_name() == "Android"):
                self.anchor_left = 1
                self.anchor_top = 1
                self.anchor_right = 1
                self.anchor_bottom = 1
        elif (OS.get_name() == "iOS"):
                self.scale = Vector2(0.5, 0.5)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        if OS.get_name() == "Android":
                for anchor in current_anchors:
                        set_anchor(anchor, 1)
        elif OS.get_name() == "iOS":
                scale = Vector2(0.5, 0.5)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes existing array of Side enum values
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        if OS.get_name() == "Android":
                set_anchors_preset(Control.PRESET_FULL_RECT)
        elif OS.get_name() == "iOS":
                scale *= 0.5
```

```diff
+ Syntax correct

- Functionality incorrect
! Selected preset only sets two of the four anchors to 1

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready() -> void:
        if OS.get_name() == "Android":
                set_anchors_all(1)
        elif OS.get_name() == "iOS":
                scale = Vector2(0.5, 0.5)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes non-engine set_anchors_all method
```

---

### Calculate and print all prime numbers up to 1000.

#### gpt-3.5-turbo

```gdscript
func is_prime(n):
    if n <= 1:
        return false
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return false
    return true

for i in range(2, 1001):
    if is_prime(i):
        print(i)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Function to check if a number is prime
func is_prime(num):
    if num < 2:
        return false
    for i in range(2, num):
        if num % i == 0:
            return false
    return true

# Function to find all prime numbers up to n
func find_primes(n):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

# Calculate and print all prime numbers up to 1000
var primes = find_primes(1000)
print(primes)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func test():
        var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for i in range(1, 1001):
                if is_prime(i):
                        print(i)
                        primes.append(i)
```

```diff
+ Syntax correct

- Functionality incorrect
! Makes no attempt to calculate prime numbers
! Returns incorrect list

- Verbosity bad
! Assumes non-engine is_prime function
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func test():
        var primes = []
        for n in range(1, 1000):
                if is_prime(n):
                        primes.append(n)
                        print(n)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes non-engine is_prime function
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func test():
        var primes = []
        for i in range(2, 1000):
                if is_prime(i):
                        primes.append(i)
        print(primes)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes non-engine is_prime method
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func test():
        var primes = []
        for i in range(2, 1000):
                var is_prime = true
                for j in primes:
                        if i % j == 0:
                                is_prime = false
                                break
                if is_prime:
                        primes.append(i)
        print(primes)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func test():
        for i in range(1, 1000):
                if is_prime(i):
                        print(i)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes non-engine is_prime method
```

---

### Create a timer and connect to its timeout signal. Then start it with a random duration.

#### gpt-3.5-turbo

```gdscript
# Create a timer node
var timer = Timer.new()

# Connect to timeout signal
func _on_Timer_timeout():
    print("Timer completed")

timer.connect("timeout", self, "_on_Timer_timeout")

# Set a random duration between 1 and 10 seconds
var duration = rand_range(1, 10)

# Start the timer
timer.start(duration)
```

```diff
- Syntax incorrect
! Uses 3.x syntax for signal connections
! rand_range does not exist in 4.x (should be randf_range or randi_range)
! Does not add timer as child

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Import the random_number function
from random import random

# Create a timer
var timer = Timer.new()

# Connect to the timer's timeout signal
timer.connect("timeout", self, "_on_Timer_timeout")

# Add the timer as a child of the current node
add_child(timer)

# Set the timer's wait time to a random duration
timer.wait_time = random()

# Start the timer
timer.start()

# Define the method to be called when the timer emits the "timeout" signal
func _on_Timer_timeout():
    print("Timer finished")
```

```diff
- Syntax incorrect
! Uses 3.x syntax for signal connections
! random does not exist in 4.x (should be randf_range or randi_range)

+ Functionality correct

- Verbosity bad
! Uses useless Python-style import statement
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready() -> void:
        _timer = get_tree().create_timer(randf_range(0.1, 0.5))
        _timer.timeout.connect(_on_timer_timeout)
        _timer.start()
```

```diff
- Syntax incorrect
! start function does not exist on SceneTreeTimer object

+ Functionality correct

- Verbosity bad
! Unneeded start call
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _init():
        _timer = Timer.new()
        add_child(_timer)
        _timer.timeout.connect( self._on_timer_timeout )
        _timer.start( randf_range( 0.01, 0.05 ) )
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready() -> void:
        _timer = Timer.new()
        add_child(_timer)
        _timer.timeout.connect(_on_timer_timeout)
        _timer.start(randf_range(0.5, 1.0))
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready() -> void:
        timer = get_tree().create_timer(randf_range(min_delay, max_delay))
        timer.timeout.connect(_on_timer_timeout)
        timer.start()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready() -> void:
        _timer = Timer.new()
        _timer.one_shot = true
        _timer.timeout.connect(_on_timer_timeout)
        _timer.start(randf_range(MIN_DURATION, MAX_DURATION))
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Create a vertical container and populate it with colored rectangles. Each one should have a different color.

#### gpt-3.5-turbo

```gdscript
extends Control

func _ready():
    # Create a new vertical container
    var container = VBoxContainer.new()

    # Add the container to the scene
    add_child(container)

    # Define a list of colors
    var colors = [
        Color(1, 0, 0), # Red
        Color(0, 1, 0), # Green
        Color(0, 0, 1), # Blue
        Color(1, 1, 0), # Yellow
        Color(1, 0, 1), # Magenta
        Color(0, 1, 1)  # Cyan
    ]

    # Loop through each color in the list
    for color in colors:
        # Create a new colored rectangle
        var rect = ColorRect.new()
        rect.color = color

        # Add the rectangle to the container
        container.add_child(rect)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
extends Control

func _ready():
    # Create the VBoxContainer
    var vbox = VBoxContainer.new()
    # Add the VBoxContainer as a child of the root node
    add_child(vbox)

    # Create an array of colors for the colored rectangles
    var colors = [Color.red, Color.green, Color.blue, Color.yellow, Color.magenta, Color.cyan]

    # Iterate through the colors array and create ColorRect nodes
    for color in colors:
        # Create a ColorRect node
        var rect = ColorRect.new()
        # Set the color of the ColorRect node
        rect.color = color
        # Set the size of the ColorRect node
        rect.rect_min_size = Vector2(50, 50)
        # Add the ColorRect node as a child of the VBoxContainer
        vbox.add_child(rect)
```

```diff
- Syntax incorrect
! Color.red, Color.green etc. constants do not exist in 4.x (should be Color.RED etc.)
! rect_min_size does not exist in 4.x (should be custom_minimum_size)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func view():
        return\
        vbox({preset="expand-h"}, [
                color_rect({color=Color.RED}),
                color_rect({color=Color.GREEN}),
                color_rect({color=Color.BLUE}),
                color_rect({color=Color.YELLOW}),
                color_rect({color=Color.CYAN}),
                color_rect({color=Color.WHITE}),
                color_rect({color=Color.BLACK}),
                color_rect({color=Color.POWDER_BLUE}),
                color_rect({color=Color.POWDER_RED}),
                color_rect({color=Color.POWDER_GREEN}),
                color_rect({color=Color.POWDER_BLUE}),
                color_rect({color=Color.POWDER_YELLOW}),
                color_rect({color=Color.POWDER_CYAN}),
                color_rect({color=Color.POWDER_WHITE}),
                color_rect({color=Color.POWDER_BLACK}),
        ])
```

```diff
- Syntax incorrect
! Color.POWDER_X constants do not exist

- Functionality incorrect
! Makes no attempt at implementing any functionality, only calls non-engine functions

- Verbosity bad
! Does not follow instructions in a useful way
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func view():
        return\
        panel_container({},[
                hbox({preset="expand-h"},[
                        colorRect({color=Color.DARK_GREEN}),
                        colorRect({color=Color.GREEN}),
                        colorRect({color=Color.BLUE}),
                        colorRect({color=Color.POWDER_BLUE}),
                        colorRect({color=Color.VIOLET}),
                        colorRect({color=Color.ORANGE}),
                        colorRect({color=Color.RED}),
                ])
        ])
```

```diff
+ Syntax correct

- Functionality incorrect
! Makes no attempt at implementing any functionality, only calls non-engine functions

- Verbosity bad
! Does not follow instructions in a useful way
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func view():
        return\
        vbox({preset="expand-h"}, [
                color_rect({preset="expand-h", color=Color.RED}),
                color_rect({preset="expand-h", color=Color.GREEN}),
                color_rect({preset="expand-h", color=Color.BLUE}),
                color_rect({preset="expand-h", color=Color.YELLOW}),
                color_rect({preset="expand-h", color=Color.BLACK}),
                color_rect({preset="expand-h", color=Color.WHITE}),
        ])
```

```diff
+ Syntax correct

- Functionality incorrect
! Makes no attempt at implementing any functionality, only calls non-engine functions

- Verbosity bad
! Does not follow instructions in a useful way
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        var vbox = VBoxContainer.new()
        for i in 10:
                var rect = ColorRect.new()
                rect.color = Color.from_hsv(i/10.0, 0.8, 0.7)
                vbox.add_child(rect)
        add_child(vbox)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready() -> void:
        for i in 10:
                var color = Color(1, 1, 1, i * 0.1)
                var rect = ColorRect.new()
                rect.color = color
                add_child(rect)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not create a vertical container

+ Verbosity good
```

---

### Check if current node is visible, and change "color" shader param of the active material to red if it is.

#### gpt-3.5-turbo

```gdscript
if self.is_visible():
    material = self.get_material(0)
    if material:
        material.set_shader_param("color", Color(1, 0, 0))
```

```diff
- Syntax incorrect
! material property does not exist on any Node
! get_material does not exist on an Node
! set_shader_param does not exist in 4.x (should be set_shader_parameter)

+ Functionality correct

- Verbosity bad
! Unnecessary self references
```

#### gpt-4

```gdscript
if self.visible:
    self.get_active_material().set_shader_param("color", Color.red)
```

```diff
- Syntax incorrect
! get_active_material requires int parameter
! set_shader_param does not exist in 4.x (should be set_shader_parameter)
! Color.red constant does not exist in 4.x (should be Color.RED)

+ Functionality correct

- Verbosity bad
! Unnecessary self reference
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _process(delta):
        if self.visible:
                self.get_active_material(0).set_shader_parameter("color", Color(1,0,0))
        else:
                self.get_active_material(0).set_shader_parameter("color", Color(0,1,0))
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Unnecessary self references
! Unnecessary color change to green if not visible
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _process(delta):
        if self.visible:
                self.active_material.set_shader_parameter("color", Color(1, 0, 0))
```

```diff
- Syntax incorrect
! active_material property does not exist on any Node

+ Functionality correct

- Verbosity bad
! Unnecessary self references
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _process(_delta: float) -> void:
        if visible:
                _active_material.set_shader_parameter("color", Color.RED)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Does not retrieve active material, assumes it is already referenced
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _process(_delta: float) -> void:
        if visible:
                _active_material.set_shader_parameter("color", Color.RED)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Does not retrieve active material, assumes it is already referenced
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _process(_delta: float) -> void:
        if not visible:
                return
        active_material.set_shader_parameter("color", Color.RED)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Does not retrieve active material, assumes it is already referenced
```

---

### Return a list of medieval sounding male first names.

#### gpt-3.5-turbo

```gdscript
# Define arrays of name parts
var beginning = ["Al", "Ber", "Ced", "Dag", "Ead", "Frid"]
var middle = ["gar", "ric", "mund", "ulf", "fro"]
var end = ["ric", "bert", "hard", "fred", "win"]

# Define empty list to store names
var names = []

# Loop through name parts and concatenate them to create names
for i in range(10):
    var name = beginning[randi() % beginning.size()]
    name += middle[randi() % middle.size()]
    name += end[randi() % end.size()]
    names.append(name)

# Print out the list of names
print(names)
```

```diff
+ Syntax correct

- Functionality incorrect
! Creates hilarious but not particularly believable names

+ Verbosity good
```

#### gpt-4

```gdscript
func medieval_male_names():
    return ['Aethelwulf', 'Alaric', 'Alfred', 'Archibald', 'Arnulf', 'Arthur', 'Baldwin', 'Benedict', 'Bertrand', 'Bjorn', 'Charles', 'Cuthbert', 'Drogo', 'Eadric', 'Edgar', 'Edmund', 'Edward', 'Egbert', 'Emeric', 'Eric', 'Faramund', 'Ferdinand', 'Francis', 'Frederick', 'Geoffrey', 'Gerard', 'Godfrey', 'Godwin', 'Gustav', 'Harald', 'Henry', 'Hugo', 'Ingvar', 'Ivar', 'Leofric', 'Leopold', 'Ludwig', 'Magnus', 'Maurice', 'Nigel', 'Odo', 'Oswald', 'Percival', 'Ragnar', 'Ranulf', 'Raymond', 'Reynard', 'Richard', 'Robert', 'Roland', 'Rollo', 'Rudolf', 'Sigurd', 'Stephen', 'Sven', 'Theobald', 'Theodoric', 'Thomas', 'Ulf', 'Vladimir', 'Walter', 'William', 'Wolfgang', 'Wulfstan']
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func get_medieval_male_first_names():
        var names = []
        names.append("Albert")
        names.append("Arnold")
        names.append("Bernard")
        names.append("Charles")
        names.append("Edward")
        names.append("Ferdinand")
        names.append("Francis")
        names.append("Gilbert")
        names.append("Guy")
        names.append("Henry")
        names.append("James")
        names.append("John")
        names.append("Lawrence")
        names.append("Leonard")
        names.append("Louis")
        names.append("Mark")
        names.append("Martin")
        names.append("Matthew")
        names.append("Nicholas")
        names.append("Oliver")
        names.append("Philip")
        names.append("Richard")
        names.append("Robert")
        names.append("Roger")
        names.append("Samuel")
        names.append("Thomas")
        names.append("William")
        return names
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func medieval_sounding_first_names_male() -> Array:
        return medieval_sounding_first_names()[0]
```

```diff
+ Syntax correct

- Functionality incorrect
! Returns only first item returned from non-native function

- Verbosity bad
! Makes no attempt at implementing instruction
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func get_medieval_sounding_male_first_names() -> PackedStringArray:
        return [
                "Aaron",
                "Abel",
                "Abner",
                "Abraham",
                "Abram",
                "Adalbert",
                "Adam",
                "Adar",
                "Addison",
                "Adelbert",
                "Adolf",
                "Adolph",
                "Adonis",
                "Adrian",
                "Adriano",
                "Adriel",
                "Adrien",
                "Agustin",
                "Ahmad",
                "Ahmed",
                "Aidan",
                "Aiden",
                "Aime",
                "Akeem",
                "Al",
                "Alan",
                "Alban",
                "Albion",
                "Albert",
                "Alberto",
                "Albin",
                "Albrecht",
                "Alden",
                "Aldo",
                "Alec",
                "Aleck",
                "Alejandro",
                "Alessandro",
                "Alex",
                "Alexander",
                "Alexis",
                "Alf",
                "Alferd",
                "Alfonso",
                "Alfonzo",
                "Alford",
                "Alfred",
                "Alfredo",
                "Ali",
                "Allan",
                "Allen",
                "Alley",
                "Allie",
                "Allison",
                "Allyn",
                "Alphonse",
                "Alphonso",
                "Alton",
                "Alva",
                "Alvah",
                "Alvan",
                "Alvaro",
                "Alver",
                "Alvera",
                "Alverson",
                "Alvin",
                "Alyce",
                "Alys",
                "Alysa",
                "Alyse",
                "Alysia",
                "Alyson",
                "Alyss",
                "Alyssa",
                "Amado",
                ...
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func get_medieval_sounding_male_first_names() -> PackedStringArray:
        return [
                "Aaron",
                "Abel",
                "Abner",
                "Abraham",
                "Abram",
                "Achilles",
                "Adalbert",
                "Adam",
                "Adolph",
                "Adonis",
                "Adrian",
                "Adriano",
                "Agamemnon",
                "Agnes",
                "Agrippa",
                "Aharon",
                "Ahmad",
                "Ahmed",
                "Aidan",
                "Aiden",
                "Aime",
                "Aimee",
                "Aisha",
                "Akeem",
                "Al",
                "Alain",
                "Alan",
                "Alaric",
                "Alastair",
                "Alberic",
                "Albert",
                "Alberto",
                "Albin",
                "Alden",
                "Aldo",
                "Alec",
                "Aleck",
                "Alejandro",
                "Alessandro",
                "Alex",
                "Alexander",
                "Alexis",
                "Alf",
                "Alfie",
                "Alfred",
                "Alfredo",
                "Ali",
                "Alic",
                "Alistair",
                "Alister",
                "Allan",
                "Allen",
                "Alley",
                "Allie",
                "Allison",
                "Allyn",
                "Alphonse",
                "Alphonso",
                "Alton",
                "Alva",
                "Alvah",
                "Alvan",
                "Alvaro",
                "Alver",
                "Alvera",
                "Alverson",
                "Alvin",
                "Alyce",
                "Alys",
                "Alysa",
                "Alyse",
                "Alysia",
                "Alyson",
                "Alyss",
                ...
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_medieval_sounding_male_first_names() -> PackedStringArray:
        return [
                "Aaron",
                "Abel",
                "Abelard",
                "Abraham",
                "Abram",
                "Achilles",
                "Adalbert",
                "Adalberto",
                "Adam",
                "Adolfo",
                "Adolph",
                "Adolphus",
                "Adonis",
                "Adrian",
                "Adriano",
                "Adriel",
                "Adrien",
                "Agamemnon",
                "Agatha",
                "Agnes",
                "Agrippa",
                "Aharon",
                "Ahmad",
                "Ahmed",
                "Ahmet",
                "Aidan",
                "Aiden",
                "Aimil",
                "Aime",
                "Aimee",
                "Aisha",
                "Aislinn",
                "Akeem",
                "Al",
                "Alan",
                "Alban",
                "Albany",
                "Albert",
                "Alberto",
                "Albin",
                "Albrecht",
                "Alden",
                "Aldo",
                "Alec",
                "Aleck",
                "Alejandro",
                "Alessandro",
                "Alex",
                "Alexander",
                "Alexis",
                "Alf",
                "Alfonso",
                "Alfonzo",
                "Alford",
                "Alfred",
                "Alfredo",
                "Algernon",
                "Ali",
                "Alic",
                "Alicia",
                "Alijah",
                "Allan",
                "Allen",
                "Allison",
                "Allyn",
                "Alonso",
                "Alonzo",
                "Alphonse",
                "Alphonso",
                "Alton",
                "Alva",
                "Alvaro",
                "Alvin",
                ...
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Strip the input string of all white space, then replace all instances of "GPT" with "Dodo" and finally return an array containing each character in the string.

#### gpt-3.5-turbo

```gdscript
func transformString(input: String) -> Array:
	# Remove all white space from the input string
	var strippedString = input.replace(" ", "")

	# Replace all instances of "GPT" with "Dodo"
	strippedString = strippedString.replace("GPT", "Dodo")

	# Convert the transformed string into an array of characters
	var charArray = []
	for i in range(strippedString.length()):
		charArray.append(strippedString[i])

	return charArray
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
func strip_and_replace(input_string):
    stripped_string = input_string.replace(" ", "")
    replaced_string = stripped_string.replace("GPT", "Dodo")
    return [char for char in replaced_string]
```

```diff
- Syntax incorrect
! Invalid array initialization via "char for char in replaced_string"

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func string_to_ascii_array(string: String) -> PackedStringArray:
        var characters := PackedStringArray()
        string = string.strip_edges()
        for ch in string:
                if ch == "GPT":
                        ch = "Dodo"
                characters.append(ch)
        return characters
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not replace all white-space
! Does not replace GPT instances

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _humanize_token(token: String) -> Array:
        token = token.strip_edges()
        token = token.replace("GPT", "Dodo")
        return token.split("")
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not replace all white-space

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func string_to_array(text):
        text = text.strip_edges()
        text = text.replace("GPT", "Dodo")
        return list(text)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not replace all white-space

- Verbosity bad
! Assumes non-engine method to split string
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func string_to_array(text):
        text = text.strip_edges()
        text = text.replace("GPT", "Dodo")
        return list(text)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not replace all white-space

- Verbosity bad
! Assumes non-engine method to split string
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func clean_up_text(text: String) -> Array:
        text = text.strip_edges()
        text = text.replace("GPT", "Dodo")
        return text.to_ascii_buffer()
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not replace all white-space

+ Verbosity good
```

---

### Get volume of default audio bus and cap it at 20dB.

#### gpt-3.5-turbo

```gdscript
var volume = AudioServer.get_bus_volume_db(0)
if volume > 20:
    volume = 20
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Get current volume of default audio bus
current_volume = AudioServer.get_bus_volume_db(0)

# Cap the volume at 20dB
capped_volume = min(current_volume, 20)

# Set the capped volume as the new volume
AudioServer.set_bus_volume_db(0, capped_volume)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():
        default_volume = AudioServer.get_bus_volume_db(AudioServer.get_bus_index("Master"))
        default_volume = clamp(default_volume, -80, 20)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func get_default_volume() -> float:
        var bus_index = AudioServer.get_bus_index(DEFAULT_BUS)
        var volume = AudioServer.get_bus_volume_db(bus_index)
        volume = max(volume, -20)
        return volume
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not cap volume value

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func get_master_volume():
        var vol = AudioServer.get_bus_volume_db(AudioServer.get_bus_index("Master"))
        if vol > 20:
                vol = 20
        return vol
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func get_default_audio_volume() -> float:
        var bus_index: int = AudioServer.get_bus_index("Master")
        var volume_db: float = AudioServer.get_bus_volume_db(bus_index)
        volume_db = clampf(volume_db, -20.0, 20.0)
        return volume_db
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_default_volume():
        var volume = AudioServer.get_bus_volume_db(AudioServer.get_default_bus_index())
        if volume > 20:
                volume = 20
        return volume
```

```diff
- Syntax incorrect
! get_default_bus_index does not exist in AudioServer

+ Functionality correct

+ Verbosity good
```

---

### Get the currently active camera and change its projection to orthogonal. If code is executed in-editor, change to frustum projection.

#### gpt-3.5-turbo

```gdscript
var current_camera = get_viewport().get_camera()
if Engine.editor_hint:
    current_camera.projection = Camera.PROJECTION_FRUSTUM
else:
    current_camera.projection = Camera.PROJECTION_ORTHOGONAL
```

```diff
- Syntax incorrect
! get_camera does not exist in 4.x (should be get_camera_3d)
! Engine.editor_hint does not exist in 4.x (should be is_editor_hint)
! Camera does not exist in 4.x (should be Camera3D)

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Get the currently active camera
var camera = get_viewport().get_camera()

if Engine.editor_hint:
    # Change to frustum projection
    camera.projection = Camera.PROJECTION_PERSPECTIVE
else:
    # Change to orthogonal projection
    camera.projection = Camera.PROJECTION_ORTHOGONAL
```

```diff
- Syntax incorrect
! get_camera does not exist in 4.x (should be get_camera_3d)
! Engine.editor_hint does not exist in 4.x (should be is_editor_hint)
! Camera does not exist in 4.x (should be Camera3D)

- Functionality incorrect
! Sets projection to perspective, not frustum

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():
        camera = get_current_camera()
        if Engine.is_editor_hint():
                camera.projection = Camera.PROJECTION_FRUSTUM
        else:
                camera.projection = Camera.PROJECTION_ORTHOGONAL
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Uses non-engine function get_current_camera to retrieve camera instead of implementing logic
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _change_to_orthogonal():
        var cam = get_current_camera2d()
        if Engine.is_editor_hint():
                cam.set_projection(Camera2D.PROJECTION_FRUSTUM)
        else:
                cam.set_orthogonal(true)
```

```diff
- Syntax incorrect
! Camera2D.PROJECTION_FRUSTUM does not exist

- Functionality incorrect
! Attempts to retrieve 2D camera, which does not support projections

- Verbosity bad
! Uses non-engine function get_current_camera2d to retrieve camera instead of implementing logic
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        camera = get_viewport().get_camera_3d()
        if Engine.is_editor_hint():
                _change_to_orthogonal()
        else:
                _change_to_frustrum()
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
!Assumes non-engine _change_to_orthogonal method
!Assumes non-engine _change_to_frustrum method
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        camera = get_viewport().get_camera_3d()
        if Engine.is_editor_hint():
                _change_to_orthogonal()
        else:
                _change_to_frustrum()
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
!Assumes non-engine _change_to_orthogonal method
!Assumes non-engine _change_to_frustrum method
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready() -> void:
        camera = get_viewport().get_camera_2d()
        if Engine.is_editor_hint():
                camera.projection = Camera2D.PROJECTION_FRUSTUM
        else:
                camera.projection = Camera2D.PROJECTION_ORTHOGONAL
```

```diff
- Syntax incorrect
!PROJECTION_FRUSTUM does not exist in Camera2D

- Functionality incorrect
!Attempts to change projection on 2D camera

+ Verbosity good
```

---

### Create a blue button with the text "Dodos are my favorite flightless bird" and connect its pressed signal to on_dodo_pressed.

#### gpt-3.5-turbo

```gdscript
extends Button

func _ready():
    self.text = "Dodos are my favorite flightless bird"
    self.modulate = Color(0.2, 0.2, 1)

func _on_Button_pressed():
    on_dodo_pressed()

func on_dodo_pressed():
    # Add your code here to handle the button press event
    pass
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not connect pressed signal

- Verbosity bad
! Does not create button, assumes it already exists
```

#### gpt-4

```gdscript
# First, create a new Button node in your scene and set its name to "DodoButton"
# Set the button's text to "Dodos are my favorite flightless bird"
# Set the button's modulate to blue

# In the script attached to the node containing the button, add the following code

func _ready():
    $DodoButton.connect("pressed", self, "on_dodo_pressed")
    $DodoButton.modulate = Color.blue
    $DodoButton.text = "Dodos are my favorite flightless bird"

func on_dodo_pressed():
    print("Dodo button has been pressed")
```

```diff
- Syntax incorrect
! Uses 3x syntax for signal connection
! Color.blue does not exist in 4.x (should be Color.BLUE)

+ Functionality correct

- Verbosity bad
! Does not create button, assumes it already exists
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():
        var button = Button.new()
        button.text = "Dodos are my favorite flightless bird"
        button.pressed.connect(on_dodo_pressed)
        button.color = Color.BLUE
```

```diff
- Syntax incorrect
! color property does not exist in Button object

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _ready():
        var button = Button.new()
        button.text = "Dodos are my favorite flightless bird"
        button.modulate = Color.BLUE
        button.pressed.connect(on_dodo_pressed)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        var button = BlueButton.instantiate()
        button.text = "Dodos are my favorite flightless bird"
        button.pressed.connect(on_dodo_pressed)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes BlueButton PackedScene reference implementing button color
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        var button = BlueButton.instantiate()
        button.text = "Dodos are my favorite flightless bird"
        button.pressed.connect(on_dodo_pressed)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes BlueButton PackedScene reference implementing button color
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready():
        button = Button.new()
        button.text = "Dodos are my favorite flightless bird"
        button.connect("pressed", on_dodo_pressed)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not attempt to assign color

+ Verbosity good
```

---

### Return the current project version.

#### gpt-3.5-turbo

```gdscript
var version = ProjectSettings.get_setting("application/config/version")
print("Current project version: ", version)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
func get_project_version():
    return ProjectSettings.get("config_version")
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func get_version() -> String:
        return ProjectSettings.get_setting("application/config/version")
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func get_version() -> String:
        return _current_project_version
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Makes no attempt at retrieving version from a globally accessible place such as the project settings
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func get_version() -> String:
        return ProjectSettings.get_setting("application/config/version")
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func get_version() -> String:
        return ProjectSettings.get_setting("application/config/version")
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_version() -> String:
        return current_version
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
!Assumes existing value, does not attempt to fetch version
```

---

### Convert input object to JSON string and save in user directory as tmp.json. Return success message if successful.

#### gpt-3.5-turbo

```gdscript
# Assuming the input object is already defined and populated

# Convert the input object to a JSON formatted string
var json_str = JSON.print(input)

# Define the file path to save the JSON string
var file_path = OS.get_user_data_dir() + "/tmp.json"

# Open the file for writing
var file = File.new()
if file.open(file_path, File.WRITE) == OK:
    # Write the JSON string to the file
    file.store_string(json_str)
    # Close the file
    file.close()
    # Return success message
    return "JSON string saved to file: " + file_path
else:
    # If file could not be opened for writing, return error message
    return "Error: Could not open file for writing"
```

```diff
- Syntax incorrect
! JSON.print does not exist in 4.x (should be JSON.stringify)
! File does not exist in 4.x (should be FileAccess)

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
extends Node

var input_object = {"name": "John", "age": 30, "city": "New York"}
var file_path = "user://tmp.json"

func _ready():
	print(save_json(input_object))

func save_json(input_object):
	var json_string = JSON.print(input_object)
	var file = File.new()
	var error = file.open(file_path, File.WRITE)
	if error != OK:
		return "Failed to open file"
	file.store_line(json_string)
	file.close()
	return "Successfully saved JSON string to tmp.json"
```

```diff
- Syntax incorrect
! JSON.print does not exist in 4.x (should be JSON.stringify)
! File does not exist in 4.x (should be FileAccess)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _import(source_file: String, save_path: String, options: Dictionary, platform_variants: Array[String], gen_files: Array[String]) -> int:
        if source_file.get_extension() == "dch":
                source_file = source_file.get_basename() + ".json"
        var file = FileAccess.open(source_file, FileAccess.READ)
        if file == null:
                return ERR_FILE_CANT_READ
        var json = JSON.new()
        var err = json.parse(file.get_as_text())
        if err != OK:
                return err
        var data = json.get_data()
        if data == null:
                return ERR_JSON_PARSE_ERROR
        file = FileAccess.open(save_path, FileAccess.WRITE)
        if file == null:
                return ERR_FILE_CANT_WRITE
        file.store_string(JSON.stringify(data))
        return OK
```

```diff
- Syntax incorrect
! ERR_JSON_PARSE_ERROR constant does not exist

- Functionality incorrect
! Does not convert input object, instead opens source file and re-saves it

- Verbosity bad
! Has multiple unneeded function parameters
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _import(object, save_path, options, platform_variants, gen_files):
        var json_string = JSON.stringify(object)
        var file = FileAccess.open("user://tmp.json", FileAccess.WRITE)
        if FileAccess.get_open_error() == OK:
                file.store_string(json_string)
                file.close()
        return "User directory saved as tmp.json"
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Has multiple unneeded function parameters
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func save_json(object):
        var json = JSON.stringify(object)
        var file = FileAccess.open("user://tmp.json", FileAccess.WRITE)
        if file:
                file.store_string(json)
                file = null
                return "SUCCESS"
        else:
                return "ERROR"
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func save_object(object):
        var json_string = JSON.stringify(object)
        var file = FileAccess.open("user://tmp.json", FileAccess.WRITE)
        if file:
                file.store_string(json_string)
                file = null
                return "SUCCESS"
        else:
                return "ERROR"
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func save_json(object):
        var json = JSON.stringify(object)
        var file = FileAccess.open("user://tmp.json", FileAccess.WRITE)
        file.store_string(json)
        return "Success"
```

```diff
+ Syntax correct

- Functionality incorrect
! Always returns success message

+ Verbosity good
```

---

### Get the current local system time. If it is past 10pm, close the app. Otherwise, print "It's still early. :)".

#### gpt-3.5-turbo

```gdscript
var date = OS.get_datetime()
var hour = date.hour
if hour >= 22:
    get_tree().quit()
else:
    print("It's still early. :)")
```

```diff
- Syntax incorrect
! OS.get_datetime does not exist in 4.x (should be Time.get_datetime_dict_from_system)

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
import datetime

func _ready():
    var current_time = datetime.datetime.now().time()
    if current_time.hour >= 22:
        get_tree().quit()
    else:
        print("It's still early. :)")
```

```diff
- Syntax incorrect
! Uses nonexistent datetime syntax

+ Functionality correct

- Verbosity bad
! Uses Python-like import statement
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():
        now = Time.get_datetime_dict_from_system()
        if now.hour > 22:
                close()
        else:
                print("It's still early. :)")
```

```diff
+ Syntax correct

- Functionality incorrect
! Only closes app starting at 11pm

- Verbosity bad
! Does not implement app quit, call non-engine function instead
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _process(_delta):
        var now = Time.get_datetime_dict_from_system()
        if now.hour > 22:
                get_tree().quit()
        else:
                print("It's still early. :)")
```

```diff
+ Syntax correct

- Functionality incorrect
! Only closes app starting at 11pm

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        var currentTime = Time.get_datetime_dict_from_system()
        if (currentTime.hour > 22):
                get_tree().quit()
        else:
                print("It's still early. :)")
```

```diff
+ Syntax correct

- Functionality incorrect
! Only closes app starting at 11pm

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        var currentTime = Time.get_datetime_dict_from_system()
        if (currentTime["hour"] > 22):
                get_tree().quit()
        else:
                print("It's still early. :)")
```

```diff
+ Syntax correct

- Functionality incorrect
! Only closes app starting at 11pm

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _process(delta):
        var time = Time.get_datetime_string_from_system()
        var hour = int(time.split(" ")[1].split(":")[0])
        if hour > 22:
                get_tree().quit()
        else:
                print("It's still early. :)")
```

```diff
+ Syntax correct

- Functionality incorrect
! No space in datetime string, hence 1 is an invalid index

+ Verbosity good
```

---

### Get dot product of two input vectors and floor it, then return as string.

#### gpt-3.5-turbo

```gdscript
# Assume the two input vectors are represented as arrays of numbers.
# For example, [1, 2, 3] and [4, 5, 6] are two input vectors.
# The dot product of these two vectors is 1*4 + 2*5 + 3*6 = 32.

func get_floor_dot_product(vector1: Array, vector2: Array) -> String:
    var dot_product = 0
    for i in range(vector1.size()):
        dot_product += vector1[i] * vector2[i]
    var floor_dot_product = floor(dot_product)
    return str(floor_dot_product)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Ignores native Vector3 object in favor of arrays and manual calculation
```

#### gpt-4

```gdscript
func get_dot_product_string(vector1: Vector2, vector2: Vector2) -> String:
    var dot_product = vector1.dot(vector2)
    var floored_dot_product = int(dot_product)
    return str(floored_dot_product)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _get_code(input_vars, output_vars, mode, type):
        var uv = "UV"

        if input_vars[0]:
                uv = input_vars[0]

        return "%s = floor(%s.xy * %s.xy);" % [output_vars[0], uv, input_vars[1]]
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not calculate a dot product
! Does not floor any result

- Verbosity bad
! Includes multiple useless parameters
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _get_code(input_vars, output_vars, mode, type):
        var uv = "UV"

        if input_vars[0]:
                uv = input_vars[0]

        return "%s.xy = floor(%s.xy dot %s.xy);" % [output_vars[0], uv, input_vars[1]]
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not calculate a dot product
! Does not floor any result

- Verbosity bad
! Includes multiple useless parameters
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _get_code(input_vars, output_vars, mode, type):
        var uv = "UV"

        if input_vars[0]:
                uv = input_vars[0]

        return "%s = floor(dot(%s.xy, %s.xy));" % [
```

```diff
- Syntax incorrect
! Ends on open bracket

- Functionality incorrect
! Does not calculate a dot product
! Does not floor any result

- Verbosity bad
! Includes multiple useless parameters
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _get_code(input_vars, output_vars, mode, type):
        var uv = "UV"

        if input_vars[0]:
                uv = input_vars[0]

        return "%s = floor(dot(%s.xy, %s.xy));" % [output_vars[0], uv, input_vars[1]]
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not calculate a dot product
! Does not floor any result

- Verbosity bad
! Includes multiple useless parameters
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _get_code(input_vars, output_vars, mode, type):
        var uv = "UV"

        if input_vars[0]:
                uv = input_vars[0]

        return "%s = floor(dot(%s.xy - %s.xy, %s.xy));" % [output_vars[0], uv, input_vars[1], input_vars[2]]
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not calculate a dot product
! Does not floor any result

- Verbosity bad
! Includes multiple useless parameters
```

---

### Create a raycast and cast from active camera to current node. Return ray collisions.

#### gpt-3.5-turbo

```gdscript
# Get active camera
var camera = get_viewport().get_camera()

# Get ray from camera
var ray = camera.get_ray()

# Perform raycast and get collisions
var collisions = get_world().get_direct_space_state().intersect_ray(ray.origin, ray.origin + ray.direction * 1000, [self])

# Return collisions
return collisions
```

```diff
- Syntax incorrect
! get_camera does not exist in 4x (should be get_camera_3d)
! get_ray does not exit in Camera3D object
! get_world does not exist in 4x (should be get_world_3d)
! intersect_ray only takes a single parameter of type PhysicsRayQueryParameters3D

- Functionality incorrect
! Does not cast a ray rowards the current node

+ Verbosity good
```

#### gpt-4

```gdscript
extends Node

func _ready():
    var camera = get_viewport().get_camera()
    var ray_origin = camera.project_ray_origin(get_viewport().size / 2)
    var ray_end = ray_origin + camera.project_ray_normal(get_viewport().size / 2) * 1000

    var space_state = get_world().direct_space_state
    var result = space_state.intersect_ray(ray_origin, ray_end)

    if result:
        print("Ray collided with: ", result.collider.name)
    else:
        print("No collision detected")
```

```diff
- Syntax incorrect
! get_camera does not exist in 4x (should be get_camera_3d)
! get_world does not exist in 4x (should be get_world_3d)
! get_world_3d is only available in Node3D objects
! intersect_ray only takes a single parameter of type PhysicsRayQueryParameters3D

- Functionality incorrect
! Does not cast a ray rowards the current node

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _get_colliding_bodies():
        var space_state = get_viewport().get_world_3d().direct_space_state
        var camera = get_viewport().get_camera_3d()
        var from = camera.project_ray_origin(get_global_mouse_position())
        var to = from + camera.project_ray_normal(get_global_mouse_position()) * 100.0
        var ray = PhysicsRayQueryParameters3D.new()
        ray.from = from
        ray.to = to
        return space_state.intersect_ray(ray)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not cast a ray towards the current node

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _get_active_raycast():
        var camera = get_viewport().get_camera_3d()
        var from = camera.project_ray_origin(camera.get_screen_transform().basis.y)
        var to = from + camera.project_ray_normal(camera.get_screen_transform().basis.y) * 100
        var ray = PhysicsRayQueryParameters3D.new()
        ray.from = from
        ray.to = to
        return get_world_3d().direct_space_state.intersect_ray(ray)
```

```diff
- Syntax incorrect
! get_screen_transform does not exist in Camera3D object

- Functionality incorrect
! Does not cast a ray towards the current node

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func raycast_from_active_camera():
        var space_state = get_world_3d().direct_space_state
        var from = get_active_camera().project_ray_origin(get_viewport().get_mouse_position())
        var to = from + get_active_camera().project_ray_normal(get_viewport().get_mouse_position()) * 100
        var ray = PhysicsRayQueryParameters3D.create(from, to)
        return space_state.intersect_ray(ray)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not cast a ray towards the current node

- Verbosity bad
! Assumes non-engine get_active_camera method
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func raycast_from_active_camera():
        var space_state = get_world_3d().direct_space_state
        var from = get_active_camera().project_ray_origin(get_viewport().get_mouse_position())
        var to = from + get_active_camera().project_ray_normal(get_viewport().get_mouse_position()) * 1000
        var ray_query = PhysicsRayQueryParameters3D.create(from, to)
        return space_state.intersect_ray(ray_query)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not cast a ray towards the current node

- Verbosity bad
! Assumes non-engine get_active_camera method
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func raycast_from_active_camera():
        var camera = get_viewport().get_camera_2d()
        var space_state = get_world_2d().direct_space_state
        var ray = PhysicsRayQueryParameters2D.create(camera.global_position, global_position)
        return space_state.intersect_ray(ray)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Bounce current control node off top and bottom edges of the screen, moving it each frame.

#### gpt-3.5-turbo

```gdscript
# Get the size of the viewport
var viewport_size = get_viewport_rect().size

# Calculate the maximum y position of the control node
var max_y = viewport_size.y - control_node.get_size().y

# Calculate the new y position of the control node
var new_y = control_node.position.y + control_node.velocity.y

# Check if the control node has hit the top or bottom edge of the screen
if new_y < 0:
    new_y = abs(new_y)
    control_node.velocity.y = -control_node.velocity.y
elif new_y > max_y:
    new_y = max_y - (new_y - max_y)
    control_node.velocity.y = -control_node.velocity.y

# Update the position of the control node
control_node.position.y = new_y
```

```diff
- Syntax incorrect
! velocity does not exist in Control object

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Assuming that the node which this script is attached to is the control node to be bounced. Please, attach this script to a control node and adjust the speed value as needed.

extends Control

var speed = Vector2(0, 200)  # Adjust the speed value as needed

func _ready():
    set_process(true)

func _process(delta):
    var target_position = position + speed * delta
    if target_position.y < 0 or target_position.y + rect_size.y > get_viewport_rect().size.y:
        speed.y = -speed.y
    position += speed * delta
```

```diff
- Syntax incorrect
! rect_size does not exist in 4.x (should be size)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _physics_process(delta: float) -> void:
        if not visible:
                return

        if (position.y - sprite_height) < 0:
                velocity.y = (position.y - sprite_height) * bounce_speed
                move_and_collide(velocity * delta)
                velocity.y = 0
        elif (position.y + sprite_height) > window_size.y:
                velocity.y = (position.y + sprite_height) * bounce_speed
                move_and_collide(velocity * delta)
                velocity.y = 0

        if (position.x - sprite_width) < 0:
                velocity.x = (position.x - sprite_width) * bounce_speed
                move_and_collide(velocity * delta)
                velocity.x = 0
        elif (position.x + sprite_width) > window_size.x:
                velocity.x = (position.x + sprite_width) * bounce_speed
                move_and_collide(velocity * delta)
                velocity.x = 0
```

```diff
+ Syntax correct

- Functionality incorrect
! Moves PhysicsBody2D instead of Control node

- Verbosity bad
! Assumes a lot of pre-existing values instead of calculating them
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _process(delta):
        if not current:
                return

        current.position.y = screen_size.y - current.size.y
        current.position = current.position.bounce(Vector2(0, screen_size.y))
        current.position.y = 0
        pass
```

```diff
- Syntax incorrect
! bounce does not existing in Vector2 object

- Functionality incorrect
! Does not correctly move and bounce the current node

- Verbosity bad
! Does not attempt to implement instructions
! Adds useless pass at end of function
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _process(delta):
        if (position.y - control.size.y / 2 - gap_offset < 0):
                velocity.y = abs(velocity.y)
        elif (position.y + control.size.y / 2 + gap_offset > screen_size.y):
                velocity.y = -abs(velocity.y)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not apply velocity

- Verbosity bad
! Assumes screen size value has already been retrieved
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _process(delta):
        if (position.y - control.size.y / 2 - gap_offset < 0):
                velocity.y = abs(velocity.y)
        elif (position.y + control.size.y / 2 + gap_offset > screen_size.y):
                velocity.y = -abs(velocity.y)
        position += velocity * delta
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes screen size value has already been retrieved
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _physics_process(delta: float) -> void:
        if not is_inside_tree():
                await ready

        if position.y < 0:
                position.y = -position.y
        elif position.y > get_viewport_rect().size.y:
                position.y = get_viewport_rect().size.y - (position.y - get_viewport_rect().size.y)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not move node unless outside of screen

+ Verbosity good
```

---

### Make a POST request to https://example.com with a JSON payload of {test: "value"}

#### gpt-3.5-turbo

```gdscript
# Create the request body
var payload = {"test": "value"}

# Create the HTTP request
var request = HTTPRequest.new()
request.request("https://example.com", {"Content-Type": "application/json"}, JSON.print(payload), HTTPClient.METHOD_POST)

# Print the response
print(request.get_response_body_as_text())
```

```diff
- Syntax incorrect
! request params are incorrect. Requires string array for headers, and method type as third parameter instead of fourth
! get_response_body_as_text does not exist in HttpRequest object

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
extends HTTPRequest

func _ready():
    make_post_request("https://example.com", {"test": "value"})

func make_post_request(url, payload):
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    var body = to_json(payload).to_utf8()
    request(url, headers = request_headers, body = body, method = HTTPClient.METHOD_POST)

func _on_request_completed(result, response_code, headers, body):
    if response_code == 200:
        print("Request succeeded.")
        var response = parse_json(body.get_string_from_utf8())
        print("Response: ", response)
    else:
        print("Request failed. Response code: ", response_code)
```

```diff
- Syntax incorrect
! request params are incorrect. Requires string array for headers, and method type as third parameter instead of fourth

+ Functionality correct

- Verbosity bad
! Uses non-engine to_json and get_json functions instead of existing JSON class
! Does not create an HttpRequest object, instead extends the class
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func test_request():
        var request = HTTPRequest.new()
        add_child(request)
        request.request("https://example.com", [USER_AGENT, "Content-Type: application/json"], JSON.stringify({test: "value"}))
```

```diff
- Syntax incorrect
! request params are incorrect. Requires method type as third parameter
! Payload key is not a string

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func test_explicit_json_payload():
        var response = await make_request(
                "https://example.com",
                ["Content-Type: application/json"],
                true,
                JSON.stringify({test: "value"))
        assert_that(response.code).is_equal(200)
```

```diff
- Syntax incorrect
! No closing } for payload
! assert_that().is_equal() syntax makes little sense

+ Functionality correct

- Verbosity bad
! Assumes non-engine make_request function to handle request
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func test_example():
        var json = JSON.stringify({test="value"})
        var headers := PackedStringArray([
                "Content-Type: application/json",
                "Content-Length: " + str(json.length()),
        ])
        var body := json.to_utf8_buffer()
        var request := HTTPRequest.new()
        add_child(request)
        request.request("https://example.com", headers, HTTPClient.METHOD_POST, body)
```

```diff
- Syntax incorrect
! Uses request instead of request_raw despite binary payload

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func test_example():
        var body = JSON.stringify({test="value"})
        var headers := PackedStringArray([
                "Content-Type: application/json",
                "Content-Length: %d" % body.length()
        ])
        var request := HTTPRequest.new()
        add_child(request)
        request.request("https://example.com", headers, HTTPClient.METHOD_POST, body)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _on_request_pressed():
        var error = http_request.request("https://example.com", [USER_AGENT, "Content-Type: application/json"], HTTPClient.METHOD_POST, JSON.stringify({"test": "value"}))
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes HttpRequest object already exists
```

---

### Get each child node that is a ColorRect and return found nodes as an array.

#### gpt-3.5-turbo

```gdscript
var colorRectNodes = []

# Loop through all child nodes
for node in get_children():
    # Check if node is a ColorRect
    if node is ColorRect:
        # Add node to array
        colorRectNodes.append(node)

# Return array of found ColorRect nodes
return colorRectNodes
```

```diff
+ Syntax correct
! Uses camel case for array variable (non-fatal)

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Assuming this is a method inside a class that extends Node or one of its subclasses
func get_colorrect_child_nodes():
    var colorrect_nodes = []
    for child in get_children():
        if child is ColorRect:
            colorrect_nodes.append(child)
    return colorrect_nodes
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _get_color_rects() -> Array[ColorRect]:
        var found := []
        for child in get_children():
                if child is ColorRect:
                        found.append(child)
        return found
```

```diff
- Syntax incorrect
! Array[ColorRect] type is only valid if found array is initialized as such

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func get_color_rects() -> Array[ColorRect]:
        var arr: Array[ColorRect] = []
        for node in get_children():
                if node is ColorRect:
                        arr.append(node)
        return arr
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func get_color_rects() -> Array[ColorRect]:
        var arr: Array[ColorRect] = []
        for child in get_children():
                if child is ColorRect:
                        arr.append(child)
        return arr
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _get_color_rects() -> Array[ColorRect]:
        var nodes: Array[ColorRect]
        for node in get_children():
                if node is ColorRect:
                        nodes.append(node)
        return nodes
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_color_rects() -> Array[ColorRect]:
        var color_rects := []
        for child in get_children():
                if child is ColorRect:
                        color_rects.append(child)
        return color_rects
```

```diff
+ Syntax correct

- Functionality incorrect
! Returns Array type despite Array[ColorRect] specified

+ Verbosity good
```

---

### Create a two dimensional array of size 64\*64 with default boolean values of false.

#### gpt-3.5-turbo

```gdscript
var myArray = []
for i in range(64):
    var row = []
    for j in range(64):
        row.append(false)
    myArray.append(row)
```

```diff
+ Syntax correct
! Uses camel case for array variable (non-fatal)

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
var array = []
for i in range(64):
    array.append([])
    for j in range(64):
        array[i].append(false)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func init_2d_array():
        for i in range(64):
                for j in range(64):
                        array[i][j] = false
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes array already exists instead of creating it
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _ready():
        for i in 64:
                for j in 64:
                        data[i][j] = false
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes array already exists instead of creating it
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        randomize()
        world = []
        for i in range(64):
                world.append([])
                for j in range(64):
                        world[i].append(false)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Useless randomize call
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        randomize()
        world = []
        for i in range(64):
                world.append([])
                for j in range(64):
                        world[i].append(false)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Useless randomize call
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready():
        for i in range(64):
                array.append([])
                for j in range(64):
                        array[i].append(false)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes array is already initialized
```

---

### If the input strings second character is an "m", throw an error.

#### gpt-3.5-turbo

```gdscript
# Assuming the input string is stored in a variable called 'input_str'

if input_str[1] == 'm':
    raise ValueError("Second character cannot be 'm'")
```

```diff
- Syntax incorrect
! raise does not exist in GDScript
! ValueError does not exist

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
func check_second_char(input_string: String):
    if input_string[1] == "m":
        raise("Error: The second character is an 'm'.")
```

```diff
- Syntax incorrect
! raise does not exist in GDScript

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _init(first: String, second: String):
        if second.begins_with("m"):
                assert(false)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not check for second character

- Verbosity bad
! Takes two arguments instead of one
! Does not include error message in assert call
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _init(s,e):
                super(s,e)
                if s.length() > 1 and s[1] == "m":
                        error("Invalid interval notation: 'm' is not a valid modifier")
```

```diff
- Syntax incorrect
! Arguments can't be passed to existing _init function via super call

+ Functionality correct

- Verbosity bad
! Takes two arguments instead of one
! Assumes non-engine error function
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func set_time(h: String, m: String, s: String) -> void:
        if m.right(1) == "m":
                push_error("Invalid time!")
                return
```

```diff
+ Syntax correct

- Functionality incorrect
! Only checks second character if string length is 2

- Verbosity bad
! Takes three arguments instead of one
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func set_time(h: String, m: String, s: String) -> void:
        if m.right(1) == "m":
                push_error("Invalid time!")
                return
```

```diff
+ Syntax correct

- Functionality incorrect
! Only checks second character if string length is 2

- Verbosity bad
! Takes three arguments instead of one
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _init(s: String):
                super(s)
                if s.length() > 1 and s[1] == "m":
                        push_error("Invalid time string: " + s)
```

```diff
- Syntax incorrect
! Invalid argment count for _init super call

+ Functionality correct

+ Verbosity good
```

---

### Every 0.2s, print the milliseconds elapsed since calling this function. Exit after 10s have passed.

#### gpt-3.5-turbo

```gdscript
func print_elapsed_time():
    var start_time = OS.get_ticks_usec()
    var elapsed_time = 0
    while elapsed_time < 10000000:
        elapsed_time = (OS.get_ticks_usec() - start_time) / 1000
        print("Milliseconds elapsed: ", elapsed_time)
        yield(get_tree().create_timer(0.2), "timeout")
```

```diff
- Syntax incorrect
! OS.get_ticks_usec does not exist in 4.x (should be Time.get_ticks_usec)
! Uses yield instead of await

- Functionality incorrect
! Runs for longer than 10 seconds

+ Verbosity good
```

#### gpt-4

```gdscript
extends Node

var total_time = 0
var timer = null

func _ready():
    timer = Timer.new()
    timer.set_wait_time(0.2)
    timer.connect("timeout", self, "_on_Timer_timeout")
    add_child(timer)
    timer.start()

func _on_Timer_timeout():
    if total_time <= 10:
        print(OS.get_ticks_msec())
        total_time += 0.2
    else:
        timer.stop()
```

```diff
- Syntax incorrect
! Uses 3.x syntax for connecting signals
! OS.get_ticks_msec does not exist in 4.x (should be Time.get_ticks_msec)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _process(delta):
        print(Time.get_ticks_msec() - _start)
        if Time.get_ticks_msec() - _start > 1000*10:
                exit()
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not print every 0.2 seconds

- Verbosity bad
! Assumes non-engine exit function
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _process(delta):
        print(Time.get_ticks_msec() - start_time)

        if (Time.get_ticks_msec() - start_time) > 10000:
                exit()

        await get_tree().create_timer(0.2).timeout
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not print every 0.2 seconds

- Verbosity bad
! Assumes non-engine exit function
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _process(delta):
        static_print(Time.get_ticks_msec() - _start)
        if Time.get_ticks_msec() - _start > 10000:
                get_tree().quit()
        await get_tree().create_timer(0.2).timeout
```

```diff
+ Syntax correct

- Functionality incorrect
! Prints every frame

- Verbosity bad
! Assumes unneeded static_print method instead of using print
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _process(delta):
        static_print(Time.get_ticks_msec())
        if Time.get_ticks_msec() - start > 10000:
                get_tree().quit()
        await get_tree().create_timer(0.2).timeout
```

```diff
+ Syntax correct

- Functionality incorrect
! Prints every frame

- Verbosity bad
! Assumes unneeded static_print method instead of using print
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _process(delta):
        print(Time.get_ticks_msec() - start)
        if Time.get_ticks_msec() - start > 10000:
                get_tree().quit()
```

```diff
+ Syntax correct

- Functionality incorrect
! Prints every frame

- Verbosity bad
! Makes no attempt to wait 0.2 seconds
```

---

### Check if a "MyAndroidPlugin" singleton exists, and assign to my_plugin if so.

#### gpt-3.5-turbo

```gdscript
var my_plugin = null
if Engine.has_singleton("MyAndroidPlugin"):
    my_plugin = Engine.get_singleton("MyAndroidPlugin")
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
if Engine.has_singleton("MyAndroidPlugin"):
    my_plugin = Engine.get_singleton("MyAndroidPlugin")
else:
    my_plugin = null
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _enter_tree() -> void:
        var plugin := get_editor_interface().get_singleton("MyAndroidPlugin")
        if plugin:
                my_plugin = plugin
```

```diff
- Syntax incorrect
! get_singleton does not exist in EditorPlugin object

- Functionality incorrect
! Looks for editor plugin rather than Android one

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _init():
        var my_plugin = null
        if Java.has_singleton("MyAndroidPlugin"):
                my_plugin = Java.get_singleton("MyAndroidPlugin")
```

```diff
- Syntax incorrect
! Uses Java instead of Engine to retrieve singleton

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _enter_tree():
        my_plugin = (
                get_editor_interface()
                .get_base_control()
                .get_tree()
                .get_root()
                .get_node_or_null("MyAndroidPlugin")
        )
```

```diff
+ Syntax correct

- Functionality incorrect
! Looks for editor plugin rather than Android one

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _enter_tree():
        my_plugin = singleton.get_value("MyAndroidPlugin") if singleton.has("MyAndroidPlugin") else null
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not look for singleton, instead looks for value in existing singleton reference

- Verbosity bad
! Assumes get_value method in singleton reference
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _enter_tree() -> void:
        if has_singleton("MyAndroidPlugin"):
                my_plugin = get_singleton("MyAndroidPlugin")
```

```diff
- Syntax incorrect
! Missing "Engine." before has_singleton
! Missing "Engine." before get_singleton

+ Functionality correct

+ Verbosity good
```

---

### Return a color based on the time elapsed since starting the game.

#### gpt-3.5-turbo

```gdscript
# Solution:

# Define a function to return the color based on time elapsed
func getColor(timeElapsed: float) -> Color:
    # Define the color ranges for different time intervals
    var colorRange1 = Color(0.0, 0.0, 1.0)  # Blue
    var colorRange2 = Color(0.0, 1.0, 1.0)  # Cyan
    var colorRange3 = Color(0.0, 1.0, 0.0)  # Green
    var colorRange4 = Color(1.0, 1.0, 0.0)  # Yellow
    var colorRange5 = Color(1.0, 0.0, 0.0)  # Red

    # Define the time intervals for each color range
    var timeInterval1 = 20.0  # Blue (0-20 seconds)
    var timeInterval2 = 40.0  # Cyan (21-40 seconds)
    var timeInterval3 = 60.0  # Green (41-60 seconds)
    var timeInterval4 = 80.0  # Yellow (61-80 seconds)
    var timeInterval5 = 100.0  # Red (81-100 seconds)

    # Determine the current color range based on the time elapsed
    if timeElapsed <= timeInterval1:
        return colorRange1
    elif timeElapsed <= timeInterval2:
        return colorRange2
    elif timeElapsed <= timeInterval3:
        return colorRange3
    elif timeElapsed <= timeInterval4:
        return colorRange4
    else:
        return colorRange5

# Call the getColor() function with the time elapsed since starting the game
var timeElapsed = 35.0  # Example value, replace with actual time elapsed
var color = getColor(timeElapsed)
print(color)  # Example output, replace with actual usage of the color returned by the function
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
extends Node

func _ready():
    # Get the time elapsed since the game started
    var time_elapsed = OS.get_ticks_msec()

    # Calculate the color values
    var r = (time_elapsed % 1000) / 1000.0
    var g = (time_elapsed % 2000) / 2000.0
    var b = (time_elapsed % 3000) / 3000.0

    # Create the color
    var color = Color(r, g, b)

    # Return the color
    print(color)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _get_color() -> Color:
        if Time.get_ticks_msec() - _start_ticks > 1000:
                return Color.RED
        elif Time.get_ticks_msec() - _start_ticks > 500:
                return Color.ORANGE
        elif Time.get_ticks_msec() - _start_ticks > 200:
                return Color.YELLOW
        else:
                return Color.GREEN
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func get_color():
        if elapsed_time < 1:
                return Color.GREEN
        elif elapsed_time < 2:
                return Color.YELLOW
        else:
                return Color.RED
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes elapsed time is already stored in elapsed_time variable
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _get_description() -> String:
        if time > 0.5:
                return "Green"
        elif time > 0.25:
                return "Yellow"
        else:
                return "Red"
```

```diff
+ Syntax correct

+ Functionality correct
! Returns string instead of color, which however does not clearly violate instructions

- Verbosity bad
! Assumes elapsed time is already referenced
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _get_description() -> String:
        return "Returns color based on time"
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not return color or check for time

- Verbosity bad
! Makes no attempt to implement required logic
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_time_color() -> Color:
        var t = Time.get_ticks_msec() - start_time
        if t < 1000:
                return Color.RED
        elif t < 2000:
                return Color.YELLOW
        elif t < 3000:
                return Color.GREEN
        elif t < 4000:
                return Color.BLUE
        elif t < 5000:
                return Color.MAGENTA
        elif t < 6000:
                return Color.CYAN
        elif t < 7000:
                return Color.DARK_RED
        elif t < 8000:
                return Color.DARK_YELLOW
        elif t < 9000:
                return Color.DARK_GREEN
        elif t < 10000:
                return Color.DARK_BLUE
        elif t < 11000:
                return Color.DARK_MAGENTA
        elif t < 12000:
                return Color.DARK_CYAN
        elif t < 13000:
                return Color.WHITE
        elif t < 14000:
                return Color.BLACK
        elif t < 15000:
                return Color.DARK_GRAY
        elif t < 16000:
                return Color.GRAY
        elif t < 17000:
                return Color.LIGHT_GRAY
        elif t < 18000:
                return Color.DARK_SLATE_BLUE
        elif t < 19000:
                return Color.SLATE_BLUE
        elif t < 20000:
                return Color.MEDIUM_SLATE_BLUE
        elif t < 21000:
                return Color.LIGHT_SLATE_BLUE
        elif t < 22000:
                return Color.DARK_SLATE_GRAY
        elif t < 23000:
                return Color.SLATE_GRAY
        elif t < 24000:
                return Color.MEDIUM_SLATE_GRAY
        ...
```

```diff
- Syntax incorrect
! DARK_YELLOW, LIGHT_SLATE_BLUE and MEDIUM_SLATE_GRAY color constants do not exist

+ Functionality correct

+ Verbosity good
```

---

### Call my_async_func and wait for it to finish, then return its returned value plus 20.

#### gpt-3.5-turbo

```gdscript
var result = yield(my_async_func())
return result + 20
```

```diff
- Syntax incorrect
! Uses yield instead of await

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
async func call_my_async_func():
    var result = await my_async_func()
    return result + 20
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func my_func() -> int:
        var v = await my_async_func()
        return v + 20
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func run() -> int:
        return (await my_async_func()) + 20
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func = await my_async_func()
        return function_return_value + 20
```

```diff
- Syntax incorrect
! Fails to implement func syntax

- Functionality incorrect
! Does not await function call

- Verbosity bad
! Does not initialize return value
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func = await my_async_func()
        return function_return_value + 20
```

```diff
- Syntax incorrect
! Fails to implement func syntax

- Functionality incorrect
! Does not await function call

- Verbosity bad
! Does not initialize return value
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func my_func():
        return await my_async_func() + 20
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Resize the input image to fit into a 265x265 square.

#### gpt-3.5-turbo

```gdscript
# Load the input image
var image = Image.new()
image.load("res://path/to/input_image.png")

# Get the original size of the image
var original_width = image.get_width()
var original_height = image.get_height()

# Calculate the new size of the image to fit into a 265x265 square
var new_width = 0
var new_height = 0
if original_width > original_height:
    new_width = 265
    new_height = int(round(original_height * (new_width / original_width)))
else:
    new_height = 265
    new_width = int(round(original_width * (new_height / original_height)))

# Resize the image
image.resize(new_width, new_height)

# Save the resized image to a new file
image.save("res://path/to/resized_image.png")
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
extends TextureRect

func _ready():
    var input_image = load("res://path/to/your/image.png")
    var resized_image = input_image.get_data()
    resized_image.resize(265, 265)
    var new_texture = ImageTexture.new()
    new_texture.create_from_image(resized_image)
    self.texture = new_texture
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func thumbnail(image):
        var new_image = Image.create(265, 265, false, Image.FORMAT_RGBA8)
        new_image.blit_rect(image, Rect2i(0, 0, 265, 265), Vector2i(0, 0))
        return new_image
```

```diff
+ Syntax correct

- Functionality incorrect
! Crops image instead of resizing

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func square_image(img: Image) -> Image:
        var new_size = Vector2i(265, 265)
        return img.resize(new_size)
```

```diff
- Syntax incorrect
! resize call takes integers, not Vector2

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func square_image(image: Image) -> Image:
        var size = min(image.get_width(), image.get_height())
        var new_size = Vector2i(size, size)
        var offset = (image.get_size() - new_size) / 2
        image.resize(new_size.x, new_size.y, Image.INTERPOLATE_TRILINEAR)
        image.crop(offset.x, offset.y, new_size.x, new_size.y)
        return image
```

```diff
- Syntax incorrect
!crop only takes two arguments

- Functionality incorrect
! Does not resize image into 256x256 square

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func square_image(image: Image) -> Image:
        var new_size = Vector2(265, 265)
        var image_size = Vector2(image.get_width(), image.get_height())
        var scale = min(new_size.x / image_size.x, new_size.y / image_size.y)
        var offset = (new_size - image_size * scale) / 2
        var new_image = Image.create(new_size.x, new_size.y, image.has_mipmaps(), image.get_format())
        new_image.blit_rect(image, Rect2(Vector2.ZERO, image_size), Vector2(offset.x, offset.y))
        return new_image
```

```diff
+ Syntax correct

- Functionality incorrect
! Crops image instead of fitting it

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _get_description() -> String:
        return "Resizes the input image to fit into a 265x265 square."
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not resize image
! Does not take input image

- Verbosity bad
! Makes no attempt to implement functionality
```

---

### Load an MP3 file from res://audio/test.mp3 and play back.

#### gpt-3.5-turbo

```gdscript
# Load the MP3 file
var audio = load("res://audio/test.mp3")

# Play back the MP3 file
AudioStreamPlayer.play(audio)
```

```diff
- Syntax incorrect
! AudioStreamPlayer has no static function called play
! Non-static play function does not take audio stream as input

+ Functionality correct

- Verbosity bad
! Makes no effort to assign audio stream
```

#### gpt-4

```gdscript
# First, add the following line to your project's AudioStreamPlayer node
# stream = load("res://audio/test.mp3")

# Then, add this code to your script to play the audio
func _ready():
    $AudioStreamPlayer.play()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():

        $Music/Music.stream = load("res://audio/test.mp3")
        $Music/Music.play()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _ready():
        stream = load("res://audio/test.mp3")
        play()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        stream = load("res://audio/test.mp3")
        play()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        stream = load("res://audio/test.mp3")
        play()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready():
        $Music.stream = load("res://audio/test.mp3")
        $Music.play()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Highlight each instance of "red" in the input RichTextLabels text in red.

#### gpt-3.5-turbo

```gdscript
# Assume the RichTextLabel node is named "label"

# Get the text from the label
var text = label.get_text()

# Find instances of "red" in the text and replace them with red-colored text
text = text.replace("red", "[color=#FF0000]red[/color]")

# Set the updated text back to the label
label.set_text(text)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Assuming you have a RichTextLabel node assigned to the variable 'rich_text_label'

# Get the text from the RichTextLabel
text = rich_text_label.text

# Split the text into words
words = text.split(" ")

# Clear the text from the RichTextLabel
rich_text_label.clear()

# Define the starting point for the loop
start = 0

# Iterate through the words
for word in words:
    if word == "red":
        # Append the word in red color
        rich_text_label.push_color(Color.red)
        rich_text_label.append_text(word)
        rich_text_label.pop()

        # Increment the starting point
        start += len(word)

    # Add the next word, and increment the starting point
    rich_text_label.append_text(text[start : start + len(word) + 1])
    start += len(word) + 1
```

```diff
- Syntax incorrect
! Color.red does not exist in 4x (should be Color.RED)
! Getting a substring via [start : end] does not work in GDScript

- Functionality incorrect
! Does not find instances of red that are not surrounded by spaces

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _on_gdunit_runner_start(rtf :RichTextLabel) -> void:
        rtf.clear()
        rtf.append_text("GdUnit Runner started!\n")
        var instances := rtf.find_all("red")
        for instance in instances:
                rtf.add_theme_color_override("default_color", Color.RED)
                rtf.add_theme_color_override("highlight_color", Color.RED)
                rtf.add_theme_color_override("current_color", Color.RED)
                instance.add_theme_color_override("default_color", Color.RED)
                instance.add_theme_color_override("highlight_color", Color.RED)
                instance.add_theme_color_override("current_color", Color.RED)
```

```diff
- Syntax incorrect
! find_all does not exist in RichTextLabel objects
! add_theme_color_override does not exist in RichTextLabel or String objects

- Functionality incorrect
! Does not edit the labels text at all

- Verbosity bad
! Hallucinates new text
! Does not handle string editing
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _color_highlight_regex(text: RichTextLabels, regex: RegEx):
        var color = Color.RED
        for result in regex.search_all(text.text):
                text.highlight_regex(result.get_string(), color)
```

```diff
- Syntax incorrect
! highlight_regex does not exist in RichTextLabel objects

+ Functionality correct

- Verbosity bad
! Does not handle string editing
! Makes no attempt to generate correct regex
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _highlight_bad_words(r_text_labels: Array[RichTextLabel]) -> void:
        for r_text_label in r_text_labels:
                r_text_label.text = _highlight_word(r_text_label.text, "red")
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Does not implement highlighting logic, assumes non-engine _highlight_word method
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _set_rich_text_label_colors(r: RichTextLabels):
        r.text = "[color=red]%s[/color]" % r.text
```

```diff
- Syntax incorrect
! RichTextLabels type does not exist

- Functionality incorrect
! Attempts to highlight entire text, not just instances of "red"

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready() -> void:
        for label in $RichTextLabels.get_children():
                label.text = label.text.replace("red", "[color=ff0000]red[/color]")
```

```diff
- Syntax incorrect
! Missing # in front of color code

- Functionality incorrect
! Does not modify RichTextLabel text, instead iterates through child nodes

+ Verbosity good
```

---

### Change the font size of the input Label to 35.

#### gpt-3.5-turbo

```gdscript
# Access the label node
var label = get_node("label")

# Set the font size to 35
label.set("custom_fonts/font/size", 35)
```

```diff
- Syntax incorrect
! custom_fonts/font/size does not exist in Label objects

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Assuming you have a Label node in your scene

extends Label

func _ready():
    var new_font = get_font("font")
    new_font.set_size(35)
    set_font("font", new_font)
```

```diff
- Syntax incorrect
! set_size does not exist in Font objects
! set_font does not exist in Label objects

+ Functionality correct

- Verbosity bad
! Assumes get_font function to retrieve font
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():
        $Label.set("theme_override_font_sizes/font_size", 35)
        pass # Replace with function body.
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Add useless pass
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _change_font_size(label : Label):
        label.add_theme_font_size_override("font_size", 35)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func make_label_bigger(label: Label):
        label.add_theme_font_size_override("font_size", 35)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func make_label_bigger(label: Label):
        label.add_theme_font_size_override("font_size", 35)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready():
        $Label.add_theme_font_size_override("font_size", 35)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Get JSON object from input byte array.

#### gpt-3.5-turbo

```gdscript
var json_str = input.bytes2string()
var json_obj = JSON.parse(json_str)
```

```diff
- Syntax incorrect
! bytes2string exists on no native byte representation
! JSON.parse is invalid in 4.x (instead, a JSON object should be created first)

+ Functionality correct

- Verbosity bad
! Makes no attempt to specify how to retrieve a string from bytes
```

#### gpt-4

```gdscript
var input_byte_array = # Your input byte array here
var json_string = input_byte_array.get_string_from_utf8()
var json_object = JSON.parse(json_string).result
```

```diff
- Syntax incorrect
! JSON.parse is invalid in 4.x (instead, a JSON object should be created first)
! JSON.parse returns an error and has no result property

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _on_get_baserow_llm_chat(result: int, response_code: int, headers: PackedStringArray, body: PackedByteArray):
        var json_object: JSON = JSON.new()
        json_object.parse(body.get_string_from_utf8())
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Assumes HttpRequest result handler, multiple unneeded parameters
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func get_json_object(bytes: PackedByteArray) -> Dictionary:
        var result := Dictionary()
        var offset := 0
        if bytes.size() < 4:
                return result
        var length := bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4:
                return result
        var dict := bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4:
                return result
        var checksum := bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4:
                return result
        var checksum2 := bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4:
                return result
        result.magic = bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4 + 1:
                return result
        result.id = bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4 + 1:
                return result
        result.meta = bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4 + 1 + 1:
                return result
        result.data = bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4 + 1 + 1:
                return result
        result.crc = bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4 + 1 + 1 + 4:
                return result
        result.size = bytes.decode_u32(offset)
        offset += 4
        if bytes.size() < length + 4 + 4 + 1 + 1 + 4:
                return result
```

```diff
- Syntax incorrect
! Missing final return statement

- Functionality incorrect
! Does not successfully parse the input bytes

- Verbosity bad
! Extremely verbose, not functional
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func unserialize_input(serialized: PackedByteArray) -> Dictionary:
        var json := JSON.new()
        json.parse(serialized.get_string_from_utf8())
        return json.get_data()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func unserialize_input(serialized: PackedByteArray) -> Dictionary:
        var json := JSON.new()
        json.parse(serialized.get_string_from_utf8())
        return json.get_data()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_json(bytes: PackedByteArray) -> Dictionary:
        return JSON.parse_string(bytes.get_string_from_utf8())
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Return string name of entry i in MY_ENUM.

#### gpt-3.5-turbo

```gdscript
enum MY_ENUM {
  ENTRY_ONE,
  ENTRY_TWO,
  ENTRY_THREE,
}

func get_enum_name(i: int) -> String:
  match i:
    0:
      return "ENTRY_ONE"
    1:
      return "ENTRY_TWO"
    2:
      return "ENTRY_THREE"
    _:
      return "Invalid entry number"
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Hardcodes returned string values
```

#### gpt-4

```gdscript
enum MY_ENUM {ENTRY_0, ENTRY_1, ENTRY_2, ENTRY_3}

func name_of_entry_i(i):
    return MY_ENUM.values()[i].name()
```

```diff
- Syntax incorrect
! name function does not exist on integer values

- Functionality incorrect
! Queries values, not keys

- Verbosity bad
! Hallucinates unneded name function
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func get_my_enum_string_name(i: int) -> String:
        return MY_ENUM.keys()[i]
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func get_name() -> String:
        return MY_ENUM[i]
```

```diff
- Syntax incorrect
! Can not index enums
! Defines String return value but does not return string

- Functionality incorrect
! Does not retrieve name of any enum entry

- Verbosity bad
! Makes no attempt at retrieving string name
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func get_name(i:int) -> String:
        return MY_ENUM.keys()[i]
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func get_name(i:int) -> String:
        return MY_ENUM.keys()[i]
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_entry_name(i: int) -> String:
        return MY_ENUM.keys()[i]
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Check if current window orientation is landscape or portrait and emit orientation_changed signal accordingly.

#### gpt-3.5-turbo

```gdscript
extends Node

signal orientation_changed(orientation)

func _ready():
    # Check initial orientation
    var orientation = OS.get_screen_orientation()
    emit_signal("orientation_changed", orientation)

    # Connect to orientation change signal
    OS.set_window_fullscreen(true) # Required for orientation change detection
    OS.connect("screen_resized", self, "_on_screen_resized")

func _on_screen_resized():
    # Check new orientation and emit signal if changed
    var new_orientation = OS.get_screen_orientation()
    if new_orientation != get_signal_strength("orientation_changed"):
        emit_signal("orientation_changed", new_orientation)
```

```diff
- Syntax incorrect
! OS.get_screen_orientation does not exist (should be DisplayServer.screen_get_orientation)
! OS.set_window_fullscreen does not exist (should be Window.set_mode)
! Uses 3.x syntax to connect signals
! OS has no signal named screen_resized
! get_signal_strength matches no engine function

+ Functionality correct

- Verbosity bad
! Assumes get_signal_strength function that takes signal name as input
```

#### gpt-4

```gdscript
extends Node

signal orientation_changed(orientation)

func _ready():
    OS.window_size = Vector2(1280, 720)
    OS.connect("screen_resized", self, "_on_screen_resized")
    _check_orientation()

func _check_orientation():
    var orientation = "landscape" if OS.window_size.x > OS.window_size.y else "portrait"
    emit_signal("orientation_changed", orientation)

func _on_screen_resized():
    _check_orientation()
```

```diff
- Syntax incorrect
! OS.window_size does not exist (should use Window.size)
! OS has no signal named screen_resized

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _update_orientation() -> void:
        if DisplayServer.window_get_orientation() == DisplayServer.ORIENTATION_LANDSCAPE:
                orientation_changed.emit(DisplayServer.ORIENTATION_LANDSCAPE)
        elif DisplayServer.window_get_orientation() == DisplayServer.ORIENTATION_PORTRAIT:
                orientation_changed.emit(DisplayServer.ORIENTATION_PORTRAIT)
```

```diff
- Syntax incorrect
! DisplayServer.window_get_orientation does not exist (should be DisplayServer.screen_get_orientation)
! DisplayServer.ORIENTATION_X does not exist (should be DisplayServer.SCREEN_X)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _on_orientation_changed() -> void:
        if DisplayServer.window_get_orientation() == DisplayServer.WINDOW_ORIENTATION_LANDSCAPE:
                orientation_changed.emit("landscape")
        else:
                orientation_changed.emit("portrait")
```

```diff
- Syntax incorrect
! DisplayServer.window_get_orientation does not exist (should be DisplayServer.screen_get_orientation)
! DisplayServer.ORIENTATION_X does not exist (should be DisplayServer.SCREEN_X)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _on_window_resized() -> void:
        if DisplayServer.window_get_size().x > DisplayServer.window_get_size().y:
                if orientation!= ORIENTATION.LANDSCAPE:
                        orientation = ORIENTATION.LANDSCAPE
                        orientation_changed.emit(orientation)
        else:
                if orientation!= ORIENTATION.PORTRAIT:
                        orientation = ORIENTATION.PORTRAIT
                        orientation_changed.emit(orientation)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
! Uses custom ORIENTATION.LANDSCAPE/PORTRAIT enum instead of DisplayServer.SCREEN_LANDSCAPE/SCREEN_PORTRAIT. Not optimal, but valid
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _on_window_resized() -> void:
        if DisplayServer.window_get_size().x > DisplayServer.window_get_size().y:
                if orientation!= ORIENTATION_LANDSCAPE:
                        orientation = ORIENTATION_LANDSCAPE
                        orientation_changed.emit(orientation)
        else:
                if orientation!= ORIENTATION_PORTRAIT:
                        orientation = ORIENTATION_PORTRAIT
                        orientation_changed.emit(orientation)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
! Uses custom ORIENTATION_LANDSCAPE/ORIENTATION_PORTRAIT constants instead of DisplayServer.SCREEN_LANDSCAPE/SCREEN_PORTRAIT. Not optimal, but valid
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready() -> void:
        if DisplayServer.window_get_size().x > DisplayServer.window_get_size().y:
                orientation_changed.emit(ORIENTATION.LANDSCAPE)
        else:
                orientation_changed.emit(ORIENTATION.PORTRAIT)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
! Uses custom ORIENTATION.LANDSCAPE/PORTRAIT enum instead of DisplayServer.SCREEN_LANDSCAPE/SCREEN_PORTRAIT. Not optimal, but valid
```

---

### Execute a thread that resizes an input array of images to 1024x1024, then emit a the resized images via signal.

#### gpt-3.5-turbo

```gdscript
# Define a function that will be executed in the thread
func resize_images_thread(images: Array):
    var resized_images = []

    # Loop through each image and resize it
    for image in images:
        var resized_image = image.resize(1024, 1024)
        resized_images.append(resized_image)

    # Emit a signal with the resized images
    emit_signal("resized_images_signal", resized_images)

# Call the function in a new thread
var thread = Thread.new()
thread.start(resize_images_thread, [input_images])
```

```diff
- Syntax incorrect
! Parameters of Callable passed to Thread.start must be bound, not passed as separate parameter
! resize function does not return an Image object

- Functionality incorrect
! [input_images] produces a nested array

+ Verbosity good
```

#### gpt-4

```gdscript
# Here's an example of how you could write a class that resizes an array of images using a thread and emits a signal with the resized images.

extends Node

signal resized_images(resized_array)

var _thread = Thread.new()
var _images_to_resize = []
var _resized_images = []

func _ready():
    pass

func resize_images(images: Array) -> void:
    _images_to_resize = images
    _thread.start(self, "_resize_images_thread")

func _resize_images_thread(_void):
    for image in _images_to_resize:
        var resized_image = Image.new()
        resized_image.create_from_image(image)
        resized_image.resize(1024, 1024, Image.INTERPOLATE_BILINEAR)
        _resized_images.append(resized_image)
    call_deferred("emit_signal", "resized_images", _resized_images)

func _exit_tree():
    _thread.wait_to_finish()
```

```diff
- Syntax incorrect
! create_from_image does not exist on Image instance
! Thread.start expects Callable, not object, function name

- Functionality incorrect
! Thread function takes parameter, but none are bound/passed

+ Verbosity good

```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _on_resize_to_1024_x_1024_pressed():
        var images : Array = %Output.get_children()
        var thread = Thread.new()
        thread.start(
                func():
                        for image in images:
                                image.resize(1024, 1024)
                                image.save_png("./output/%s.png" % image.get_name())
                                image.queue_free()
        )
        self.resized.emit(images)
```

```diff
- Syntax incorrect
! Node children can not be images
! queue_free can not be called on Image objects

- Functionality incorrect
! Does not take input image array

- Verbosity bad
! Hallucinates node-specific logic
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func resize_images(images: Array):
        resize_thread.start(
                func():
                        var results = []
                        for image in images:
                                var new_image = image.get_image()
                                new_image.resize(1024, 1024)
                                results.append(new_image)
                        resize_finished.emit(results)
        )
```

```diff
+ Syntax correct

- Functionality incorrect
! Takes input array of ImageTextures, not Images

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _threaded_image_resize(images: Array) -> void:
        for image in images:
                image.resize(1024, 1024)

        emit_signal("resized_images", images)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not execute a thread

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _threaded_resize(a: Array[Image]) -> void:
        for i in range(a.size()):
                a[i].resize(1024, 1024)
        emit_signal("resized", a)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not execute a thread

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func resize_images(images: Array[Image]) -> void:
        var thread := Thread.new()
        thread.start(func():
                for image in images:
                        image.resize(1024, 1024)
        )
        thread.wait_to_finish()
        resized_images.emit(images)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Print "godot-dodo" backwards.

#### gpt-3.5-turbo

```gdscript
var str = "godot-dodo"
var reversedStr = ""

for i in range(str.length() - 1, -1, -1):
    reversedStr += str[i]

print(reversedStr)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
print("godot-dodo"[::-1])
```

```diff
- Syntax incorrect
! Python-like [::x] syntax does not work in GDScript

+ Functionality correct

- Verbosity bad
! Makes no attempt at implementing string reversal logic
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _ready():
        print("godot-dodo".reverse())
```

```diff
- Syntax incorrect
! reverse does not exist on String object

+ Functionality correct

- Verbosity bad
! Makes no attempt at implementing string reversal logic
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _run():
        print("godot-dodo")
        print("godot-dodo")
        print("godot-dodo")
        print("godot-dodo")
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not reverse string

- Verbosity bad
! Makes no attempt at implementing string reversal logic
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func backwards():
        print("godot-dodo")
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not revert string

- Verbosity bad
! Makes no attempt to implement logic
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func backwards():
        print("godot-dodo")
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not revert string

- Verbosity bad
! Makes no attempt to implement logic
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func test():
        print("godot-dodo".backwards())
```

```diff
- Syntax incorrect
! backwards method does not exist on String object

+ Functionality correct

+ Verbosity good
```

---

### Create a sorting function that sorts by the "dollar_value" property of each object if it exists, otherwise by the "euro_value" property.

#### gpt-3.5-turbo

```gdscript
func sortObjects(objects: Array) -> Array:
    var sortedObjects = objects.sort_custom(lambda(x): x.dollar_value if "dollar_value" in x else x.euro_value)
    return sortedObjects
```

```diff
- Syntax incorrect
! lambda logic is not functional in GDScript

+ Functionality correct

- Verbosity bad
! Makes no attempt at implementing GDScript sorting logic
```

#### gpt-4

```gdscript
func sort_by_currency(arr):
    return arr.sort_custom(self, "compare_currency")

func compare_currency(a, b):
    if "dollar_value" in a:
        a_value = a.dollar_value
    else:
        a_value = a.euro_value

    if "dollar_value" in b:
        b_value = b.dollar_value
    else:
        b_value = b.euro_value

    if a_value < b_value:
        return -1
    elif a_value > b_value:
        return 1
    else:
        return 0
```

```diff
- Syntax incorrect
! Returns sort_custom, which is void
! Does not pass Callable to sort_custom

+ Functionality correct

- Verbosity bad
! Does not declare clearly local variables
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func (a, b):
                if a.dollar_value < b.dollar_value:
                        return true
                elif a.dollar_value > b.dollar_value:
                        return false
                else:
                        return a.euro_value < b.euro_value
        )
```

```diff
+ Syntax correct
! If used as a sorting function for sort_custom

- Functionality incorrect
! Does not check if keys exist

- Verbosity bad
! Unnecessary explicit boolean return statements
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func sort_by_value():
        var sort_by_dollar = func(a, b):
                if get_property_value(a, "dollar_value") != null and get_property_value(b, "dollar_value") != null:
                        if get_property_value(a, "dollar_value") < get_property_value(b, "dollar_value"):
                                return true
                        else:
                                return false
                else:
                        if get_property_value(a, "euro_value") != null and get_property_value(b, "euro_value") != null:
                                if get_property_value(a, "euro_value") < get_property_value(b, "euro_value"):
                                        return true
                                else:
                                        return false
                        else:
                                if a < b:
                                        return true
                                else:
                                        return false
        var sort_by_euro = sort_by_dollar
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Duplicates sorting function unnecessarily
! Assumes get_property_value non-engine function to handle key checks
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func sort_by_value(a, b) -> bool:
        if a.has("dollar_value"):
                if b.has("dollar_value"):
                        return a.dollar_value < b.dollar_value
                else:
                        return a.dollar_value < b.euro_value
        else:
                if b.has("dollar_value"):
                        return a.euro_value < b.dollar_value
                else:
                        return a.euro_value < b.euro_value
```

```diff
+ Syntax correct

- Functionality incorrect
! May compare dollar to euro values, instead of dollar to dollar and euro to euro

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func sort_by_value(a, b) -> bool:
        if a.has("dollar_value"):
                if b.has("dollar_value"):
                        return a.dollar_value < b.dollar_value
                else:
                        return a.dollar_value < b.euro_value
        else:
                if b.has("dollar_value"):
                        return a.euro_value < b.dollar_value
                else:
                        return a.euro_value < b.euro_value
```

```diff
+ Syntax correct

- Functionality incorrect
! May compare dollar to euro values, instead of dollar to dollar and euro to euro

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func sort(a, b):
        if a.has("dollar_value"):
                return a.dollar_value < b.dollar_value
        else:
                return a.euro_value < b.euro_value
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not check for valid key in b

+ Verbosity good
```

---

### Call my_func if Shift + C was pressed by the user.

#### gpt-3.5-turbo

```gdscript
func _input(event):
    if event is InputEventKey:
        if event.scancode == KEY_C and event.mod.control:
            my_func()
```

```diff
- Syntax incorrect
! scancode does not exist in 4.x (should be keycode)
! mod does not exist on InputEventKey

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
func _input(event):
    if event.is_action_pressed("shift+c"):
        my_func()
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Makes not attempt to check for pressed keys, assumes special input event
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _input(event: InputEvent) -> void:
        if event.is_pressed() and event.as_text() == "Shift+C":
                my_func()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _input(event: InputEvent) -> void:
        if event is InputEventKey and event.is_pressed():
                if event.as_text() == "Shift+C":
                        my_func.call()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _input(event):
        if event is InputEventKey and event.pressed:
                match event.as_text():
                        "Shift+C":
                                my_func()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _unhandled_input(event: InputEvent) -> void:
        if event is InputEventKey and event.is_pressed():
                match event.as_text():
                        "Shift+C":
                                my_func()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _input(event):
        if event is InputEventKey and event.pressed:
                if event.shift_pressed and event.keycode == KEY_C:
                        my_func()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Print a warning message if the current FPS are below 30, and include the current FPS in the message.

#### gpt-3.5-turbo

```gdscript
var current_fps = Engine.get_frames_per_second()

if current_fps < 30:
    print("Warning: Current FPS is below 30. Current FPS is " + str(current_fps))
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# Fetch the current FPS
current_fps = Engine.get_frames_per_second()

# Check if the current FPS is below 30
if current_fps < 30:
    # Print the warning message with the current FPS
    print("Warning! The current FPS is below 30. Current FPS: %s" % current_fps)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _process(delta):
        if Engine.get_frames_per_second() < 30:
                print("FPS: " + str(Engine.get_frames_per_second()))
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func show_warning():
        if Performance.get_monitor(Performance.TIME_FPS) < 30:
                print("Warning: FPS are below 30. Consider increasing the frame limit in the editor.")
                print("Current FPS: ", Performance.get_monitor(Performance.TIME_FPS))
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _process(_delta: float) -> void:
        var fps := Engine.get_frames_per_second()
        if fps < 30:
                push_warning("Low FPS: %d" % fps)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _process(_delta: float) -> void:
        var fps := Performance.get_monitor(Performance.TIME_FPS)
        if fps < 30:
                push_warning("Low FPS: %d" % fps)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _process(_delta: float) -> void:
        if Engine.get_frames_per_second() < 30:
                push_warning("FPS is below 30: %s" % Engine.get_frames_per_second())
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### When the size of this Control node has changed, calculate the area of the new size and print it.

#### gpt-3.5-turbo

```gdscript
# Solution:
func _on_Control_resized():
    var area = size.x * size.y
    print("The area of the new size is:", area)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
# In your Control node's script:

func _ready():
    connect("size_changed", self, "_on_size_changed")

func _on_size_changed():
    var size = get_size()
    var area = size.x * size.y
    print(area)
```

```diff
- Syntax incorrect
! Uses 3.x syntax for signal connection
! size_changed signal does not exist in Control nodes

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _on_size_changed():
        var area = self.get_rect().size
        print(area)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not calculate area

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _on_size_changed():
        print(size)
        area = size.x * size.y
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not print area

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _on_Control_resized():
        var new_area = size.x * size.y
        print(new_area)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _on_Control_resized():
        var new_size = $Control.size
        var area = new_size.x * new_size.y
        print(area)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _notification(what):
        if what == NOTIFICATION_SIZE_CHANGED:
                var area = Rect2(Vector2.ZERO, size)
                print(area)
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not calculate area

+ Verbosity good
```

---

### Create a new environment with fog enabled, and add it to the scene.

#### gpt-3.5-turbo

```gdscript
# Create a new Environment node
var environment = Environment.new()

# Enable fog
environment.fog_enabled = true

# Add the environment to the scene
get_tree().get_root().add_child(environment)
```

```diff
- Syntax incorrect
! add_child does not exist on Window objects
! Can not add Environment object as child

- Functionality incorrect
! Does not attempt to add to current scene

- Verbosity bad
! Does not create WorldEnvironment necessary to add to scene
```

#### gpt-4

```gdscript
extends Node

func _ready():
    var environment = Environment.new()
    environment.background_mode = Environment.BG_MODE_COLOR
    environment.background_color = Color(0.2, 0.2, 0.2)
    environment.fog_enabled = true
    environment.fog_color = Color(0.1, 0.1, 0.1)
    environment.fog_begin = 10.0
    environment.fog_end = 100.0
    environment.fog_height_enabled = true
    environment.fog_height_min = 0.0
    environment.fog_height_max = 50.0

    var world_env = WorldEnvironment.new()
    world_env.environment = environment
    add_child(world_env)
```

```diff
- Syntax incorrect
! Environment.BG_MODE_COLOR does not exist in 4x (should be Environment.BG_COLOR)
! fog_X properties do no exist in Environment object (except fog_enabled)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func benchmark_fog_enabled():
        var rv := Environment.new()
        rv.fog_enabled = true
        return rv
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not attempt to add to current scene

- Verbosity bad
! Does not create WorldEnvironment necessary to add to scene
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func test_environment():
        var env = Environment.new()
        env.environment = Environment.ENV_FOG_ENABLED
        add_child(env)
```

```diff
- Syntax incorrect
! environment does not exist on Environment objects
! Environment.ENV_FOG_ENABLED does not exist
! Environment is not a node type that can be added to tree

+ Functionality correct

- Verbosity bad
! Does not create WorldEnvironment necessary to add to scene
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _ready():
        environment = Environment.new()
        environment.fog_enabled = true
        add_child(environment)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Does not create WorldEnvironment necessary to add to scene
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _ready():
        environment = Environment.new()
        environment.fog_enabled = true
        add_child(environment)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Does not create WorldEnvironment necessary to add to scene
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready():
        environment = Environment.new()
        environment.fog_enabled = true
        add_child(environment)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Does not create WorldEnvironment necessary to add to scene
```

---

### Push the rigidbody rigid_box upwards if the user presses the space key.

#### gpt-3.5-turbo

```gdscript
func _process(delta):
    if Input.is_action_pressed("ui_accept"):
        rigid_box.apply_impulse(Vector3.UP * 10, Vector3.ZERO)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
extends RigidBody

func _physics_process(delta):
    if Input.is_action_just_pressed("ui_select"):
        self.apply_impulse(Vector3(), Vector3(0, 10, 0))
```

```diff
- Syntax incorrect
! RigidBody does not exist in 4.x (should be RigidBody3D)

- Functionality incorrect
! Does not apply force to rigid_box
! Does not apply upwards force

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _physics_process(delta):
        if Input.is_key_pressed(KEY_SPACE):
                rigidbody.rigid_box.push_up()
```

```diff
- Syntax incorrect
! push_up does not exist on RigidBody3D objects

- Functionality incorrect
! Does not correctly reference rigid_box

- Verbosity bad
! Makes no attempt to specify any force
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _physics_process(delta):
        if Input.is_key_pressed(KEY_SPACE):
                rigidbody.push(rigid_box, Vector3(0,1,0))
```

```diff
- Syntax incorrect
! push does not exist on RigidBody3D objects

- Functionality incorrect
! Does not correctly reference rigid_box

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _input(event):
        if event is InputEventKey and event.pressed and event.keycode == KEY_SPACE:
                rigid_box.push_rigidbody(Vector3.UP)
```

```diff
- Syntax incorrect
! push_rigidbody does not exist on RigidBody3D objects

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _input(event):
        if event is InputEventKey and event.pressed and event.keycode == KEY_SPACE:
                rigid_box.push_rigidbody(Vector3.UP)
```

```diff
- Syntax incorrect
! push_rigidbody does not exist on RigidBody3D objects

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _input(event):
        if event is InputEventKey and event.pressed and event.keycode == KEY_SPACE:
                rigid_box.push_up()
```

```diff
- Syntax incorrect
! push_up does not exist on RigidBody3D objects

+ Functionality correct

+ Verbosity good
```

---

### Import the my_model.glb file from the user directory and add it to the scene.

#### gpt-3.5-turbo

```gdscript
# Assuming the my_model.glb file is located in the user directory
var my_model = load("res://user/my_model.glb")

# Create a new Spatial node and add the model as a child
var my_model_node = Spatial.new()
my_model_node.add_child(my_model)

# Add the new node to the scene tree
get_tree().get_root().add_child(my_model_node)
```

```diff
- Syntax incorrect
! Spatial does not exist in 4.x (should be Node3D)
! add_child does not exist on Window object

- Functionality incorrect
! Does not instantiate loaded model
! Does not add model to current scene

+ Verbosity good
```

#### gpt-4

```gdscript
extends Node

func _ready():
    var my_model = load("user://my_model.glb")
    var model_instance = my_model.instance()
    add_child(model_instance)
```

```diff
- Syntax incorrect
! instance does not exist in 4.x (should be instantiate)

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _import_my_model():
        var my_model = load("user://my_model.glb")
        add_model(my_model)
```

```diff
+ Syntax correct

+ Functionality correct

- Verbosity bad
! Makes no attempt to implement logic to add to scene, assumes non-engine add_model function
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _ready():
        import_my_model.glb = load("user://my_model.glb")
        add_child(import_my_model)
```

```diff
- Syntax incorrect
! glb property does not exist on any engine object

- Functionality incorrect
! Does not instantiate loaded model

- Verbosity bad
! Assumes import_my_model object that is not necessary for required logic
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _on_my_pc_m_pressed():
        var my_model = Importer.import("user://my_model.glb")
        add_child(my_model)
```

```diff
- Syntax incorrect
! Importer class does not exist, should be load

- Functionality incorrect
! Does not instantiate loaded model

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _on_my_model_pressed():
        add_my_model("user://my_model.glb")
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not reasonably implement any logic

- Verbosity bad
! Assumes non-engine method implementing loading logic
! Assumes non-engine method implementing tree logic
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func _ready() -> void:
        import_glb("user://my_model.glb")
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not reasonably implement any logic

- Verbosity bad
! Assumes non-engine method implementing loading logic
! Assumes non-engine method implementing tree logic
```

---

### Get the distance between the current node and the input node in global space.

#### gpt-3.5-turbo

```gdscript
# Assuming 'input_node' is an instance of Node2D or Spatial
# and 'current_node' is the current node instance

var distance = current_node.global_transform.origin.distance_to(input_node.global_transform.origin)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### gpt-4

```gdscript
func get_distance(input_node):
    return global_transform.origin.distance_to(input_node.global_transform.origin)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func distance_to(from: Node2D) -> float:
        return from.global_position.distance_to(global_position)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func distance_to(node: Node2D) -> float:
        return global_position.distance_to(node.global_position)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func distance_to(to: Node3D) -> float:
        return global_position.distance_to(to.global_position)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func distance_to(to: Node3D) -> float:
        return global_position.distance_to(to.global_position)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func get_distance_to(node: Node2D) -> float:
        return global_position.distance_to(node.global_position)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Split the input string into an array of lines, then remove any line that is shorter than 10 characters.

#### gpt-3.5-turbo

```gdscript
var input_string = "This is a sample string.\nIt has multiple lines.\nSome lines are shorter than others.\nThis line is longer than ten characters.\nAnother long line goes here.";

var lines = input_string.split("\n")

for i in range(lines.size()):
    if lines[i].length() < 10:
        lines.remove(i)
        i -= 1

print(lines)
```

```diff
- Syntax incorrect
! remove does not exist in PackedStringArray (should be remove_at)

- Functionality incorrect
! For-loop fails after item has been removed due to out-of-range index

+ Verbosity good
```

#### gpt-4

```gdscript
func remove_short_lines(input: String) -> Array:
    var input_lines = input.split("\n")
    var long_lines = []
    for line in input_lines:
        if len(line) >= 10:
            long_lines.append(line)
    return long_lines
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func _import(source_file: String, save_path: String, options: Dictionary, platform_variants: Array[String], gen_files: Array[String]) -> int:
        var file = FileAccess.open(source_file, FileAccess.READ)
        var text = file.get_as_text()

        var lines = text.split("\n")

        for line in lines:
                if line.length() < 10:
                        continue
```

```diff
- Syntax incorrect
! Missing return statements

- Functionality incorrect
! Does not handle input string
! Does not assemble or return array

- Verbosity bad
! Multiple unneeded parameters
! Unneded file access
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _remove_short_lines(text: String) -> String:
        var lines = text.split("\n")
        return lines.filter(func(line: String) -> bool: return line.length() > 10)
```

```diff
- Syntax incorrect
! filter does not exist in PackedStringArray (should create Array first)
! Array return value does not match specified String type

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func clean_lyrics(lyrics : String) -> String:
        var cleaned := PackedStringArray()
        for line in lyrics.split("\n"):
                if line.length() >= 10:
                        cleaned.append(line)
        return "\n".join(cleaned)
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func remove_useless_lines(lyrics : String) -> String:
        var lines := lyrics.split("\n")
        for line in lines.size():
                if lines[line].length() < 10:
                        lines.remove_at(line)
        return "\n".join(PackedStringArray(lines))
```

```diff
+ Syntax correct

- Functionality incorrect
! For-loop fails after item has been removed due to out-of-range index

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func clean_text(text: String) -> String:
        var lines = text.split("\n")
        for line in lines:
                if line.length() < 10:
                        lines.erase(line)
        return "\n".join(lines)
```

```diff
- Syntax incorrect
! erase does not exist in PackedStringArray type

+ Functionality correct

+ Verbosity good
```

---

### Enable SDFGI for the input environment.

#### gpt-3.5-turbo

```gdscript
Sorry, as an AI language model, I don't have access to the specific environment or context you are referring to. Can you please provide more details or context so that I can give you a more accurate response?
```

```diff
- Syntax incorrect
! No code provided

- Functionality incorrect
! No code provided

- Verbosity bad
! No code provided
```

#### gpt-4

```gdscript
# Assuming `env` is the input environment
env.gi_probe_enable = true
env.gi_probe_sdfgi_enable = true
```

```diff
- Syntax incorrect
! gi_probe_enable does not exist on Environment or WorldEnvironment objects
! gi_probe_sdfgi_enable does not exist on Environment or WorldEnvironment objects

- Functionality incorrect
! Attempts to modify gi-probe related properties

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func sdfgi_enable(environment):
        environment.sdfgi_enable()
```

```diff
- Syntax incorrect
! sdfgi_enable does not exist on Environment or WorldEnvironment objects

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _init_env(env: Environment) -> void:
        env.sdfgi_enabled = true
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _get_description() -> String:
        return "Enable SDFGI for the input environment"
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not enable SDFGI

- Verbosity bad
! Makes no attempt to implement logic
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _on_cb_global_illumination_toggled(button_pressed):
        if button_pressed:
                environment.sdfgi_enabled = true
```

```diff
+ Syntax correct

- Functionality incorrect
! Does not take input environment param

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func enable_sdfgi(env: Environment) -> void:
        env.sdfgi_enabled = true
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

---

### Exit the game.

#### gpt-3.5-turbo

```gdscript
# Import the OS class
var OS = Engine.get_singleton().get_OS()

# Call the quit() function to exit the game
OS.quit()
```

```diff
- Syntax incorrect
! Attempts to assign to reserved name OS
! get_singleton expects one string parameter
! get_OS does not exist on any engine object
! quit does not exist on OS object

+ Functionality correct

- Verbosity bad
! Attempts convoluted, nonsensical way of retrieving OS object
```

#### gpt-4

```gdscript
get_tree().quit()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_7b

```gdscript
func exit() -> void:
        get_tree().quit()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_llama_13b

```gdscript
func _on_quit_button_pressed():
        get_tree().quit()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_3ep

```gdscript
func _on_exit_pressed():
        get_tree().quit()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_2ep

```gdscript
func _on_exit_button_pressed() -> void:
        get_tree().quit()
```

```diff
+ Syntax correct

+ Functionality correct

+ Verbosity good
```

#### godot_dodo_4x_60k_starcoder_15b_1ep

```gdscript
func exit() -> void:
```

```diff
- Syntax incorrect
! No indented block after function definition

- Functionality incorrect
! Does not exit game

- Verbosity bad
! Makes no attempt to implement logic.
```
