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

    def __str__(self):
        return '#{} {}'.format(self.height, self.myHash)
