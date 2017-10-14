from pathlib import Path
import json

class Entry:
    def __init__(self, title, date, tags):
        self.date = date
        self.title = title
        self.tags = tags
    def export_as_json(self):
        return '{\n  "date": "{}", \n  "title": "{}", \n  "tags": "{}"\n}'.format(self.date, self.title, self.tags)

def generate_entry_from_file(filename):
    date, title, tags = "", "", []

    # generate 'date' from the first 10 characters of the filename (e.g "'2017-10-14'_name-of-the-entry.md")
    # get the 'title' from the first header ('# the title')
    # extract the 'tags' from the embedded json ('<!-- { "tags": ["",""]} -->')

    return Entry(title, date, tags)

def parse_entries_in_path(path):
    ls_entry_objects = []
    # for each .md file in 'directory_name'/:
        # ls_entry_objects.append(generate_entry_from_file(filename))
    return ls_entry_objects

def build_manifest():
    ls_entries = parse_entries_in_path('entries/')
    # json_string_to_export = json.dumps(ls_entries)
    # create 'blog.json' file with 'json_string_to_export'

build_manifest()
