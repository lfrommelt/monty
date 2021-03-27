#!/usr/bin/env python3

import sys
import subprocess
import panflute as pf
import textwrap


def _execute(to_execute, wd=None):
    '''
    executes python code

    Args:
        to_execute: (str) python code or python script name
    '''
    command = [sys.executable or 'python3'] + to_execute
    print('Command', file=sys.stderr)
    print(command, file=sys.stderr)
    return subprocess.run(command, stdout=subprocess.PIPE,
                          cwd=wd, stderr=subprocess.STDOUT, universal_newlines=True).stdout
#    return subprocess.run(command, stdout=subprocess.PIPE,
#                          stderr=subprocess.PIPE, universal_newlines=True).stdout

# stderr=subprocess.STDOUT,


def execute_code(code, wd=None):
    '''
    used if it is pure python code (str)
    '''
    return _execute(['-c', code], wd)


def execute_script(script, wd=None):
    '''
    used if you pass .py file
    '''
    return _execute([script], wd)


def execute_code_block(elem, doc):
    '''
    makes a block out of the executed code
    '''
    code = elem.text.strip()
    script = elem.attributes.get("script")
    wd = elem.attributes.get("wd")
    linelength = int(elem.attributes.get("linelength", 51))
    if script:
        output = execute_script(script, wd)
        with open(wd+"/"+script) as python_script:
            code = python_script.read()
            elem.text = code
    else:
        output = execute_code(code, wd)
    output = '\n'.join([
        '\n'.join(textwrap.wrap(
            line, linelength, break_long_words=False, replace_whitespace=False))
        for line in output.splitlines()])
    output_element = pf.CodeBlock(output, classes=['output'])
    # output_element = pf.CodeBlock(output, classes=['python'])

    return output_element


def handle_execution(elem, doc):
    '''make a execution block
    checks if elem is of type CodeBlock
    and if it additionally has "exec"
    '''
    if isinstance(elem, pf.CodeBlock) and 'exec' in elem.classes:
        begin_exec = pf.RawBlock(r'\begin{pyexec}', format='tex')
        exec_output = execute_code_block(elem, doc)
        end_exec = pf.RawBlock(r'\end{pyexec}', format='tex')

        if 'hide' in elem.classes:
            return [begin_exec, exec_output, end_exec]
        else:
            return [elem, begin_exec, exec_output, end_exec]
    elif isinstance(elem, pf.CodeBlock) and 'script' in elem.attributes:
        script = elem.attributes.get("script")
        wd = elem.attributes.get("wd")
        with open(wd+"/"+script) as python_script:
            code = python_script.read()
            elem.text = code
    # else:
    #    print(elem, file=sys.stderr)


def main(doc=None):
    return pf.run_filter(handle_execution, doc=doc)


if __name__ == '__main__':
    main()
