# coding: utf-8
Movie.objects.all()
Movie.objects.all()[2]
dj = Movie.objects.all()[2]
dj
dj.name
dj.rating
dj.name = 'Django'
dj.save()
dj.rating = 84
dj.save()
dj.year = 2014
dj.save()
dj.budget = 9999999
dj.s
dj.save()
dj = Movie.objects.all()[2:]
dj
dj[1].name
dj[1].name = XXXy
dj = Movie.objects.all()[4]
dj.name = 'XXXY'
dj.save()
Movie.objects.all()[4]
Movie.objects.all()[4].name = 'XXXT'
