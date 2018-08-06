#! /usr/bin/env python
#
############################################################################
#
from gimpfu import *

PROC_NAME = 'python-fu-cut_column'


def cut_column(layer, shift, merge):
    image = layer.image
    x, y = layer.offsets
    image.add_layer(pdb.gimp_layer_copy(layer, True), -1)
    new_layer = image.active_layer
    if shift > 0:
        new_layer.resize(image.width // 2 - shift - x, new_layer.height, 0, 0)
        new_layer.set_offsets(x + shift, y)
    else:
        new_layer.resize(new_layer.width - image.width // 2 - shift - x, new_layer.height,
                         -(image.width // 2 - x - shift), 0)
        new_layer.set_offsets(image.width // 2, y)
    if merge:
        image.merge_visible_layers(CLIP_TO_IMAGE)


register(
    PROC_NAME,
    N_("Cut <shift> sized column left/right from center"),
    """Copy selected layer.
    Cut column with <shift> width (if positive - left from image center, if negative - right from image center).
    And shift it to fill the gap""",
    "Vladimir Kushnir",
    "Vladimir Kushnir",
    "2018",
    N_("_Cut Column..."),
    "RGB*, GRAY*",
    [
        (PF_LAYER, "layer", "Layer", None),
        (PF_INT16, "shift", "Shift in pixels", 118),
        (PF_TOGGLE, "merge", "Merge visible layers", False)

    ],
    [],
    cut_column,
    menu="<Image>/Wallpapers/Transform",
    domain=("gimp20-python", gimp.locale_directory))

main()
