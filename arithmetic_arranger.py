def get_result_problem(str_problem=''):
    if ('+' in str_problem) is ('-' in str_problem):
        return 'Error: Operator must be \'+\' or \'-\'.'
    normalize_problem = str_problem.replace(' ', '')
    operands = normalize_problem.split('+')
    if len(operands) == 2:
        if len(operands[0]) > 4 or len(operands[1]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if operands[0].isdigit() and operands[1].isdigit():
            return {
                'operand1': int(operands[0]),
                'operand2': int(operands[1]),
                'operator': '+',
                'result': int(operands[0]) + int(operands[1])
            }
        else:
            return 'Error: Numbers must only contain digits.'
    else:
        operands = normalize_problem.split('-')
        if len(operands[0]) > 4 or len(operands[1]) > 4:
            raise SystemExit('Error: Numbers cannot be more than four digits.')
        if operands[0].isdigit() and operands[1].isdigit():
            return {
                'operand1': int(operands[0]),
                'operand2': int(operands[1]),
                'operator': '-',
                'result': int(operands[0]) - int(operands[1])
            }
        else:
            return 'Error: Numbers must only contain digits.'


def build_arrange_string(result_problems, displayed):
    spaces_4 = '    '
    arrange_problems, operands1, operands2, results, dashes = '', '', '', '', ''
    for result in result_problems:
        spaces = 2 + max(len(str(result['operand1'])), len(str(result['operand2'])))
        operands1 += f"{str(result['operand1']).rjust(spaces)}" + spaces_4
        operands2 += str(result['operator']) + f"{str(result['operand2']).rjust(spaces - 1)}" + spaces_4
        dashes += f"{('-' * spaces).rjust(spaces)}" + spaces_4
        results += f"{str(result['result']).rjust(spaces)}" + spaces_4

    arrange_problems += operands1[:-4] + '\n' + operands2[:-4] + '\n' + dashes[:-4]
    if displayed:
        arrange_problems += '\n' + results[:-4]

    return arrange_problems


def arithmetic_arranger(problems, displayed=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    result_problems = []
    for problem in problems:
        result_problem = get_result_problem(problem)
        if 'Error' in result_problem:
            return result_problem
        else:
            result_problems.append(result_problem)
    arranged_problems = build_arrange_string(result_problems, displayed)

    return arranged_problems
