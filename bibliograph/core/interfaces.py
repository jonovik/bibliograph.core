from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary

# XXX as long as we don't have a propper translation messagefactory
_ = unicode

###############################################################################

class IBibliographyExport(Interface):
    """ Marker interface for a container with
        exportable bibliography elements.
    """

###############################################################################

class IBibrenderable(Interface):
    """ An object is renderable as a bibliography """

    title = schema.TextLine(
        title=_('Title'),
        description=_('The title of the entry'),
        required = True,
        )

    publication_type = schema.Choice(
        title=_('Publication type'),
        description=_('A publication type as found in the bibtex definition'),
        required=True,
        vocabulary=SimpleVocabulary.fromItems([
            (_("Article"), 'article'),
            (_("Book"), 'book'),
            (_("Booklet"), 'booklet'),
            (_("Conference"), 'conference'),
            (_("Inbook"), 'inbook'),
            (_("Incollection"), 'incollection'),
            (_("Inproceedings"), 'inproceenings'),
            (_("Manual"), 'manual'),
            (_("Masterthesis"), 'masterthesis'),
            (_("Misc"), 'misc'),
            (_("Phdthesis"), 'phdthesis'),
            (_("Proceedings"), 'proceedings'),
            (_("Techeport"), 'techreport'),
            (_("Unpublished"), 'unpublished'),
            ])
        )

    editor_flag = schema.Bool(
        title=_('Editor'),
        description=_('Marker for interpretation of author field as editor'),
        required = False,
        )

    publication_year = schema.Int(
        title=_('Year of publication'),
        required=True,
        )

    abstract = schema.Text(
        title=_('Abstract'),
        description=_('A short summary of the document'),
        required = True,
        )

    subject = schema.List(
        title=_('Subject'),
        description=_('A list of tags(subjects) of the document'),
        required = True,
        )

    note = schema.Text(
        title=_('Note'),
        description=_('Some additional notes'),
        required = False,
        )

    annote = schema.Text(
        title=_('Annotation'),
        description=_('Some annotations'),
        required = False,
        )

    source_fields = schema.List(
        title=_('Source fields'),
        value_type=schema.TextLine(),
        required=False,
        )

    def Authors(*args, **kw):
        """ Get a list-like object containing the authors.
            The object must know about rendering a formatted list
            of authors by beeing called.
        """

    def getURL():
        """ URL of publication """

# EOF
