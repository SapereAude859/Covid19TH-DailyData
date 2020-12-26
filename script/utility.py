import re

html_tag = r".*<.*?>"
common = r"\""
datetime_str = r"[0-3]\d/[01]\d/(19|20)\d{2}\s[0-2]\d:[0-5]\d"
date_str = r"[0-3]\d/[01]\d/(19|20)\d{2}"
func_pat = r"(function.*)\);"


# Cleaning Function
def c_dict(d):
    for k, v in d.items():
        patterns = [html_tag, common]
        for pattern in patterns:
            if re.search(pattern, str(v), 0):
                d[k] = re.sub(pattern, "", v)
    return d


def c_list(lst):
    for i in range(0, len(lst)):
        c = lst[i]
        c_dict(c)
    return lst


# Matching Function
def m_func(script):
    match = re.search(func_pat, script[0])
    function = match.group(1)
    return function
