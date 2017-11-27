# Example with https://github.com/eagafonov/json_schema_helpers

import json_schema_helpers as jsh

heading_loc_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "heading_loc object",
    "type": "object",
    "additionalProperties": False, # properties must contains a complete list of supported languages
    "properties": {
        "en": jsh.type_string,
        "cz": jsh.type_string,
        "de": jsh.type_string,
        # Add more language properties as `"lng": jsh.ref_id("lang")`
    },
}

# validate something

import json
import jsonschema
import pprint

object2validate = '''{
        "de": "German",
        "en": "English",
        "cz": "Czech"
}'''


object2validate = json.loads(object2validate)

pprint.pprint(object2validate)

jsonschema.validate(object2validate, heading_loc_schema)
