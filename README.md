## Simple JSON format image interpreter created with a use of Python pygame library.

### Usage
To run type
```
python3 js_image path_to_json_data [-o image_save_path]
```
Once json image window opens program gives you an access to following shortcuts:

- ``` s ``` to save a file in program's running location 

- ``` q ``` to quit a program



### Example JSON  File
```
 {
    "Figures": [
        {"type": "point", "x": 1, "y": 0},
        {"type": "polygon", "points": [[2,5], [3,14], [5,18], [11,18], [3,39]], "color": "blue"},
        {"type": "rectangle", "x": 100, "y": 50, "width": 200, "height": 50},
        {"type": "square", "x": 150, "y": 100, "size": 80, "color": "(255,255,255)"},
        {"type": "square", "x": 800, "y": 600, "radius": 40, "color": "#abcdef"}
    ],
    "Screen": {"width": 800, "height": 600, "bg_color": "black", "fg_color": "red"},
    "Palette": {"red": "#ff0000", "blue": "#0000ff", "black": "#000000"}
}
```
