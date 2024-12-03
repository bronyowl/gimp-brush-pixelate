#!/usr/bin/env python

from gimpfu import *

def auto_pixelate(image, drawable):
    # Duplicate the layer
    new_layer = drawable.copy()
    image.add_layer(new_layer, 0)
    
    # Apply pixelize filter
    pdb.plug_in_pixelize(image, new_layer, 10)
    
    # Create black mask (ADD_BLACK_MASK = 1)
    mask = new_layer.create_mask(ADD_BLACK_MASK)
    new_layer.add_mask(mask)
    
    # Set up for brushing
    pdb.gimp_context_set_foreground((255, 255, 255))
    pdb.gimp_context_set_brush("2. Hardness 075")
    pdb.gimp_context_set_brush_spacing(0.1)   # 10% spacing
    # Make the mask active
    image.active_layer = new_layer
    new_layer.mask_bounds
    
    # Refresh the display
    gimp.displays_flush()

register(
    "python-fu-auto-pixelate",
    "Automate pixelate mask setup",
    "Creates a pixelated layer with mask ready for brushing",
    "Bronyowl", "Bronyowl", "2024",
    "<Image>/Filters/Custom/Auto Pixelate",
    "*",
    [],
    [],
    auto_pixelate)

main()