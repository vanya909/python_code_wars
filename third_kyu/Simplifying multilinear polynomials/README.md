Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"