import re


__camelcase_regex = re.compile(r"(?<!^)(ID|[A-Z])")
__snakecase_regex = re.compile(r"_(id|[a-z])")


def camelcase_to_snakecase(string: str) -> str:
    result = __camelcase_regex.sub(lambda m: "_" + m.group(1).lower(), string)
    return result


def snakecase_to_camelcase(string: str) -> str:
    result = __snakecase_regex.sub(lambda m: m.group(1).upper(), string)
    return result