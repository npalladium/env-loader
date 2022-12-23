from typing import Any


def validate_is_not_none(config_val: str, evar: Any) -> None:
    """
    If the value is ``None``, fail validation.

    :param str config_val: The env var value.
    :param EnvironmentVariable evar: The EVar object we are validating
        a value for.
    :raises: ValueError if the config value is None.
    """
    if config_val is None:
        raise ValueError(
            "Value for environment variable '{evar_name}' can't "
            "be empty.".format(evar_name=evar.name)
        )


def validate_is_boolean_true(config_val: str, evar: Any) -> None:
    """
    Make sure the value evaluates to boolean True.

    :param str config_val: The env var value.
    :param EnvironmentVariable evar: The EVar object we are validating
        a value for.
    :raises: ValueError if the config value evaluates to boolean False.
    """
    if config_val is None:
        raise ValueError(
            "Value for environment variable '{evar_name}' can't "
            "be empty.".format(evar_name=evar.name)
        )
