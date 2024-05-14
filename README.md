# Palette Generator

Generate a palette based on hue, saturation, and brightness values.

Configuration Options

* Number of Values Section
  * `HUE_COUNT` The number of hues to use during generation.
  * `SATURATION_COUNT` The number of saturation values to use during generation.
  * `BRIGHTNESS_COUNT` The name of brightness values to use during generation.

* Value Usage Section
  * `HUE_START` The first hue value.
  * `HUE_STEP` The step between hue values.
    * Note: Hue values are interpreted on a scale from 0 to 360
  * `SATURATION_START` The first saturation value.
  * `SATURATION_STEP` The step between saturation values.
    * Note: Saturation values are interpreted on a scale from 0 to 1
  * `BRIGHTNESS_START` The first brightness values.
  * `BRIGHTNESS_STEP` The step between brightness values.
    * Note: Brightness values are interpreted on a scale from 0 to 1
  * Note: Any hue saturation or brightness configuration must stay within the defined scale
    to get expected results. `START + STEP * (COUNT - 1) <  SCALE`

* Output Section
  * `OUTPUT_FILE_PATH` The path to the output file. Ensure this directory exists.
  * `OUTPUT_FILE_PATH` `True` to output in a ARGB. `False` for RGB
    * Note: Output values are in hexadecimal. I.E. `FF00FF` For magenta.

### Execution
```commandline
py main.py
```

### Command Line Output
*Based on configuration*
```
Generated 6 unique colors in "palette.txt"!
	Used 3 hues: 0, 120, 240
	Used 1 saturation values: 50%
	Used 2 brightness values: 25%, 50%
```

### File Output
*palette.txt*
```
FF3F1F1F
FF7F3F3F
FF1F3F1F
FF3F7F3F
FF1F1F3F
FF3F3F7F
```