from oddsboard.models import Block, Pool
from django.core.management.base import BaseCommand, CommandError
import requests as re

class Command(BaseCommand):
    help = 'import data from blockchain.info'


    def handle(self, *args, **options):

        start_block_height = 466500
        latest_block = re.get('https://blockchain.info/en/latestblock?format=json').json()

        valid_block_from_past = -5 #only blocks with 5 following blocks are considered valid
        latest_valid_block = latest_block['height'] + valid_block_from_past

        for height in range(start_block_height, latest_valid_block+1):
            received_block = re.get('https://blockchain.info/de/block-height/{}?format=json'.format(height)).json()['blocks'][0]
            new_block = Block(
              height = received_block['height'],
              my_hash = received_block['hash'],
              blockchaininfo_id = received_block['block_index'],
              previous_block = received_block['prev_block'],
              miner = None, # ToBeDefined
              in_main_chain = received_block['main_chain'],
              )
            new_block.save()

        for height in range(latest_valid_block+1, latest_valid_block+10):
            new_future_block = Block(
              height=height,
              in_main_chain=False,
            )
            new_future_block.save()
