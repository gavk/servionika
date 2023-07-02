#!/usr/bin/env python

import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', nargs=1, required=True)
    parser.add_argument('--val', nargs=1, required=False)
    parser.add_argument('--storage', nargs=1, required=False)
    args = parser.parse_args().__dict__

    storage_filename = args['storage']
    if not storage_filename:
        storage_filename = 'storage.data'

    key = args['key'][0]
    result = {
        'storage_filename': storage_filename,
        'key': key,
    }
    values = args['val']
    if values:
        val = values[0]
    else:
        val = None
    result.update({'val': val})
    return result


def get_new_storage():
    storage = {}
    return storage


def load_storage(storage_filename='storage.data'):
    try:
        with open(storage_filename, 'r') as fp:
            storage = json.load(fp)
    except FileNotFoundError:
        storage = get_new_storage()
    return storage


def save_storage(storage_filename='storage.data', storage={}):
    with open(storage_filename, 'w') as fp:
        fp.write(json.dumps(storage, indent=4))


def add_data(storage={}, key='key', value='val'):
    if key in storage.keys():
        values = storage.get(key)
        values.append(value)
        update = {key: values}
    else:
        update = {key: [value]}
    storage.update(update)


def get_data(storage={}, key='key'):
    if key in storage.keys():
        return storage.get(key)
    return None


def main():
    args = parse_args()
    storage_filename = args['storage_filename']
    storage = load_storage(storage_filename)
    key = args['key']
    value = args['val']
    if value:
        add_data(storage, key, value)
        save_storage(storage_filename, storage)
        return
    values = get_data(storage, key)
    if values:
        print(','.join(values))
        return
    print(None)


if '__main__' == __name__:
    main()
