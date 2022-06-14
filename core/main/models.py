from django.db import models


# Create your models here.

class Homepage(models.Model):
    img = models.ImageField('Homepage logo img', upload_to='media')
    name1 = models.CharField('Homepage name1', max_length=100)
    name2 = models.CharField('Homepage name2', max_length=100)
    about = models.TextField('Homepage about')
    

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'



class Homepage1(models.Model):
    img = models.ImageField('Homepage1 logo img', upload_to='media')
    name = models.CharField('Homepage1 name', max_length=100)
    about = models.TextField('Homepage1 about')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Homepage1'
        verbose_name_plural = 'Homepages1'



class Homepage2(models.Model):
    img = models.ImageField('Homepage2 logo img', upload_to='media')
    name = models.CharField('Homepage2 name', max_length=100)
    about = models.TextField('Homepage2 about')
    

    def __str__(self):
        return self.name



class Homepage3(models.Model):
    img = models.ImageField('Homepage3 logo img', upload_to='media')
    name = models.CharField('Homepage3 name', max_length=100)
    price = models.IntegerField('Homepage3 price')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Homepage3'
        verbose_name_plural = 'Homepages3'




class Homepage4(models.Model):
    img = models.ImageField('Homepage4 logo img', upload_to='media')
    name = models.CharField('Homepage4 name', max_length=100)
    about = models.TextField('Homepage4 about')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Homepage4'
        verbose_name_plural = 'Homepages4'




class Homepage5(models.Model):
    about = models.TextField('Homepage5 about')
    img = models.ImageField('Homepage5 logo img', upload_to='media')
    name = models.CharField('Homepage5 name', max_length=100)
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Homepage5'
        verbose_name_plural = 'Homepages5'



class Homepage6(models.Model):
    img = models.ImageField('Homepage6 logo img', upload_to='media')
    name = models.CharField('Homepage6 name', max_length=100)
    about = models.TextField('Homepage6 about')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Homepage6'
        verbose_name_plural = 'Homepages6'








class Aboutnew(models.Model):
    name = models.CharField('Aboutnew name', max_length=100)
    about = models.TextField('Aboutnew about')
    img = models.ImageField('Aboutnew logo img', upload_to='media')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aboutnew'
        verbose_name_plural = 'Aboutnews'




class Hotelpage(models.Model):
    img = models.ImageField('Hotelpage logo img', upload_to='media')
    name = models.CharField('Hotelpage name', max_length=100)
    about = models.TextField('Hotelpage about')
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hotelpage'
        verbose_name_plural = 'Hotelpages'



class Hotelpage2(models.Model):
    img = models.ImageField('Hotelpage2 logo img', upload_to='media')
    name2 = models.CharField('Hotelpage2 name2', max_length=100, null=True)
    name3 = models.CharField('Hotelpage2 name3', max_length=100, null=True)
    price = models.IntegerField('Hotelpage2 price')
    name = models.CharField('Hotelpage2 name', max_length=100)
    name4 = models.CharField('Hotelpage2 name4', max_length=100, null=True)
    name5 = models.CharField('Hotelpage2 name5', max_length=100, null=True)
    name6 = models.CharField('Hotelpage2 name6', max_length=100, null=True)

    
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hotelpage2'
        verbose_name_plural = 'Hotelpages2'




class Blogpage(models.Model):
    img = models.ImageField('Blogpage logo img', upload_to='media')
    name = models.CharField('Blogpage name', max_length=100)
    name1 = models.CharField('Blogpage name1', max_length=100, null=True)
    
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blogpage'
        verbose_name_plural = 'Blogpages'






class Blogpage1(models.Model):
    img = models.ImageField('Blogpage1 logo img', upload_to='media')
    name = models.CharField('Blogpage1 name', max_length=100)
    about = models.TextField('Blogpage1 name')
    
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blogpage1'
        verbose_name_plural = 'Blogpages1'

    












    

   

