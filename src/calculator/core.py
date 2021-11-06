from typing import Union

import requests
import sympy
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, \
    implicit_multiplication_application, convert_xor, convert_equals_signs

from . import complement

transformations = standard_transformations + (convert_xor, implicit_multiplication_application, convert_equals_signs)

local_dict = {"e": sympy.E, "ℯ": sympy.E, "i": sympy.I, "ⅈ": sympy.I, "π": sympy.pi, "θ": sympy.Heaviside,
              "φ": sympy.GoldenRatio, "ϕ": sympy.GoldenRatio, "⋅": "*"}

replace_dict = {"⋅": "*", "√": "sqrt "}


def parse(expression: str):
    for old, new in replace_dict.items():
        expression = expression.replace(old, new)

    return parse_expr(expression, transformations=transformations, local_dict=local_dict)


def latex_needed(expression, printer=sympy.pretty) -> bool:
    if expression == sympy.zoo:
        return True
    try:
        return bool(
            printer(parse(printer(expression))) != printer(expression)
        )
    except SyntaxError:
        return True


def latex2png(latex_str: str, outfile: str = "output.png"):
    response = requests.get(
        r"https://latex.codecogs.com/png.latex?\dpi{110}&space;\fn_phv&space;\huge&space;" + latex_str)
    if response.ok:
        with open(outfile, "wb+") as file:
            file.write(response.content)
    else:
        raise ConnectionError("https://latex.codecogs.com/ don't respond correctly")


def calc(expression: str, latex: Union[None, bool] = None) -> str:
    result = parse(expression)

    if result.is_Equality:
        solve_set = sympy.solveset(result)
        if latex is False:
            return str(sympy.pretty(solve_set))
        try:
            latex2png(sympy.latex(solve_set))
            return ""
        except ConnectionError as e:
            print(e)
            return str(sympy.pretty(solve_set))

    if latex is None:
        latex = latex_needed(result)

    if not latex:
        return complement.printer_with_complement(result)
    try:
        latex2png(complement.printer_with_complement(result, printer=sympy.latex).replace("≈", r"\approx"))
        return ""
    except ConnectionError as e:
        print(e)
        return complement.printer_with_complement(result)
