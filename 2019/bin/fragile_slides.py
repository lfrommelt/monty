#!/usr/bin/env python3

import panflute as pf


def action(elem, doc):
    if isinstance(elem, pf.Header):
        elem.classes.append('fragile')
        return elem


def finalize(doc):
    ref_section = pf.Header(pf.Str('References'), level=1)
    ref_section.classes.append('unnumbered')
    ref_sub_section = pf.Header(pf.Str('References'), level=2)
    doc.content.append(ref_section)
    doc.content.append(ref_sub_section)


def main(doc=None):
    return pf.run_filter(action, finalize=finalize, doc=doc)


if __name__ == '__main__':
    main()
