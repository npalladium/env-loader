from __future__ import annotations

import os
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, TypeAlias

Transformer: TypeAlias = Callable[[str], Any]  #:
Validator: TypeAlias = Callable[
    [str, "EnvironmentVariable"], Optional[str]
]  #:
EnvironmentVariableDefinitions: TypeAlias = Dict[
    str, "EnvironmentVariable"
]  #:
EnvironmentVariableValues: TypeAlias = Dict[str, Any]  #:


class EnvLoaderError(Exception):
    """Base class for this projects errors."""


class MissingEnvironmentVariablesError(EnvLoaderError, ValueError):
    """Thrown when environment variables are found missing."""


class InvalidEnvironmentVariablesError(EnvLoaderError, ValueError):
    """Thrown when environment variables are found missing."""


@dataclass
class EnvironmentVariable:
    """
    Defines an Environment Variable to handle.
    """

    #: Name
    name: str
    is_required: bool = True
    default_val: Optional[str] = None
    description: Optional[str] = None
    transformers: List[Transformer] = field(default_factory=lambda: [])
    validators: List[Validator] = field(default_factory=lambda: [])


class EnvironmentVariableLoader:
    """
    This is the container for your :py:class:`EnvironmentVariable` definitions,
    along with their eventual loaded config values. Once :py:meth:`load_values`
    is ran on an instance of this class, the config values are addressable
    via the Python dict API.
    """

    def __init__(self, evar_defs: EnvironmentVariableDefinitions):
        """
        :param evar_defs: Pass in a dict whose keys are config
            names and the values are :py:class:`EnvironmentVariable`
            instances.
        """
        self.__evar_defs = evar_defs

    @classmethod
    def __load(
        cls, evar_defs: EnvironmentVariableDefinitions
    ) -> EnvironmentVariableValues:
        values_dict: Dict[str, Any] = {}
        missing = []
        for config_name, evar in evar_defs.items():
            values_dict[config_name] = (
                os.environ.get(evar.name) or evar.default_val
            )
            if evar.is_required and values_dict[config_name] is None:
                missing.append(evar.name)

        if len(missing) != 0:
            raise MissingEnvironmentVariablesError(
                f"Missing required environment variables: {missing}"
            )
        return values_dict

    @classmethod
    def __transform(
        cls,
        evar_defs: EnvironmentVariableDefinitions,
        current_values: EnvironmentVariableValues,
    ) -> EnvironmentVariableValues:
        for config_name, evar in evar_defs.items():
            for transformer in evar.transformers:
                current_val = current_values[config_name]
                new_val = transformer(current_val)
                current_values[config_name] = new_val
        return current_values

    @classmethod
    def __validate(
        cls,
        evar_defs: EnvironmentVariableDefinitions,
        current_values: EnvironmentVariableValues,
    ) -> None:
        validation_errors: Dict[str, List[str]] = {}
        for config_name, evar in evar_defs.items():
            for validator in evar.validators:
                current_val = current_values[config_name]
                error = validator(current_val, evar)
                if error is not None:
                    if validation_errors.get(evar.name) is None:
                        validation_errors[evar.name] = []
                    validation_errors[evar.name].append(error)

        if len(validation_errors) != 0:
            raise InvalidEnvironmentVariablesError(
                f"Invalid environment variables: {validation_errors}"
            )

    def __call__(self) -> Dict[str, Any]:
        """
        Go through the env var map, transferring the values to this object
        as attributes.

        :raises:  if a required env var isn't defined.
        :raises: RuntimeError if a required env var isn't defined.
        """

        values_dict = self.__class__.__load(self.__evar_defs)
        values_dict = self.__class__.__transform(self.__evar_defs, values_dict)
        self.__class__.__validate(self.__evar_defs, values_dict)

        return defaultdict(lambda: None, values_dict)
