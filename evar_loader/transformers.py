from typing import List, Set


def comma_separated_str_to_list(config_val: str) -> List[str]:
    """
    Splits a comma-separated environment variable into a list of strings.

    :param str config_val: The env var value.
    :param EnvironmentVariable evar: The EVar object we are validating
        a value for.
    :rtype: list
    :return: The equivalent list for a comma-separated string.
    """
    if not config_val:
        return []
    return [token.strip() for token in config_val.split(",")]


def comma_separated_to_set(config_val: str) -> Set[str]:
    """
    Splits a comma-separated environment variable into a set of strings.

    :param str config_val: The env var value.
    :param EnvironmentVariable evar: The EVar object we are validating
        a value for.
    :rtype: set
    :return: The equivalent set for a comma-separated string.
    """
    return set(comma_separated_str_to_list(config_val))


def value_to_none(config_val: str) -> str | None:
    """
    Given a value that evaluates to a boolean False, return None.

    :param str config_val: The env var value.
    :param EnvironmentVariable evar: The EVar object we are validating
        a value for.
    :rtype: str or None
    :return: Either the non-False value or None.
    """
    if not config_val:
        return None
    return config_val


def value_to_int(config_val: str) -> int:
    """
    Convert the value to int.

    :param str config_val: The env var value.
    :param EnvironmentVariable evar: The EVar object we are validating
        a value for.
    :rtype: int
    """
    return int(config_val)


def value_to_bool(config_val: str) -> bool:
    """
    Massages the 'true' and 'false' strings to bool equivalents.

    :param str config_val: The env var value.
    :param EnvironmentVariable evar: The EVar object we are validating
        a value for.
    :rtype: bool
    :return: True or False, depending on the value.
    """
    if not config_val:
        return False
    if config_val.strip().lower() == "true":
        return True
    else:
        return False
