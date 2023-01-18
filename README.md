# Env Loader

This package can create a config dict from environment variables, performing validations and mappings in the process.

Fork (and an unendorsed spiritual successor) of [evarify](https://github.com/gtaylor/evarify).

![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Stability

- This is currently a pre-alpha stage software that has not yet been used in production, may contain bugs and sharp edges.
- The package API is also not stable.

## Library Philoosphy

### Goals

- Simple API with sane defaults that is easy to use.
- Simple Implementation following current industry standard practices.
- Easy to understand, maintain and fork.
- Reasonably performant.
- *Eventually*, a stable API.

### Non-goals

- Extreme performance.
- Support for other configuration formats such as files (`yaml`, `.env` etc.) or command-line flags.

## Usage

### Installation

With pip:
```bash
python3 -m pip install git+https://github.com/npalladium/env-loader.git
```

With poetry:
```bash
poetry add git+https://github.com/npalladium/env-loader.git
```

Refer ['pip install' From a Git Repository](https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/) for how this works.


### Usage

A simple example:
```python3
from env_loader import (
    EnvironmentVariable,
    EnvironmentVariableLoader,
    EnvLoaderError,
)

env_definitions = {
    "ENV_VAR1": EnvironmentVariable(name="ENV_VAR1"),
    "ENV_VAR2": EnvironmentVariable(name="ENV_VAR2_DIFF_NAME"),
    "ENV_VAR3": EnvironmentVariable(
        name="ENV_VAR3",
        is_required=False,
    ),
    "ENV_VAR4": EnvironmentVariable(
        name="ENV_VAR3",
        default_val="qwertyuiop",
    ),
}

load_env = EnvironmentVariableLoader(env_definitions)

env_values = load_env()  # returns a defaultdict

# If ENV_VAR1 and ENV_VAR2_DIFF_NAME are not present, you will get the following error:
# MissingEnvironmentVariablesError: Missing required environment variables: ['ENV_VAR1', 'ENV_VAR2_DIFF_NAME']

env_var3 = env_values["ENV_VAR3"]
```

## Alternatives

- [Pydantic](https://github.com/pydantic/pydantic)
- [Dynaconf](https://github.com/dynaconf/dynaconf)
- [evarify](https://github.com/gtaylor/evarify)

## TODOs

- [ ] README
    - [x] Usage instructions
    - [x] Library philosophy, goals and non-goals
- [ ] Documentation
- [ ] Tests
- [ ] Improve types
- [ ] Publish to PyPI


## Copyright

- Portions Copyright Gregory Taylor
- Portions Copyright Nikhil Reddy

## License

- The current library is MIT licensed.
- [evarify](https://github.com/gtaylor/evarify) is licensed under the MIT License.
