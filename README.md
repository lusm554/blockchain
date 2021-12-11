# Fun with blockchain

## What is going on here?
I want to implement my version of blockchain to learn about crypto 

## Notes
Do not forget!! <br>
To better understand ETH, this blockchain borrow some things from the Ethereum blockchain. <br>
LevelDB better for this purpose, but for raw version let's use MongoDB.

[](docs/block-header.png)

### How to store data?
Two types of data:
 - permanent data
 - ephemeral data

An example of permanent data would be a transaction. Once a transaction has been fully confirmed, it is recorded in the transaction trie and it is never altered.

An example of ephemeral data would be the balance of a particular account address. The balance of an account address is stored in the state trie and is altered whenever transactions occurs with that particular account.

So, the permanent data and ephemeral data should be stored separately. This blockchain will use trie data structures to manage data, I think.

### State trie
The one and only one global state trie. The state trie contains a **key and value pair** for every account which exists on the Ethereum network. <br>
The **key** is a signle 160 bit indentifier (the address of Blockchain account). <br>
The **value** is encoding account details of an Blockchain account. I think it will be Recursive-Length Prefix encoding (RLP) method([pylib](https://pypi.org/project/rlp/), [tutorial](https://ethereum-classic-guide.readthedocs.io/en/latest/docs/appendices/recursive_length_prefix.html)). <br>
Account details:
- nonce
- balance
- storageRoot
- codeHash
Unlike the transaction and receipt tries, the state trie updates over time, constantly.

### Transaction trie — one per block
The transaction root exists within the block header. Since the ordering of the data is mostly decided upon by the miner, we do not know what the data looks like until it is mined. <br>
Parameters:
- account nonce
- gas price
- gas limit
- recipient
- transfer value
- transaction signature values
- account initialization (if transaction is of contract creation type), or transaction data (if transaction is a message call)

Once the block is mined, the transaction trie is never updated.

### Receipt Trie
The Receipt root lives within the block header and its purpose it to record the outcome of transaction. According to the yellow paper, the receipt trie can also be useful for zero-knowledge proofs or researches. <br>
Parameters:
- post-transaction state
- cumulative gas used
- logs
- bloom filter created from the information of the above logs
This trie never updates.

### Storage Trie
The storage trie is where all the contract data lives, and there is a separate storage trie for each account. <br>
At the moment Blochain will be without storage trie.

