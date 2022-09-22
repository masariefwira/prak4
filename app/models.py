from django.db import models

# Create your models here.

class pelanggan(models.Model):
    idpelanggan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    jeniskelamin = models.CharField(max_length=15)
    tanggallahir = models.DateField()
    nohp = models.IntegerField()

    def __str__(self):
        return str(self.nama)
        

class kamar(models.Model):
    idkamar = models.AutoField(primary_key=True)
    nokamar = models.IntegerField()
    jeniskamar = models.CharField(max_length=15)
    konfirmasikamar = models.BooleanField()

    def __str__(self):
        return str(self.nokamar)

class penyewaan(models.Model):
    idpenyewaan = models.AutoField(primary_key=True)
    idpelanggan = models.ForeignKey(pelanggan,on_delete=models.CASCADE)
    idkamar = models.ForeignKey(kamar,on_delete=models.CASCADE)
    tanggalsewa = models.DateField()
    hargasewa = models.IntegerField()

    def __str__(self):
        return str(self.idpenyewaan) + ' - ' + str(self.idpelanggan)
class charge(models.Model):
    idcharge = models.AutoField(primary_key=True)
    jenischarge = models.CharField(max_length=50)
    hargacharge = models.IntegerField()
    
    def __str__(self):
        return str(self.jenischarge)

class detailcharge(models.Model):
    iddetailcharge = models.AutoField(primary_key=True)
    idpenyewaan = models.ForeignKey(penyewaan,on_delete=models.CASCADE)
    idcharge = models.ForeignKey(charge,on_delete=models.CASCADE)
    jumlahitemcharge = models.IntegerField()

    def __str__(self):
        return str(self.iddetailcharge)