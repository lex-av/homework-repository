# -*- coding: utf-8 -*-


from ..pack_task3.module_task3 import make_filter

sample_data_1 = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]


def test_make_filter_sample_data():
    assert make_filter(name='Bill').apply(sample_data_1) == [{'name': 'Bill',
                                                              'last_name': 'Gilbert',
                                                              'occupation': 'was here',
                                                              'type': 'person'}]


def test_make_filter_sample_data_key_missing():
    assert make_filter(namee='Bill').apply(sample_data_1) == []
