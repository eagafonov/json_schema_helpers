from json_schema_helpers import ref, list_of, type_null


import json_schema_helpers


class TestSimpleTypes:
    def test_simple_types(self):
        types = ['string', 'null', 'integer', 'object', 'list', 'boolean']

        for t in types:
            assert hasattr(json_schema_helpers, 'type_%s' % t)
            f = getattr(json_schema_helpers, 'type_%s' % t)
            assert dict(type=t) == f

    def test_simple_types_or_null(self):
        types = ['string', 'integer', 'object', 'list', 'boolean']

        for t in types:
            assert hasattr(json_schema_helpers, 'type_%s_or_null' % t)
            f = getattr(json_schema_helpers, 'type_%s_or_null' % t)
            expected = dict(oneOf=[dict(type=t), type_null])

            assert expected == f


class TestRef:
    def test_01(self):
        assert {'$ref': '#/definitions/some_time'} == ref('some_time')

class TestTypeList:
    def test_list_of(self):
        assert list_of('some_time') == dict(type='array',
                                            items=[{'$ref': '#/definitions/some_time'}])

        assert dict(type='array', items=[ref('some_time')]) == list_of('some_time')

    def test_list_of_exact_items(self):
        assert list_of('some_time', exactItems=10) == dict(type='array',
                                                           items=[ref('some_time')],
                                                           maxItems=10,
                                                           minItems=10)

    def test_list_of_min_items_only(self):
        assert list_of('some_time', minItems=10) == dict(type='array',
                                                         items=[ref('some_time')],
                                                         minItems=10)

    def test_list_of_max_items_only(self):
        assert list_of('some_time', maxItems=10) == dict(type='array',
                                                         items=[ref('some_time')],
                                                         maxItems=10)
