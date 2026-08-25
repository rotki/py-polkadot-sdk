# Python Substrate Interface

[![Build Status](https://img.shields.io/github/actions/workflow/status/rotki/py-polkadot-sdk/unittests.yml?branch=master)](https://github.com/rotki/py-polkadot-sdk/actions?query=workflow%3A%22Run+unit+tests%22)
[![Latest Version](https://img.shields.io/pypi/v/substrate-interface.svg)](https://pypi.org/project/substrate-interface/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/substrate-interface.svg)](https://pypi.org/project/substrate-interface/)
[![License](https://img.shields.io/pypi/l/substrate-interface.svg)](https://github.com/rotki/py-polkadot-sdk/blob/master/LICENSE)

> [!NOTE]
> This repository is a [rotki](https://rotki.com/)-maintained fork of
> [JAMdotTech/py-polkadot-sdk](https://github.com/JAMdotTech/py-polkadot-sdk).
> It removes functionality and dependencies that are not used by rotki.

## Description
This rotki-focused build specializes in read-only access to a
[Substrate](https://substrate.io/) node: querying storage, SCALE decoding and
convenience methods for runtime metadata. It deliberately excludes seed,
private-key, signing and embedded light-client support.

## Documentation

* [Library repository and documentation](https://github.com/rotki/py-polkadot-sdk)
* [Metadata documentation for Polkadot and Kusama ecosystem runtimes](https://jamdottech.github.io/py-polkadot-metadata-docs/)

## Installation
```bash
pip install git+https://github.com/rotki/py-polkadot-sdk.git
```

## Development

Install the locked test and lint environments with [uv](https://docs.astral.sh/uv/):

```bash
uv sync --locked --group lint --group test
uv run pytest
```

Build the source and wheel distributions with:

```bash
uv build --no-sources
```

## Initialization

Using node RPC endpoint 
```python
substrate = SubstrateInterface(url="ws://127.0.0.1:9944")
```

After connecting certain properties like `ss58_format` will be determined automatically by querying the RPC node. At 
the moment this will work for most `MetadataV14` and above runtimes like Polkadot, Kusama, Acala, Moonbeam. For 
older or runtimes under development the `ss58_format` (default 42) and other properties should be set manually. 

## Quick usage

### Balance information of an account
```python
result = substrate.query('System', 'Account', ['F4xQKRUagnSGjFqafyhajLs94e7Vvzvr8ebwYJceKpr8R7T'])
print(result.value['data']['free']) # 635278638077956496
```
### Convert a public key to an SS58 address

```python
keypair = Keypair(
    public_key='0xe4359ad3e2716c539a1d663ebd0a51bdc5c98a12e663bb4c4402db47828c9446',
    ss58_format=0,
)
print(keypair.ss58_address)
```

## Contact and Support 

For questions, please see the [Substrate StackExchange](https://substrate.stackexchange.com/questions/tagged/python) or [GitHub Discussions](https://github.com/rotki/py-polkadot-sdk/discussions).

## License
https://github.com/rotki/py-polkadot-sdk/blob/master/LICENSE
