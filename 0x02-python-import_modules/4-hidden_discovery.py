#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    # Get all attributes (names) from the module hidden_4
    attributes = dir(hidden_4)

    # Iterate over attributes & print non-dunder
    # / (not starting with '__') names

    for attribute in sorted(attributes):
        if not attribute.startswith("__"):
            print(attribute)
