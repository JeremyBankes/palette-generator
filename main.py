import colorsys

# Configuration

HUE_COUNT = 6
SATURATION_COUNT = 4
BRIGHTNESS_COUNT = 4

HUE_START = 0
HUE_STEP = 360 / HUE_COUNT
SATURATION_START = 0.0
SATURATION_STEP = 0.30
BRIGHTNESS_START = 0
BRIGHTNESS_STEP = 1 / (BRIGHTNESS_COUNT - 1)

OUTPUT_FILE_PATH = "palette.txt"
OUTPUT_ARGB = True

# Logic

unique_colors = []

hue_values = [
    HUE_START + hue_index * HUE_STEP / 360 for hue_index in range(0, HUE_COUNT)
]

saturation_values = [
    SATURATION_START + saturation_index * SATURATION_STEP for saturation_index in range(0, SATURATION_COUNT)
]

brightness_values = [
    BRIGHTNESS_START + brightness_index * BRIGHTNESS_STEP for brightness_index in range(0, BRIGHTNESS_COUNT)
]

with open(OUTPUT_FILE_PATH, "w") as output_file:
    for hue in hue_values:
        for saturation in saturation_values:
            for brightness in brightness_values:
                normalized_rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
                [red, green, blue] = [hex(int(value * 255))[2:].zfill(2) for value in normalized_rgb]
                hex_string = f"{red}{green}{blue}".upper()
                if OUTPUT_ARGB:
                    hex_string = "FF" + hex_string
                if hex_string not in unique_colors:
                    unique_colors.append(hex_string)
                    output_file.write(hex_string)
                    output_file.write("\n")

display_saturation_values = ", ".join(["{:.0f}%".format(saturation * 100) for saturation in saturation_values])
display_brightness_values = ", ".join(["{:.0f}%".format(brightness * 100) for brightness in brightness_values])
print(f"Generated {len(unique_colors)} unique colors in \"{OUTPUT_FILE_PATH}\"!")
print(f"\tUsed {len(hue_values)} hues: {", ".join(["{:.0f}".format(hue * 360) for hue in hue_values])}")
print(f"\tUsed {len(saturation_values)} saturation values: {display_saturation_values}")
print(f"\tUsed {len(brightness_values)} brightness values: {display_brightness_values}")
