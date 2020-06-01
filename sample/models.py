from django.db import models

class station1(models.Model):
    stationName = models.CharField(max_length=100, default='横浜駅')
    usertOfStation = models.IntegerField(default=0)

    def __str__(self):
        return '<station:id=' + str(self.id) + ',' + \
            self.stationName

class regionInfo1(models.Model):
    cityName =  models.CharField(max_length=100, default='横浜')
    prefecture = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    annualIncome = models.IntegerField(default=0)

    def __str__(self):
        return '<region:id=' + str(self.id) + ',' + \
            self.cityName

class house(models.Model):
   name = models.CharField(max_length=100)
   setFee = models.IntegerField(default=0)
   FreeFee = models.IntegerField(default=0)
   destanceToStation = models.IntegerField(default=0)
   eventTimes = models.IntegerField(default=0)
   mjTables = models.IntegerField(default=0)
   address = models.CharField(max_length=100, default='dummy')
   station = models.ForeignKey(station1, on_delete=models.CASCADE)
   city = models.ForeignKey(regionInfo1, on_delete=models.CASCADE)

   def __str__(self):
        return '<MJhouse:id=' + str(self.id) + ',' + \
            self.name + '(' + str(self.setFee) + ')'


    
   