
import processing

############################################################
####### ADD THE DIRECTORY FOR THE FILES TO SAVE HERE #######
############################################################
############### IT MUST END WITH A SLASH (/) ###############
############################################################

SAVE_DIR = "C:/Users/iwatk/OneDrive/Desktop/"

############################################################

layers = [
    ("Overview_bbox", 1517642.0733140623, 1532244.8076437297, 7517785.772636008, 7532388.512338427),
    ("Overview_bbox_with_margin", 1517142, 1532744, 7517285, 7532888)
]

for layer in layers:
    name = layer[0]
    north, south, east, west = layer[1:]

    epsg3857_string = str(north) + "," + str(south) + "," + str(east) + "," + str(west) + " [EPSG:3857]"
    file_path = SAVE_DIR + name + ".tif"

    processing.run(
        "native:rasterize",
        {
            "EXTENT": epsg3857_string,
            "EXTENT_BUFFER": 0,
            "TILE_SIZE": 64,
            "MAP_UNITS_PER_PIXEL": 1,
            "MAKE_BACKGROUND_TRANSPARENT": False,
            "MAP_THEME": None,
            "LAYERS": None,
            "OUTPUT": file_path,
        },
)
