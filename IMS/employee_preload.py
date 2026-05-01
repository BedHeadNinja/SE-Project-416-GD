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
firstNameList = ["Steve","Joseph","Sarah","Henry","Natalie","Jordan",
                "Paul","Jasmine","Christine","Jose","Vladimir","Fred","Seymour","Arthur"]

lastNameList = ["Stevenson","Johnson","Copperfield","Smith","Hughman","Bobbins",
                "Saul","Gourd","Todd","Cortez","Krakowski","Flintstone","Posterior","Dent"]

rolelist = ["Employee","Manager","Employee","Manager","Employee","Manager",
            "Employee","Manager","Employee","Manager","Employee","Manager","Manager","Manager"]

added = 0

for i in range(len(firstNameList)):
    u = User(id=(100+i),name=(firstNameList[i]+" "+lastNameList[i]),role=rolelist[i])
    inDatabase = db.session.scalar(sa.select(User).where(User.id == u.id))

    if not inDatabase:
        db.session.add(u)
        db.session.commit()
        print(f"{u.name} successfully added to the database")
        added += 1
    else:
        print(f"{u.name} already in database")

print(f"User addition complete.\n{''*10}Users added: {added}\n{' '*10}Users skipped: {len(firstNameList) - added}")
