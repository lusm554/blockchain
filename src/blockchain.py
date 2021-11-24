import binascii

from collections import OrderedDict

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import json
import hashlib
import requests
from urllib.parse import urlparse
from uuid import uuid4
from time import time

MINING_SENDER = "THE BLOCKCHAIN"
MINING_REWARD = 1
MINING_DIFFICULTY = 2

class Blockchain:

    def __init__(self):
        # List of transactions that will be added to the next block
        self.tx = []
        # The actual blockchain
        self.chain = []
        # Set containing node urls
        self.nodes = set()
        # String to identify the blockchain node
        self.node_id = str(uuid4()).replace('-', '')
        # Create genesis block
        self.create_block(0, '00')


    def create_block(self, nonce: int, prev_hash: str) -> dict:
        """
        Add a block of transactions to the blockchain
        """
        block = {
            'block': len(self.chain) + 1,
            'timestamp': time(),
            'tx': self.tx,
            'nonce': nonce,
            'prev_hash': prev_hash
        }

        # Reset the current list of transactions
        self.tx = []

        # Add new block
        self.chain.append(block)

        return block


    def register_node(self, node_url: str) -> None:
        """
        Add a new node to the list of nodes
        """
        # Check node_url for valid format
        parsed_url = urlparse(node_url)
        
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts url like '192.168.0.5:5000'
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError("Invalid URL")

    
    def hash(self, block: dict) -> str:
        """
        Create a SHA-256 hash of a block
        """
        # We need to sort dict or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()


    def verify_tx_sign(self, sender_addr, sign, tx):
        """
        Check that the provided sign corresponds to transaction
        signed by the public key(sender_addr)
        """
        public_key = RSA.importKey(binascii.unhexlify(sender_addr))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA.new(str(tx).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(sign))

    
    def submit_tx(self, sender_addr, recipient_addr, value, sign):
        """
        Add a transaction to transactions list if the sign verified
        """
        tx = OrderedDict({
            'sender_addr': sender_addr,
            'recipient_addr': recipient_addr,
            'value': value
        })
        
        # Reward for mining a block
        if sender_addr == MINING_SENDER:
            self.tx.append(tx)
            return len(self.chain) + 1

        # Manages tx from wallet to another wallet
        tx_verification = self.verify_tx_sign(sender_addr, sign, tx)
        if tx_verification:
            self.tx.append(tx)
            return len(self.chain) + 1
        else:
            return False


    def valid_proof(self, tx, last_hash, nonce, difficulty=MINING_DIFFICULTY) -> bool:
        """
        Check if a hash value satisfies the mining conditions. This function is
        used within the proof_of_work function.
        """
        guess = (str(tx) + str(last_hash) + str(nonce)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == '0' * difficulty 

    
    def valid_chain(self, chain) -> bool:
        """
        Check if a blockchain is valid
        """
        last_block = chain[0]
        i = 1

        while i < len(chain):
            block = chain[i]
            
            # Check that the hash of block is correct
            if block['prev_hash'] != self.hash(last_block):
                return False
            
            # Check Proof of Work
            
            # Delete reward tx
            txs = block['tx'][:-1]
            
            if not self.valid_proof(txs, block['prev_hash'], block['nonce'], MINING_DIFFICULTY):
                return False
            
            last_block = block
            i += 1
        
        return True


    def proof_of_work(self):
        """
        Proof of work algorithm
        """
        last_block = self.chain[-1]
        last_hash = self.hash(last_block)

        nonce = 0
        while not self.valid_proof(self.tx, last_hash, nonce):
            nonce += 1

        return nonce


