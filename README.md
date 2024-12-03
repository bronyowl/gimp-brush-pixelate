# Brush Pixelate GIMP Plugin

A simple GIMP plugin that creates a dynamic pixelation effect where your brush strokes are applied, treamlining the process of mosaic censorship.

## Installation Guide

### Windows
1. Download the `auto_pixelate.py` file
2. Locate your GIMP plugins folder:
   ```
   C:\Users\[YourUsername]\AppData\Roaming\GIMP\2.10\plug-ins\
   ```
3. Copy the `brush_pixelate.py` file into this folder
4. Restart GIMP

### Linux
1. Download the `brush_pixelate.py` file
2. Copy to your GIMP plugins directory:
   ```bash
   cp brush_pixelate.py ~/.config/GIMP/2.10/plug-ins/
   ```
3. Make the script executable:
   ```bash
   chmod +x ~/.config/GIMP/2.10/plug-ins/brush_pixelate.py
   ```
4. Restart GIMP

### macOS
1. Download the `brush_pixelate.py` file
2. Copy to your GIMP plugins folder:
   ```bash
   cp brush_pixelate.py ~/Library/Application\ Support/GIMP/2.10/plug-ins/
   ```
3. Make the script executable:
   ```bash
   chmod +x ~/Library/Application\ Support/GIMP/2.10/plug-ins/brush_pixelate.py
   ```
4. Restart GIMP

## Troubleshooting Installation

- Ensure Python support is enabled in GIMP
- Verify the file permissions are correct
- Check GIMP's Python console for error messages
- Make sure the file extension is `.py`

## Features

- **Interactive Pixelation**: Pixelate only where you paint
- **Non-destructive Editing**: Works on a separate layer with a mask
- **Instant Setup**: Automatically configures brush and layer settings
- **Reversible Effects**: Easy to modify or remove using the layer mask

## How It Works

The plugin creates a setup where:
1. A duplicate layer is created with a pixelation effect
2. A black mask hides the pixelation initially
3. Your brush strokes with white reveal the pixelated areas
4. Areas you don't brush remain unchanged

## Usage Instructions

1. Open your image in GIMP
2. Select `Filters > Custom > Auto Pixelate`
3. Once activated:
   - Use the brush tool (already configured)
   - Paint over areas you want to pixelate
   - The pixelation appears only where you brush
4. Adjust the mask with black/white brushes to fine-tune the effect


## Default Parameters
(you can adjust them in the auto_pixelate.py file)
- Default pixelation block size: 10 pixels
- Brush preset: "2. Hardness 075"
- Brush spacing: 10% 


## Setting Up a Keyboard Shortcut

To assign a keyboard shortcut to the Auto Pixelate plugin:

1. Open GIMP and navigate to `Edit > Keyboard Shortcuts`

2. In the Keyboard Shortcuts Dialog:
   - Use the search field to find "Auto Pixelate"
   - Click on the action line for Auto Pixelate
   - When "New accelerator..." appears, press your desired key combination(`Shift+Alt+M` is recommended to avoid confliction)
   - Click "Save" to apply immediately

## Author

Bronyowl (2024)
