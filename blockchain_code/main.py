# import module you need
from blockchain import *
import os
import time

blockchain = Blockchain()
try_again_choice = ['y', 'n', 'yes', 'no']

def makeHeader():
    os.system('cls')
    print("*"*50)
    print("Welcome to Hello Blockchain")
    print('*'*50)


def add_transaction():
    makeHeader()

    try:
        numb_transactions = int(input("how much transaction you whant to do: "))
    except :
        try_again = input('An error occur do you whant to try again (y/n).').lower()

        if try_again in try_again_choice:
            add_transaction()
        else:
            return
    else:
        for transaction in range(int(numb_transactions)):
            transaction_data = input("what do you whant the transaction to be: ")
            blockchain.pending_transactions.append(transaction_data)
        
    return

def mine_block():
    blockchain.mine()
    try:
        print('Block was mined successfully.')
        print(f"Info on the block \nBlock Index: {blockchain.chain[-1].index} \nBlock hash: {blockchain.chain[-1].hash} \nTransaction in block: {blockchain.chain[-1].transactions} \n")
        print("type ctrl + c to go to the main page.")
        time.sleep(60)
    except:
        return

def see_blockchain():
    makeHeader()

    for block in range(len(blockchain.hash_chain)):
        print(f'[{block}] ',blockchain.hash_chain[block], '\n')

    index_block = input("do you whant to see a block in particular (y/n): ").lower()
    
    if index_block.lower() in ('y', 'yes'):
        choose_block_index()

    return

def choose_block_index():
    try:
        index_block = int(input('What is the index of the block you whant to see: '))
    except:
        try_again = input('An error occur do you whant to try again (y/n).').lower()

        if try_again in try_again_choice:
            choose_block_index()
        else:
            return
    else:
        see_block_particular(index_block)

def see_block_particular(index_block):
    try:
        blockchain.chain[int(index_block)]
    except:
        try_again = input('An error occur do you whant to try again (y/n).').lower()

        if try_again in try_again_choice:
            choose_block_index()
        else:
            return
    else:
        try:
            print("\ntype ctrl + c to go to the main page.\n")
            print(blockchain.chain[int(index_block)].__str__())
            time.sleep(60)

        except KeyboardInterrupt:
            return

def closeProg():
    makeHeader()

    print("You choose to leave have a good day.")
    blockchain.dumps_chain()
    time.sleep(10)
    
    exit()

function_choice = {
    'a': add_transaction,
    'b': mine_block,
    'c': see_blockchain,
    'q': closeProg
}
'''
def whant_to_try_again():
    makeHeader()

    if choice in ['y', 'n', 'yes', 'no']:
        return True
    else:
        closeProg()
'''
   

# REPL loop
if __name__ == '__main__':
    makeHeader()

    while True:
        makeHeader()

        print('\nWhat do you whant to do:')
        choice = input("""
        a- Add a transaction:\n
        b- Mine block:\n
        c- see the block currently in the blockchain:\n
        q -close the program\n
        What is your choice: """).lower()

        list_choice = ['a', 'b', 'c', 'q']

        if choice in list_choice:
            programme_to_play = function_choice[choice.strip()]()
        else:
            _break = input("We did not understand you answer do you whant to contine (y/n).")

            if _break.lower() == ('y' or 'yes'):
                continue
            else:
                blockchain.dumps_chain()
                break