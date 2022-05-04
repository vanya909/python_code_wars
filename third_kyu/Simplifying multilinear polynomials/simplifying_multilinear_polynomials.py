import re
from collections import namedtuple


variable_regex = r'(-?\d*)([^\d\W]+)'
Variable = namedtuple('Variable', 'constant literal')

def get_variable_tuple(variable):
    """Returns norm looking named tuple, e.g. ('-', 'xy') -> Variable(-1, 'xy')"""

    if variable[0]:
        if variable[0] != '-':
            constant = int(variable[0])
        else:
            constant = -1
    else:
        constant = 1

    literal = ''.join(sorted(variable[1]))

    return Variable(constant, literal)

def simplify(poly):
    # Get all operands using regular expressions
    all_operands = [get_variable_tuple(variable) for variable in re.findall(variable_regex, poly)]
    all_operands_simplified = []
    
    # Sum all identical operands and add them to list
    for operand in all_operands:
        literal = operand.literal

        if literal in [x.literal for x in all_operands_simplified]:
            continue

        constant = sum([variable.constant for variable in all_operands if variable.literal == literal])

        if constant == 0:
            continue
        elif constant == 1:
            all_operands_simplified.append(Variable('', literal))
        elif constant == -1:
            all_operands_simplified.append(Variable('-', literal))
        else:
            all_operands_simplified.append(Variable(constant, literal))

    # Sort list and join it to get a final result
    all_operands_simplified.sort(key=lambda x: (len(x.literal), x.literal))
    result = '+'.join([f'{x.constant}{x.literal}' for x in all_operands_simplified])
    result = result.replace('+-', '-')

    return result
