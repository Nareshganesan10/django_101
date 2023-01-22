from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse

    
class club(models.Model):
    league = models.CharField(max_length=50)
    cup = models.CharField(max_length=50)
    def full_name(self):
        return f"{self.league} {self.cup}"
    
    def __str__(self):
        return self.full_name()

class captain(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    club = models.OneToOneField(club, on_delete=models.CASCADE, null=True)
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.fullname()
    
class worldcup_teams(models.Model):
    country = models.CharField(max_length=30)
    stage = models.CharField(max_length=30)
    is_top_3 = models.BooleanField(default=False)
    captain = models.ForeignKey(captain, on_delete=models.CASCADE, null=True)
    goals = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(2)])
    # slug = models.SlugField(default="", null=True)
    
    def get_absolute_url(self):
        return reverse("find-result", args=[self.id])
    
    def __str__(self):
        return f"{self.country}, {self.captain} , Their result in WC ({self.stage})"