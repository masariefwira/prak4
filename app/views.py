from datetime import datetime
from django.shortcuts import render,redirect
from . import models

'1. jelasin autofield (menambah otomatis iterasi dalam bentuk angka) dan charfield'
'2. bikin views index, jelasin (render itu respons dalam bentuk html)'
'3. bikin folder tempelates'
'4. bikin pelanggan.html'
'5. nambah url.py index'
'6. runserver, jelasin dan kasi liat all, get, sama filter'
'7. bikin views create data'
'8. bikin createdata.html'
'9. nambah url.py create data'
'10. runserver, jelasin nambah dan liat in berubahnya'
'11. bikin views update data'
'12. buka dan jelaskan updatedata.html'
'13. nambah url.py update data'
'14. runserver, jelasin'
'15. bikin views deletedata'
'16. nambah url.py delete data'
'17. runserver, liatin'

# Create your views here.
def index(request):
    # Ambil data dari pelanggan
    # All
    allpelangganobj = models.pelanggan.objects.all()
    # Get 
    getpelangganobj = models.pelanggan.objects.get(idpelanggan=1)
    # Filter
    filterpelangganobj = models.pelanggan.objects.filter(jeniskelamin = 'Perempuan')

    return render(request,'pelanggan.html',{
        "allpelangganobj" : allpelangganobj,
        'getpelangganobj' : getpelangganobj,
        'filterpelangganobj' : filterpelangganobj
    })

def createdata(request):
    if request.method == "GET":
        return render(request,'createdata.html')
    else:
        nama = request.POST['nama']
        tanggal = request.POST['tanggal']
        jeniskelamin = request.POST['jeniskelamin']
        nohp = request.POST['nohp']

        newpelanggan = models.pelanggan(
            nama = nama,
            tanggallahir = tanggal,
            jeniskelamin = jeniskelamin,
            nohp = nohp
        ).save()
        return redirect('index')

def updatedata(request,id):
    pelangganobj = models.pelanggan.objects.get(idpelanggan=id)
    tanggal = datetime.strftime(pelangganobj.tanggallahir, '%Y-%m-%d')
    if request.method == 'GET':
        return render(request,'updatedata.html',{
            'pelangganobj':pelangganobj,
            'tanggal' :tanggal

        })
    else:
        nama = request.POST['nama']
        tanggal = request.POST['tanggal']
        jeniskelamin = request.POST['jeniskelamin']
        nohp = request.POST['nohp']
        pelangganobj.nama = nama
        pelangganobj.tanggal = tanggal
        pelangganobj.jeniskelamin = jeniskelamin
        pelangganobj.nohp = nohp
        pelangganobj.save()

        return redirect('index')

def deletedata(request,id):
    pelangganobj = models.pelanggan.objects.get(idpelanggan = id)
    pelangganobj.delete()
    return redirect('index')