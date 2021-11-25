# Fun with blockchain

## What is going on here?
I want to implement my version of blockchain to learn about crypto 

## Notes
Do not forget!!
To better understand ETH, this blockchain borrow some things from the Ethereum blockchain.

### How to store data?
Two types of data:
 - permanent data
 - ephemeral data

An example of permanent data would be a transaction. Once a transaction has been fully confirmed, it is recorded in the transaction trie and it is never altered.

An example of ephemeral data would be the balance of a particular account address. The balance of an account address is stored in the state trie and is altered whenever transactions occurs with that particular account.

So, the permanent data and ephemeral data should be stored separately. This blockchain will use trie data structures to manage data, I think.


