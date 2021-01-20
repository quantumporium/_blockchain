# import all the needed module
from hashlib import sha256
from datetime import date

import pickle




# Block class
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions    
        self.timestamp = timestamp # tell when the block is created
        self.nonce = 0 # used in the PoW algorithm
        self.hash = ''
        self.previous_hash = previous_hash
        return

# the data will be stored as a list with the order behin (index, transaction, timestamp, nonce, previous_hash)
    def get_hash(self):
        data = "".join(str((self.index, self.transactions, self.timestamp, self.nonce, self.previous_hash)))
        return sha256(data.encode()).hexdigest()

    def __str__(self):
        return str({'index:': self.index, 'transaction': self.transactions, 'timestamp:': self.timestamp, 'nonce': self.nonce, 'hash': self.hash,'previous_hash:': self.previous_hash})
        


class Blockchain:
    # how hard getting the response to the PoW will be
    difficulty = 2
    def __init__(self):
        self.pending_transactions = []
        self.chain = [] # were all the block will be store --> load blockchain() function use to load the blockchain from pickle
        self.hash_chain = [] # chain of hash used in the see_blokchain function in main.py

        self.create_genesis_block()
        self.load_chain()

    def dumps_chain(self):
        blockchainPickle = [self.chain, self.hash_chain]

        with open('blockchainPickle.pickle', 'wb') as blockchainPickleFile:
            pickle.dump(blockchainPickle, blockchainPickleFile)
        return

    def load_chain(self):
        try:
            open('blockchainPickle.pickle')
        except:
            open('blockchainPickle.pickle', 'wb')
        else:
            with open('blockchainPickle.pickle', 'rb') as pickle_file:
                blockchainPickle = pickle.load(pickle_file)
            
            self.chain = blockchainPickle[0]
            self.hash_chain = blockchainPickle[1]
            
        return
        

# first block in the blockchain
    def create_genesis_block(self):
        data = "Implementation of first blockchain application in python by QuantumPorium"
        genesis_block = Block(0, [data], (date.today()), '0')
        genesis_block.hash = genesis_block.get_hash()
        self.chain.append(genesis_block)
        self.hash_chain.append(genesis_block.hash)
    
    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

# if the blockchain is not valid
        if not Blockchain.is_valid_proof(block.hash, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        self.hash_chain.append(block.hash)
        return True

# return if the hash of the blockchain is valid - if the block itself is valid
    def is_valid_proof(block_hash, proof):
        return ((block_hash.startswith('0' * Blockchain.difficulty)) and (block_hash == proof))


    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.get_hash()

        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.get_hash()

        block.hash = computed_hash
        return computed_hash

    def mine(self):
        if not self.pending_transactions:
            return False

        last_block = self.last_block
        new_block = Block(index=last_block.index + 1, transactions=self.pending_transactions, timestamp=(date.today()), previous_hash=last_block.hash)
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        return

