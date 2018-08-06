#! /usr/bin/env python
#
############################################################################
#
from gimpfu import *

PROC_NAME = 'python-fu-align_by_source'


def align_by_source(src, tgt, scale):
    sx, sy = src.offsets
    if scale:
        tgt.scale(src.width, src.height, 0)
    tgt.set_offsets(sx, sy)


register(
    PROC_NAME,
    N_("Align two layers"),
    """Place target layer in same offset as source.
    Scale if requested.""",
    "Vladimir Kushnir",
    "Vladimir Kushnir",
    "2018",
    N_("_Align Layer..."),
    "RGB*, GRAY*",
    [
        (PF_LAYER, "src", "Source Layer", None),
        (PF_LAYER, "tgt", "Target Layer", None),
        (PF_TOGGLE, "scale", "Scale", False)
    ],
    [],
    align_by_source,
    menu="<Image>/Wallpapers/Transform",
    domain=("gimp20-python", gimp.locale_directory))


main()
