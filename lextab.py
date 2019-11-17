# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('DATATYPE', 'DIVISION', 'ELSE', 'ENDLINE', 'EQUAL', 'FOR', 'ID', 'IF', 'LBRACE', 'LBRACKET', 'MINUS', 'MULTIPLY', 'NUMBER', 'PLUS', 'RBRACE', 'RBRACKET', 'VARIABLE', 'WHILE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_NUMBER>\\d+)|(?P<t_IF>if)|(?P<t_VARIABLE>\\$\\w*\\b)|(?P<t_DATATYPE>(let))|(?P<t_RBRACE> \\))|(?P<t_MULTIPLY>\\*)|(?P<t_PLUS>\\+)|(?P<t_LBRACE>\\()|(?P<t_RBRACKET>\\})|(?P<t_LBRACKET>\\{)|(?P<t_EQUAL>=)|(?P<t_DIVISION>/)|(?P<t_MINUS>-)|(?P<t_ENDLINE>;)', [None, ('t_NUMBER', 'NUMBER'), ('t_IF', 'IF'), ('t_VARIABLE', 'VARIABLE'), (None, 'DATATYPE'), None, (None, 'RBRACE'), (None, 'MULTIPLY'), (None, 'PLUS'), (None, 'LBRACE'), (None, 'RBRACKET'), (None, 'LBRACKET'), (None, 'EQUAL'), (None, 'DIVISION'), (None, 'MINUS'), (None, 'ENDLINE')])]}
_lexstateignore = {'INITIAL': ' \t\n'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
