from django.db import models

class Kategoria(models.Model):
    kategoria_azon = models.AutoField(primary_key = True, editable = False, verbose_name = "kategoria_azon")
    nev = models.CharField( max_length=50, verbose_name = "kategoria_nev")

    def __str__(self):
        return self.nev
      
class Edesseg(models.Model):
    edesseg_azon = models.AutoField(primary_key = True, editable = False, verbose_name = "edesseg_azon")
    kategoria_azon = models.ForeignKey(Kategoria, verbose_name="kategoria_azon_kulsokulcs", on_delete=models.CASCADE)
    nev = models.CharField(verbose_name = "edesseg_nev" ,max_length=50)
    leiras = models.CharField(verbose_name = "lairas", max_length=100)
    ar = models.IntegerField(verbose_name = "ar")
    kep_utvonal = models.CharField(verbose_name = "kep_utvonal", max_length=60, null = True, blank = True)


    def __str__(self):
        return self.nev
    