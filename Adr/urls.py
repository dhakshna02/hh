from django.urls import path
from.import views 
from django.urls import reverse
 
urlpatterns = [
        path("",views.home , name="home"),
       
        path("about",views.About , name="About"),
       
        path ("products",views.products, name="products"),
        
      #  path("<str:id>",views.v1, name="views1"),
        
        path ("services",views.services, name="services"),
       
        path ("sap",views.sap, name="sap"),
       
        path ("s4hana",views.s4hana, name="s4hana"),
       
        path ("successfactors",views.successfactors, name="successfactors"),
       
        path ("sapb1",views.sapb1, name="sapb1"),
       
        path ("hybris",views.hybris, name="hybris"),
       
        path ("manufacturing",views.manufacturing, name="manufacturing"),
       
        path ("automotive",views.automotive, name="automotive"),
       
        path ("logistics",views.logistics, name="logistics"),
        
        path ("retail",views.retail, name="retail"),
       
        path ("education",views.education, name="education"),
       
        path ("career",views.career, name="career"),
       
                         
        path ("jobforms",views.jobforms,name="jobforms"),

        path ("contact",views.contact, name="contact"),

        path("fotopia",views.fotopia, name ="fotopia"),

        path ("smartboat",views.smartboat,name="smartboat"),

        path ("erp",views.erp,name="erp") ,

        path ( "itstaffing" , views.itstaffing,name= "itstaffing"), 

        path ("masterdata" , views.masterdata,name= "masterdata"), 
     
        path ("bigdat" , views.bigdat ,name= "bigdata"), 
 
        path ("itesandglobalsupport" , views.itesandglobalsupport ,name= "itesandglobalsupport"),       
        
        path ("careersucess" , views.careersuccess ,name= "careersucess"),

         path ("careerfail" , views.careerfail ,name= "careerfail"),

          path ("contactsucess" , views.contactsucess ,name= "contactsucess"),

           path ("contactfail" , views.contactfail ,name= "contactfail"),
]
