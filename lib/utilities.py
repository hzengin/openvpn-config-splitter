import lib.constants as constants
import re


def initialize_paths(paths):  # checks given paths and merges with defaults if not given by hand
    for filename in constants.defaultFileNames:
        if (filename not in paths) or (filename in paths and not paths[filename]):
            paths[filename] = constants.defaultFileNames[filename]
    return paths


def write_to_files(paths, parts):  # writes given parts to given paths
    paths = initialize_paths(paths)
    for part_key in parts:
        file = open(paths[part_key], "w")  # opening with mode "w" means any existing data will be lost
        file.write(parts[part_key])
        file.close()


def merge_with_source(source, text):
    return re.sub(constants.insertLocationMatcher, "\n".join([constants.insertLocationMatcher, text]), source)


def file_exist(filename):  # check if file exist
    import os
    return os.path.isfile(filename)


def create_text_to_insert(paths, tls_key_dir=-1):
    parts_to_insert = ["### ---Added By hzengin's python openvpn config. file splitter ###"]
    for path_key in paths:
        if path_key == "tlsAuth" and tls_key_dir != -1:
            parts_to_insert.append(create_tls_line(paths[path_key], str(tls_key_dir)))
        elif path_key in constants.textToInsertRefs:
            line = create_text_to_insert_line(path_key, paths[path_key])
            parts_to_insert.append(line)
    return "\n".join(parts_to_insert)


def create_text_to_insert_line(path_key, path):
    return " ".join([constants.textToInsertRefs[path_key], path]).strip()


def create_tls_line(tls_path, tls_key_dir):
    return " ".join([constants.textToInsertRefs["tlsAuth"], tls_path, tls_key_dir]).strip()