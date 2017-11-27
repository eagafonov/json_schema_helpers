
# Simple types
type_string = dict(type="string")
type_null = dict(type="null")
type_integer = dict(type="integer")
type_number = dict(type="number")
type_object = dict(type="object")
type_list = dict(type="array")  # Python clashed with JavaScript :-)
type_boolean = dict(type="boolean")

# Simple type or null
type_string_or_null = dict(oneOf=[type_string, type_null])
type_integer_or_null = dict(oneOf=[type_integer, type_null])
type_number_or_null = dict(oneOf=[type_number, type_null])
type_object_or_null = dict(oneOf=[type_object, type_null])
type_list_or_null = dict(oneOf=[type_list, type_null])
type_boolean_or_null = dict(oneOf=[type_boolean, type_null])

list_of_strings = dict(type="array", items=[{"type": "string"}])
list_of_numbers = dict(type="array", items=[type_number])


# Complex
def list_of(ref, minItems=None, maxItems=None, exactItems=None):
    d = dict(type="array", items=[{"$ref": "#/definitions/%s" % ref}])

    if exactItems is not None:
        minItems = exactItems
        maxItems = exactItems

    if minItems is not None:
        d['minItems'] = minItems

    if maxItems is not None:
        d['maxItems'] = maxItems

    return d


def ref(ref_id):
    '''
        Reference to type
    '''
    return {"$ref": "#/definitions/%s" % ref_id}


def schema(schema_options, **kwargs):
    s = {
        "$schema": "http://json-schema.org/draft-04/schema#"
    }

    s.update(schema_options)
    s.update(kwargs)

    return s
