#******************************************************************************#
# Return and Input Serializers for the Applicant API                           # 
#******************************************************************************#
from datetime import date, datetime
from typing import List, Optional
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel
from pymysql import Time

# This is a pydantic to sql model converter
class ApplicantModel(BaseModel):
    # TODO: Add a time field option to take in a string and convert it to YYYY-MM-DD HH:MM:SS
    #timestamp: Time
    email: str
    name: str
    year: str
    major: str
    second_major: Optional[str]
    minor: Optional[str]
    second_minor: Optional[str]
    gpa: str
    website: Optional[str]
    division: List[str]
    why_team: str
    commitment: str
    value_to_club: str
    personal_goals: str

class ApplicantGrapheneModel(PydanticObjectType):
    class Meta:
        model = ApplicantModel

class ApplicantGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = ApplicantModel
        #exclude_fields = ('email',) # email is the primary key