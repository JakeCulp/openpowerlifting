#!/usr/bin/env python3
# vim: set ts=8 sts=4 et sw=4 tw=99:
#
# Helper library for automatically generating usernames from the Name column.
# This logic is needed independently for testing and for compilation.
#

# UTF-8 => lookalike ASCII substitutions.
SubstitutionMap = {
    'á': 'a', 'ä': 'a', 'å': 'a', 'ą': 'a', 'ã': 'a', 'à': 'a', 'â': 'a', 'ā': 'a',
    'æ': 'ae',
    'ć': 'c', 'ç': 'c', 'č': 'c',
    'đ': 'd', 'ð': 'd', 'ď': 'd',
    'é': 'e', 'ê': 'e', 'ë': 'e', 'è': 'e', 'ě': 'e', 'ę': 'e', 'ē': 'e',
    'ğ': 'g', 'ģ': 'g',
    'î': 'i', 'í': 'i', 'ï': 'i', 'ì': 'i', 'ї': 'i', 'ī': 'i',
    'ķ': 'k',
    'ľ': 'l', 'ĺ': 'l',
    'ñ': 'n', 'ń': 'n', 'ň': 'n', 'ņ': 'n',
    'ø': 'o', 'ô': 'o', 'ö': 'o', 'ó': 'o', 'ő': 'o', 'õ': 'o', 'ò': 'o',
    'ř': 'r',
    'ß': 'ss',
    'š': 's', 'ś': 's', 'ș': 's', 'ş': 's',
    'ț': 't', 'ť': 't',
    'þ': 'th',
    'ü': 'u', 'ů': 'u', 'ú': 'u', 'ù': 'u', 'ū': 'u', 'ű': 'u',
    'ý': 'y',
    'ł': 'w',
    'ž': 'z', 'ż': 'z', 'ź': 'z',
}


def sub_from(m, c):
    try:
        return m[c]
    except KeyError:
        return c


def get_username(name):
    # Although the input string is UTF-8, the username must be ASCII.
    # Instead of dropping non-ASCII characters, just make look-alike
    # substitutions.
    name_lower = name.lower()
    name_ascii = map(lambda c: sub_from(SubstitutionMap, c), name_lower)
    name_alnum = filter(str.isalnum, name_ascii)
    ret = ''.join(name_alnum)
    return ret
