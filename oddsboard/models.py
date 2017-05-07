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
        value = 0
        for bc in self.betcombination_set.all():
            value += bc.betAmount()
        return value

    def totalBets(self):
        count = 0
        for bc in self.betcombination_set.all():
            count += bc.betCount()
        return count

    def __str__(self):
        return '#{} {}'.format(self.height, self.myHash)

class BetCombination(models.Model):
    block = models.ForeignKey(Block)
    betAddress = models.CharField(max_length=34)
    miner = models.ForeignKey(Pool)

    def betAmount(self):
        value = 0
        for deposit in self.deposit_set.all():
            value += deposit.amount
        return value

    def betCount(self):
        count = 0
        for deposit in self.deposit_set.all():
            count += 1
        return count

class Deposit(models.Model):
    betCombination = models.ForeignKey(BetCombination)
    amount = models.FloatField()
    address = models.CharField(max_length=34)
