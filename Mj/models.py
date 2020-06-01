from django.db import models

class MJhouse(models.Model):
   name = models.CharField(max_length=100)
   setFee = models.IntegerField(default=0)
   FreeFee = models.IntegerField(default=0)
   destanceToStation = models.IntegerField(default=0)
   eventTimes = models.IntegerField(default=0)
   mjTables = models.IntegerField(default=0)   
   station = models.CharField(max_length=100, default=False)
   city = models.CharField(max_length=100, default=False)

   def __str__(self):
        return '<MJhouse:id=' + str(self.id) + ',' + \
            self.name + '(' + str(self.setFee) + ')'


class station1(models.Model):
   mjhouse = models.ForeignKey(MJhouse, on_delete=models.CASCADE)
   usertOfStation = models.IntegerField(default=0)

   #def __str__(self):
   #     return '<station:id=' + str(self.id) + ',' + \
   #          self.staion + '(' + str(self.usertOfStation) + ')'

class regionInfo1(models.Model):
    mjhouse = models.ForeignKey(MJhouse, on_delete=models.CASCADE)
    prefecture = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    annualIncome = models.IntegerField(default=0)

    #def __str__(self):
    #    return '<regionInfo:id=' + str(self.id) + ',' + \
    #        self.city + '(' + str(self.population) + ')'   
    
   