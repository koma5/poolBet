from oddsboard.models import Block, Pool, BetCombination, Deposit
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Generate some dummy data.'


    def handle(self, *args, **options):

        p1 = Pool(
          address = "1",
          name = "BTC.com",
          )
        p1.save()

        b = Block(
          height=465305,
          my_hash="00000000000000000007dc0c9c1f5c7aa25655f8e9996bcf9b82eb02faf7e9d6",
          blockchaininfo_id=1502797,
          previous_block="0000000000000000020a07fbd9f0266a6be77eb81ca04c7d7ee94aea1f566ddb",
          miner=p1,
          in_main_chain=True,
          )
        b.save()

        p = Pool(
          address = "2",
          name = "SlushPool",
        )
        p.save()

        b = Block(
          height=465306,
          my_hash="00000000000000000125f00019e1d3550c1d75bff10198c00e34df021da9d5bf",
          blockchaininfo_id=1504865,
          previous_block="00000000000000000007dc0c9c1f5c7aa25655f8e9996bcf9b82eb02faf7e9d6",
          miner=p,
          in_main_chain=True,
          )
        b.save()

        b = Block(
          height=465307,
          my_hash="000000000000000000d0f94566697715ab2e29fda915e3f38918d45a5de8fb11",
          blockchaininfo_id=1504865,
          previous_block="00000000000000000125f00019e1d3550c1d75bff10198c00e34df021da9d5bf",
          miner=p,
          in_main_chain=True,
          )
        b.save()

        b = Block(
          height=465308,
          my_hash="000000000000000001fe8bd9cc962eb4fa1b8daa6cf08a4e223f81874c6f278c",
          blockchaininfo_id=1504867,
          previous_block="000000000000000000d0f94566697715ab2e29fda915e3f38918d45a5de8fb11",
          miner=p,
          in_main_chain=True,
          )
        b.save()

        b = Block(
          height=465309,
          my_hash="000000000000000000b40b5da384bd80c8d027c6161e3f35384a7ce95300f5d6",
          blockchaininfo_id=1502798,
          previous_block="000000000000000001fe8bd9cc962eb4fa1b8daa6cf08a4e223f81874c6f278c",
          miner=p,
          in_main_chain=True,
          )
        b.save()

        b = Block(
          height=465310,
          previous_block="000000000000000000b40b5da384bd80c8d027c6161e3f35384a7ce95300f5d6",
          in_main_chain=False,
        )
        b.save()


        bc1 = BetCombination(
            block=b,
            bet_address="1337ZMMgXFHqiA7ujRMw3NfURC2Cm6FD2h",
            miner=p,
        )
        bc1.save()

        bc2 = BetCombination(
            block=b,
            bet_address="1337ZNncWgQvTUEBUiDXcrcZsEzZyaLNTx",
            miner=p1,
        )
        bc2.save()

        d = Deposit(
            betcombination=bc1,
            amount=.4,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betcombination=bc1,
            amount=.4,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betcombination=bc2,
            amount=.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betcombination=bc2,
            amount=.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betcombination=bc2,
            amount=.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()




        b1 = Block(
          height=465311,
          in_main_chain=False,
        )
        b1.save()

        b2 = Block(
          height=465312,
          in_main_chain=False,
        )
        b2.save()

        bc1 = BetCombination(
            block=b2,
            bet_address="1337zkf9XzvuhwdW2dHNBWHx3RZV1Fypq9",
            miner=p,
        )
        bc1.save()

        bc2 = BetCombination(
            block=b1,
            bet_address="1337vY9LM2ma9aKVvFVW3PVGezSMXeHWno",
            miner=p,
        )
        bc2.save()

        d = Deposit(
            betcombination=bc1,
            amount=5.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betcombination=bc2,
            amount= .3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betcombination=bc1,
            amount=0.3,
            address="175o52E64wHQumzfLFnKrPaukJsvo9pgMb",
        )
        d.save()
