#!/usr/bin/env python3

import panflute as pf


def handle_code_block(elem):
    try:
        language = elem.classes[0]
    except IndexError:
        language = 'python'

    begin_raw = '\\begin{{{}code}}'.format(language)
    end_raw = '\\end{{{}code}}'.format(language)

    begin_block = pf.RawBlock(begin_raw, format='tex')
    content = pf.RawBlock(elem.text, format='tex')
    end_block = pf.RawBlock(end_raw, format='tex')

    return [begin_block, content, end_block]


def handle_solution(elem):
    '''make a solution'''
    begin_solution = pf.RawBlock(r'\begin{solution}', format='tex')
    end_solution = pf.RawBlock(r'\end{solution}', format='tex')
    return [begin_solution, elem, end_solution]


def action(elem, doc):
    '''check which type the element has; act accordingly'''
    if isinstance(elem, pf.CodeBlock):
        return handle_code_block(elem)
    elif isinstance(elem, pf.Div) and 'solution' in elem.classes:
        return handle_solution(elem)


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
