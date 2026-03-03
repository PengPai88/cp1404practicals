HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

while True:
    colour_name = input("Enter colour name (blank to exit): ").lower()
    if not colour_name:
        break
    try:
        print(f"{colour_name} is {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")