from django.db import models

'''
Talaba(ism, guruh, kurs, kitob_soni)
Muallif(ism, jins, tugilgan_sana, kitoblar_soni, tirik)
Kitob(nom, janr, sahifa, muallif(FK))
Kutubxonachi(ism, ish_vaqti)
Record(talaba(FK), kitob(FK), kutubxonachi(FK), olingan_sana, 
qaytardi(default=False), qaytarish_sana)
'''


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=255, blank=True, null=True)
    kurs = models.PositiveSmallIntegerField(default=1)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    JINS_CHOICES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=JINS_CHOICES, default='Erkak')
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50, blank=True, null=True)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Kutubxonachi(models.Model):
    ISH_VAQTI_CHOICES = (
        ('08:00-13:00', '08:00-13:00'),
        ('13:00-20:00', '13:00-20:00'),
    )

    ism = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=255, choices=ISH_VAQTI_CHOICES, default='08:00-13:00')

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytarish_sana = models.DateTimeField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.talaba.ism} - {self.kitob.nom}"

