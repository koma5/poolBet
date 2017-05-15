from django.db import models

class Pool(models.Model):
    address = models.CharField(max_length=34)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Block(models.Model):
    height = models.IntegerField(default=0)
    myHash = models.CharField(max_length=64, null=True)
    blockchainInfoId = models.IntegerField(null=True)
    previousBlock = models.CharField(max_length=64, null=True)
    miner = models.ForeignKey(Pool, null=True)
    inMainChain = models.BooleanField(default=False)

    def totalBetAmount(self):
        return self.betcombination_set.aggregate(bet_amount_sum=models.Sum('deposit__amount'))['bet_amount_sum']

    def totalBets(self):
        return self.betcombination_set.aggregate(bet_count_sum=models.Count('deposit'))['bet_count_sum']

    def __str__(self):
        return '#{} {}'.format(self.height, self.myHash)

class BetCombination(models.Model):
    block = models.ForeignKey(Block)
    betAddress = models.CharField(max_length=34)
    miner = models.ForeignKey(Pool)

class Deposit(models.Model):
    betCombination = models.ForeignKey(BetCombination)
    amount = models.FloatField()
    address = models.CharField(max_length=34)
