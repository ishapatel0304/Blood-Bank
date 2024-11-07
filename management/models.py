from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.name} - {self.amount}"
