"""
PREMADE SET OF INVENTORY ITEMS TO POPULATE DATABASE
"""
from IMS import create_app
from IMS.models import Product
import sqlalchemy as sa

# Create app and push app context(required for database access)
app = create_app()
app.app_context().push()

# Import database from app
from IMS import db

# Data
namelist = ["test","Gizmo","Gadget","Doodad","Krompus","Megakrompus","Goblin","Napoleon Bonapart Action Figure",
            "Long Piece of String","Sosauge Mcbiscuit","Poison","Antidote","Nuclear Warhead", "Another Item Name",
            "Question","Answer","Ultimate Answer","Problem","Solution","US Declaration of Independence","XXXXXXXXXXL Pantaloon",
            "Cigarette"]
quantitylist = [15,25,57,800,47,5,19,
                200,2,574,7547,0,7,50,
                10000,0,42,99,1,1776,1,500]

added = 0

for i in range(len(namelist)):
    p = Product(product_name=namelist[i], on_hand_count=quantitylist[i])
    inDatabase = db.session.scalar(sa.select(Product).where(Product.product_name == p.product_name))

    if not inDatabase:
        db.session.add(p)
        db.session.commit()
        print(f"{p.product_name} successfully added to database")
        added += 1
    else:
        print(f"{p.product_name} already in database")

print(f"Inventory addition complete.\n{' '*10}Items added: {added}\n{' '*10}Items skipped: {len(namelist) - added}")
