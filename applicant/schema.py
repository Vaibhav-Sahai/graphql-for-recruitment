#******************************************************************************#
# Queries and Mutations Here                                                   #
#******************************************************************************#
import graphene
from serializers import (
    ApplicantGrapheneInputModel,
    ApplicantGrapheneModel,
)
from models.applicant import Applicant

#TODO: Add more custom queries here that the frontend can need
# Put queries here for the GraphQL API
class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value="World"))
    list_applicants = graphene.List(ApplicantGrapheneModel) # List of ALL applicants

    @staticmethod
    def resolve_say_hello(root, info, name):
        return f"Hello {name}!"
    
    @staticmethod
    def resolve_list_applicants(root, info):
        return Applicant.all()

# Put mutations here for the GraphQL API
class CreateApplicant(graphene.Mutation):
    class Arguments:
        applicant_details = ApplicantGrapheneInputModel()
    Output = ApplicantGrapheneModel

    @staticmethod
    def mutate(root, info, applicant_details):
        applicant = Applicant()
        applicant.email = applicant_details.email
        applicant.name = applicant_details.name
        applicant.year = applicant_details.year
        applicant.major = applicant_details.major
        applicant.second_major = applicant_details.second_major
        applicant.minor = applicant_details.minor
        applicant.second_minor = applicant_details.second_minor
        applicant.gpa = applicant_details.gpa
        applicant.website = applicant_details.website
        applicant.division = applicant_details.division
        applicant.why_team = applicant_details.why_team
        applicant.commitment = applicant_details.commitment
        applicant.value_to_club = applicant_details.value_to_club
        applicant.personal_goals = applicant_details.personal_goals

        applicant.save()

        return applicant

class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()