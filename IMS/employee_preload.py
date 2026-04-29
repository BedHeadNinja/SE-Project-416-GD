"""
PREMADE SET OF EMPLOYEE ACCOUNTS TO POPULATE DATABASE
"""
from IMS import create_app
from IMS.models import User
import sqlalchemy as sa

# Create app and push app context(required for database access)
app = create_app()
app.app_context().push()

# Import database from app
from IMS import db

# Data
firstnamelist = ["Steve","Joseph","Sarah","Henry","Natalie","Jordan",
                "Paul","Jasmine","Christine","Jose","Vladimir","Fred"]

lastnamelist = ["Stevenson","Johnson","Copperfield","Smith","Hughman","Bobbins",
                "Saul","Gourd","Todd","Cortez","Krakowski","Flintstone"]

rolelist = ["Employee","Manager","Employee","Manager","Employee","Manager",
            "Employee","Manager","Employee","Manager","Employee","Manager"]

for i in range(len())
