import datetime


class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.'''
        self._find_note(note_id).tags = tags

    def search(self, filter):
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if
                note.match(filter)]


# Store the next available id for all new notes
last_id = 0


class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''

    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.'''
        return filter in self.memo or filter in self.tags

# >>> from example3 import Note, Notebook
# >>> n = Notebook()
# >>> n.new_note('hello world')
# >>> n.new_note('hello again')
# >>> n.notes
# [<example3.Note object at 0x7f4fafde3dc0>, <example3.Note object at 0x7f4fafde3cd0>]
# >>> n.notes[0]
# <example3.Note object at 0x7f4fafde3dc0>
# >>> n.notes[0].id
# 1
# >>> n.notes[1].id
# 2
# >>> n.notes[0].memo
# 'hello world'
# >>> n.notes[1].memo
# 'hello again'
# >>> n.search("hello")
# [<example3.Note object at 0x7f4fafde3dc0>, <example3.Note object at 0x7f4fafde3cd0>]
# >>> n.search("world")
# [<example3.Note object at 0x7f4fafde3dc0>]
# >>> n.modify_memo(1, "hi world")
# >>> n.notes[0].memo
# 'hi world'
# >>>
