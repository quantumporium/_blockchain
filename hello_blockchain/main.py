# import module you need
from blockchain import *

blockchain = Blockchain()

def add_transaction():
    print(('-' * 50), '\nWelcome to add transaction\n', ('-' * 50))
    numb_transactions = input("how much transaction you whant to do: ")

    for transaction in range(int(numb_transactions)):
        transaction_data = input("what do you whant the transaction to be: ")
        blockchain.pending_transactions.append(transaction_data)
    return

def mine_block():
    blockchain.mine()
    return

def see_blockchain():
    print(('-'*50), "\nWelcome to see blockchain\n",('-'*50))
    for block in range(len(blockchain.hash_chain)):
        print(f'[{block}] ',blockchain.hash_chain[block], '\n')

    index_block = input("do you whant to see a block in particular (y/n): ")
    
    if index_block.lower() in ('y', 'yes'):
        index_block = input('what is the index of the block you whant to see: ')
        see_block_particular(index_block)

    return

def see_block_particular(index_block):
    print(blockchain.chain[int(index_block)].__str__())
    return


function_choice = {
    'a': add_transaction,
    'b': mine_block,
    'c': see_blockchain
}

# REPL loop
if __name__ == '__main__':
    print('-' * 50)
    print("welcome to Hello Blockchain")
    print('-' * 50)
    while True:
        print('What do you whant to do:')
        choice = input("""
        a- Add a transaction:\n
        b- Mine block:\n
        c- see the block currently in the blockchain:\n
        What is your choice: """).lower()

        list_choice = ['a', 'b', 'c']

        if choice in list_choice:
            programme_to_play = function_choice[choice]()

        else:
            _break = input("We did not understand you answer do you whant to contine (y/n).")

            if _break.lower() == ('y' or 'yes'):
                continue
            else:
                break