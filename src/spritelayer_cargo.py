from gestalt_graphics.pipelines import GenerateSpritelayerCargos

from spritelayer_cargos import registered_spritelayer_cargos


class CargoBase(object):
    """ Base class for (spritelayer) cargos """

    # sets of cargo sprites of specific length and appearance
    # each set corresponds to a spritesheet which will be generated by the graphics processor
    # each set is used for a specific group of cargo labels or classes
    # each set may have one or more spriterows
    # spriterows are chosen randomly when vehicles load new cargo
    # rows are composed by the graphics processor, and may include variations for
    # - combinations of cargo lengths
    # - combinations of cargo types
    # - cargo colours
    # !!! cargos are going to need 'base sets' to allow double stack, cropped  for well cars etc
    # !!! the consist needs to encode the set type to fetch the right spritesets
    # !!! base sets will also have to be encoded in gestalts here, unless they're done by (sets * gestalts) combinatorially?
    def __init__(self, **kwargs):
        self.platform_type = kwargs.get("platform_type", None)
        self.pipeline = GenerateSpritelayerCargos()
        # configure gestalt_graphics in the subclass
        self.gestalt_graphics = None

    @property
    def all_platform_types_with_floor_heights(self):
        return "implement in subclass"

    @property
    def all_platform_types(self):
        return "implement in subclass"

    @property
    def floor_height_for_platform_type(self):
        return "implement in subclass"

    @property
    def id(self):
        return "implement in subclass"
