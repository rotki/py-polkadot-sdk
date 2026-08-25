This repository is a [rotki](https://rotki.com/)-maintained fork of
[JAMdotTech/py-polkadot-sdk](https://github.com/JAMdotTech/py-polkadot-sdk).
It removes functionality and dependencies that are not used by rotki.

This rotki-focused build specializes in read-only access to a
[Substrate](https://substrate.io) node: querying storage,
[SCALE](getting-started/common-concepts/#scale) decoding and convenience methods
for runtime metadata. Seed, private-key, signing and embedded light-client
support are deliberately excluded.

## Getting started
About [installation, initialization](getting-started/installation/) and useful background information.

## Usage
[Overview of available functionality](usage/query-storage/) and how to use it. 

## Function Reference
[Extensive reference](reference/base/) of functions and classes in the library.

## Extensions
Overview of available [extensions](/extensions/); adding or improving existing functionality.

## Metadata docs
[Documentation of Substrate metadata](https://polkascan.github.io/py-substrate-metadata-docs/) for well known runtimes and how to use it with py-substrate-interface.

## Contact and Support 

For questions, please see the [Substrate StackExchange](https://substrate.stackexchange.com/questions/tagged/python) or [GitHub Discussions](https://github.com/rotki/py-polkadot-sdk/discussions).

## License
[https://github.com/rotki/py-polkadot-sdk/blob/master/LICENSE](https://github.com/rotki/py-polkadot-sdk/blob/master/LICENSE)
