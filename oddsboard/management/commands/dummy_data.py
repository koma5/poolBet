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
          myHash="00000000000000000007dc0c9c1f5c7aa25655f8e9996bcf9b82eb02faf7e9d6",
          blockchainInfoId=1502797,
          previousBlock="0000000000000000020a07fbd9f0266a6be77eb81ca04c7d7ee94aea1f566ddb",
          miner=p1,
          inMainChain=True,
          )
        b.save()

        p = Pool(
          address = "2",
          name = "SlushPool",
        )
        p.save()

        b = Block(
          height=465306,
          myHash="00000000000000000125f00019e1d3550c1d75bff10198c00e34df021da9d5bf",
          blockchainInfoId=1504865,
          previousBlock="00000000000000000007dc0c9c1f5c7aa25655f8e9996bcf9b82eb02faf7e9d6",
          miner=p,
          inMainChain=True,
          )
        b.save()

        b = Block(
          height=465307,
          myHash="000000000000000000d0f94566697715ab2e29fda915e3f38918d45a5de8fb11",
          blockchainInfoId=1504865,
          previousBlock="00000000000000000125f00019e1d3550c1d75bff10198c00e34df021da9d5bf",
          miner=p,
          inMainChain=True,
          )
        b.save()

        b = Block(
          height=465308,
          myHash="000000000000000001fe8bd9cc962eb4fa1b8daa6cf08a4e223f81874c6f278c",
          blockchainInfoId=1504867,
          previousBlock="000000000000000000d0f94566697715ab2e29fda915e3f38918d45a5de8fb11",
          miner=p,
          inMainChain=True,
          )
        b.save()

        b = Block(
          height=465309,
          myHash="000000000000000000b40b5da384bd80c8d027c6161e3f35384a7ce95300f5d6",
          blockchainInfoId=1502798,
          previousBlock="000000000000000001fe8bd9cc962eb4fa1b8daa6cf08a4e223f81874c6f278c",
          miner=p,
          inMainChain=True,
          )
        b.save()

        b = Block(
          height=465310,
          previousBlock="000000000000000000b40b5da384bd80c8d027c6161e3f35384a7ce95300f5d6",
          inMainChain=False,
        )
        b.save()


        bc1 = BetCombination(
            block=b,
            betAddress="1337ZMMgXFHqiA7ujRMw3NfURC2Cm6FD2h",
            miner=p,
        )
        bc1.save()

        bc2 = BetCombination(
            block=b,
            betAddress="1337ZNncWgQvTUEBUiDXcrcZsEzZyaLNTx",
            miner=p1,
        )
        bc2.save()

        d = Deposit(
            betCombination=bc1,
            amount=.4,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betCombination=bc1,
            amount=.4,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betCombination=bc2,
            amount=.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betCombination=bc2,
            amount=.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betCombination=bc2,
            amount=.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()




        b1 = Block(
          height=465311,
          inMainChain=False,
        )
        b1.save()

        b2 = Block(
          height=465312,
          inMainChain=False,
        )
        b2.save()

        bc1 = BetCombination(
            block=b2,
            betAddress="1337zkf9XzvuhwdW2dHNBWHx3RZV1Fypq9",
            miner=p,
        )
        bc1.save()

        bc2 = BetCombination(
            block=b1,
            betAddress="1337vY9LM2ma9aKVvFVW3PVGezSMXeHWno",
            miner=p,
        )
        bc2.save()

        d = Deposit(
            betCombination=bc1,
            amount=5.3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betCombination=bc2,
            amount= .3,
            address="1koma5qm7M1bpJ37zXvrRmVoNJU9KaAVj",
        )
        d.save()

        d = Deposit(
            betCombination=bc1,
            amount=0.3,
            address="175o52E64wHQumzfLFnKrPaukJsvo9pgMb",
        )
        d.save()
