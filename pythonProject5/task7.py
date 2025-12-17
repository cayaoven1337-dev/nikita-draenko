# task7.py

ignore = ["duplex", "alias", "Current configuration"]

def ignore_command(command, ignore):
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename):
    result = {}
    current_key = None

    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()

            if not line or line.startswith("!") or ignore_command(line, ignore):
                continue

            if not line.startswith(" "):
                current_key = line
                result[current_key] = []
            else:
                result[current_key].append(line.strip())

    return result


print(convert_config_to_dict("config_sw1.txt"))