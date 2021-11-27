# Fun with blockchain

## What is going on here?
I want to implement my version of blockchain to learn about crypto 

## Notes
Do not forget!! <br>
To better understand ETH, this blockchain borrow some things from the Ethereum blockchain.

### How to store data?
Two types of data:
 - permanent data
 - ephemeral data

An example of permanent data would be a transaction. Once a transaction has been fully confirmed, it is recorded in the transaction trie and it is never altered.

An example of ephemeral data would be the balance of a particular account address. The balance of an account address is stored in the state trie and is altered whenever transactions occurs with that particular account.

So, the permanent data and ephemeral data should be stored separately. This blockchain will use trie data structures to manage data, I think.

### State trie
This global state trie is constantly updated.
The state trie contains a **key and value pair** for every account which exists on the Ethereum network. <br>

The **key** is a signle 160 bit indentifier (the address of Blockchain account). <br>

The **value** in the global state trie is created by encoding account details of an Blockchain account. I think it will be Recursive-Length Prefix encoding (RLP) method([pylib](https://pypi.org/project/rlp/), [tutorial](https://ethereum-classic-guide.readthedocs.io/en/latest/docs/appendices/recursive_length_prefix.html)). <br>
Account details:
- nonce
- balance
- storageRoot
- codeHash

### Transaction trie — one per block
...
