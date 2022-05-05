import re
from typing import *


class Tiffler:
    def __init__(self, template: str, case_sensitive: bool = True, **kwargs):
        self.template = template
        self.case_sensitive = case_sensitive
        self.build()

    def build(self):
        self.vars = []

        matches = []
        for match in re.finditer(r"(?<=[^\\]\{)[a-zA-Z_]\w*(?=\})", self.template):
            val = match.group()
            if val.isidentifier():
                assert val not in self.vars, f"Duplicate var name {val} found"
                self.vars.append(val)
                matches.append(match)

        self.exprs = []
        start_idx = 0
        for i, curr_match in enumerate(matches):
            end_idx = len(self.template)
            if i < len(matches) - 1:
                next_match = matches[i + 1]
                end_idx = next_match.start() - 1

            prefix = (
                rf"(?<={re.escape(self.template[start_idx:curr_match.start() - 1])})"
            )
            suffix = rf"(?={re.escape(self.template[curr_match.end() + 1:end_idx])})"
            start_idx = curr_match.end() + 1

            if self.case_sensitive:
                expr = re.compile(rf"{prefix}.*{suffix}")
            else:
                expr = re.compile(rf"{prefix}.*{suffix}", re.IGNORECASE)

            self.exprs.append(expr)

    def scan(self, text: str, /, **types: Dict[str, Type]) -> Dict[str, Any]:
        curr = text
        result = {}
        for var_name, expr in zip(self.vars, self.exprs):
            match = expr.search(curr)
            if match is None:
                return None

            var_value = match.group()
            if var_name in types:
                var_value = types[var_name](var_value)

            result[var_name] = var_value
            curr = curr[match.end() :]

        return result
