from typing import Any, Self
from Adr.models import jobpost
from django.core.management.base import BaseCommand
from django.contrib.messages.views import SuccessMessageMixin


class command(BaseCommand):
        help="inserts data "

        def handle(self, *args: Any, **options: Any) -> str | None:
            return super().handle(*args, **options)
         
        title=[ "job1", "job1",  "job1",  "job1", "job1", "job1",]
 
        location= ["chennai","chennai","chennai","chennai","chennai","chennai", ]
 
        time= ["fulltime","fulltime","fulltime","fulltime","fulltime","fulltime",]

        experience =[ "3+","3+","3+","3+","3+","3+",]

        description = ["dhuvvvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnaav iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ccccccccccccg00","dhuvvvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnaav iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ccccccccccccg00","dhuvvvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnaav iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ccccccccccccg00","dhuvvvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnaav iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ccccccccccccg00","dhuvvvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnaav iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ccccccccccccg00","dhuvvvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnaav iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ccccccccccccg00",]

        for title,location,time,experience,description in zip(title,location,time,experience,description):
         jobpost.objects.create(title=title,location=location,time=time,experience=experience,description=description)
   
        Self.stdout.write(Self.style.success("completed inserting"))