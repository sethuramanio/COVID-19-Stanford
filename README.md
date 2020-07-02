This is backend platform for hosting the TeleVital app used for COVID 19 remote identification. 
Mentor: Dr. Anoop Rao- Stanford school of medicine 

Project TeleVital:

As the number of Covid-19 cases are rapidly increasing, it is becoming more and more difficult for the healthcare professionals to handle the situation. TeleVital is a mobile application which helps in monitoring vitals such as [Heart Rate, Oxygen Saturation, Blood Pressure and Respiration Rate] out of which the atmost priority is given to Heart Rate and Respiration Rate.

On successful measurement of the vitals, it is sent to the doctor's application which will help the doctor determine the health of the patient. This data can also be stored for further anaysis.

Backend: 

Install these packages using pip and maintain the version

Django                        3.0.4
django-filter                 2.2.0 
djangorestframework           3.11.0 

runs on MYSql DB

create a database

Add these credentials in settings.py file

python manage.py migrate to migrate and auto create all the tables based on the models.py file.


