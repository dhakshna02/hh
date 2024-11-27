from django.db import models










 
    
class jobforms(models.Model):
    Name = models.CharField(max_length=100)
    Phoneno = models.CharField(max_length=15,blank=True,null=True)
    email= models.EmailField()
    resume = models.FileField(upload_to='resume/' )
    created_at = models.CharField(max_length=200,)
   
    def __str__(self):
        return self.created_at






    
    
class jobpost(models.Model):
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    time = models.CharField(max_length=300) 
    experience = models.CharField( max_length=100)
    description = models.TextField()   
        
    def __str__(self):
         return self.title   

    
   
    
class contact(models.Model):    
    name = models.CharField(max_length=150)
    email = models.EmailField( max_length=150)
    mesg = models.TextField()

    def __str__(self):
        return self.name

class images(models.Model):
    pagename = models.CharField(max_length=200)
    requiredpictures = models.ImageField() 


    def __str__(self):
        return self.pagename
    

class masterdatamanagement(models.Model): 
    heading = models.CharField(max_length=30)
    subhead1 = models.CharField(max_length=35)
    subtxt1 = models.CharField( max_length=400)

    subhead2 =models.CharField(max_length=50)
    subtxt2 = models.CharField(max_length=400)
   

    subhead3 = models.CharField(max_length=50)
    subtxt3 = models.CharField(max_length=400)
    

    subhead4 = models.CharField(max_length=50)
    subtxt4 = models.CharField(max_length=400)
    


    lowerhead = models.CharField(max_length=30)

    fsubhead1 = models.CharField(max_length=25)
    fsubtxt1 = models.CharField(max_length=125)

    fsubhead2 = models.CharField(max_length=25)
    fsubtxt2 = models.CharField(max_length=125)

    fsubhead3 = models.CharField(max_length=25)
    fsubtxt3 = models.CharField(max_length=125)

    fsubhead4 = models.CharField(max_length=25)
    fsubtxt4 = models.CharField(max_length=125)

    def __str__(self) -> str:
        return self.heading
    


class bigdata(models.Model): 
    heading = models.CharField(max_length=30)
    subhead1 = models.CharField(max_length=35)
    subtxt1 = models.CharField( max_length=400)

    subhead2 =models.CharField(max_length=50)
    subtxt2 = models.CharField(max_length=400)
   

    subhead3 = models.CharField(max_length=50)
    subtxt3 = models.CharField(max_length=400)
    

    subhead4 = models.CharField(max_length=50)
    subtxt4 = models.CharField(max_length=400)
    


    lowerhead = models.CharField(max_length=30)

    fsubhead1 = models.CharField(max_length=25)
    fsubtxt1 = models.CharField(max_length=125)

    fsubhead2 = models.CharField(max_length=25)
    fsubtxt2 = models.CharField(max_length=125)

    fsubhead3 = models.CharField(max_length=25)
    fsubtxt3 = models.CharField(max_length=125)

    fsubhead4 = models.CharField(max_length=25)
    fsubtxt4 = models.CharField(max_length=125)

    def __str__(self) -> str:
        return self.heading    
    

class itesglobal(models.Model): 
    heading = models.CharField(max_length=30)
    subhead1 = models.CharField(max_length=35)
    subtxt1 = models.CharField( max_length=400)

    subhead2 =models.CharField(max_length=50)
    subtxt2 = models.CharField(max_length=400)
   

    subhead3 = models.CharField(max_length=50)
    subtxt3 = models.CharField(max_length=400)
    

    subhead4 = models.CharField(max_length=50)
    subtxt4 = models.CharField(max_length=400)
    


    lowerhead = models.CharField(max_length=30)

    fsubhead1 = models.CharField(max_length=25)
    fsubtxt1 = models.CharField(max_length=125)

    fsubhead2 = models.CharField(max_length=25)
    fsubtxt2 = models.CharField(max_length=125)

    fsubhead3 = models.CharField(max_length=25)
    fsubtxt3 = models.CharField(max_length=125)

    fsubhead4 = models.CharField(max_length=25)
    fsubtxt4 = models.CharField(max_length=125)

    def __str__(self) -> str:
        return self.heading        