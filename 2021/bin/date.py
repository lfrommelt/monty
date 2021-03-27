#!/usr/bin/env python3

import panflute as pf


def action(elem, doc):
    pass


def finalize(doc):
    doc.metadata['year'], doc.metadata['month'], doc.metadata['day'] = doc.get_metadata()['date'].split('-')


def main(doc=None):
    return pf.run_filter(action, finalize=finalize, doc=doc)


if __name__ == '__main__':
    main()
