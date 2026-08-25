## Install using PyPI
```bash
pip install substrate-interface
```

## Initialization

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
