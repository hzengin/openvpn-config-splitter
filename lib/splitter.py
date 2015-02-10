import lib.utilities as utilities
import lib.constants as constants
import lib.exceptions as exceptions
import re

def split(source, paths):
    # Use default ones for not given paths
    paths = utilities.initialize_paths(paths)
    output = {}
    for key, matcher in constants.parserMatchers.items():
        match = re.search(matcher, source)
        if match is not None:
            output[key] = match.group(1).strip()

    # Check if we matched nothing
    if not output:
        raise exceptions.InvalidConfigFile(source)

    # Check if we can find key-dir
    direction = re.search(constants.keyDirMatcher, source).group(1)
    if not direction:
        direction = -1

    # create the text to insert
    text = utilities.create_text_to_insert(paths, direction)

    # merge text and source
    new_text = utilities.merge_with_source(source, text)
    output["configOutput"] = new_text
    return output

