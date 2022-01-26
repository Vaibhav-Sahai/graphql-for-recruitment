#from orator import Model
from db import Model

# Model which points to SQL table
class Applicant(Model):
    __table__ = '2022_spring_applicants'
    __timestamps__ = False
    pass
