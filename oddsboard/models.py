from django.db import models

class Pool(models.Model):
    address = models.CharField(max_length=34)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Block(models.Model):
    height = models.IntegerField(default=0)
    my_hash = models.CharField(max_length=64, null=True)
    blockchaininfo_id = models.IntegerField(null=True)
    previous_block = models.CharField(max_length=64, null=True)
    miner = models.ForeignKey(Pool, null=True)
    in_main_chain = models.BooleanField(default=False)

    def __str__(self):
        return '#{} {}'.format(self.height, self.myHash)

    def total_bet_amount(self):
        return self.betcombination_set.aggregate(bet_amount_sum=models.Sum('deposit__amount'))['bet_amount_sum']

    def total_bets(self):
        return self.betcombination_set.aggregate(bet_count_sum=models.Count('deposit'))['bet_count_sum']

class BetCombination(models.Model):
    block = models.ForeignKey(Block)
    bet_address = models.CharField(max_length=34)
    miner = models.ForeignKey(Pool)

class Deposit(models.Model):
    betcombination = models.ForeignKey(BetCombination)
    amount = models.FloatField()
    address = models.CharField(max_length=34)
