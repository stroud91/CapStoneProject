from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_users():
    user1 = User(
        username='AliceWonder',
        email='alice@wonderland.io',
        password='passwordAlice',
        address='123 Wonderland St',
        phone='123-456-7890',
        profile_image_id=1,
        role='admin',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user2 = User(
        username='BobBuilder',
        email='bob@builder.io',
        password='passwordBob',
        address='456 Construct Ave',
        phone='987-654-3210',
        profile_image_id=2,
        role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user3 = User(
        username='CharlieChocolate',
        email='charlie@choco.io',
        password='passwordCharlie',
        address='789 Choco Blvd',
        phone='123-789-4560',
        profile_image_id=3,
        role='admin',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user4 = User(
        username='DavidDreamer',
        email='david@dream.io',
        password='passwordDavid',
        address='012 Dream Way',
        phone='456-123-7890',
        profile_image_id=4,
        role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user5 = User(
        username='EvaExplorer',
        email='eva@explore.io',
        password='passwordEva',
        address='345 Explore Rd',
        phone='789-123-4560',
        profile_image_id=5,
        role='admin',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    tobe_ornottobe = User(
        username='youguessedit',
        email='englishwriter@user.io',
        first_name='Tobe',
        last_name='Ornottobe',
        password='password6',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    stu_dent = User(
        username='studybuddy',
        email='hitthebooks@user.io',
        first_name='Stu',
        last_name='Dent',
        password='password7',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ali_bye = User(
        username='seeyoulater',
        email='farewellgreetings@goodbyes.io',
        first_name='Ali',
        last_name='Bye',
        password='password8',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sandy_shore = User(
        username='beachlover',
        email='waves@coastal.io',
        first_name='Sandy',
        last_name='Shore',
        password='password102',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    phil_up = User(
        username='gasstationguy',
        email='fuel@tank.io',
        first_name='Phil',
        last_name='Up',
        password='password103',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    barry_dalive = User(
        username='graveyardshift',
        email='spooky@crypt.io',
        first_name='Barry',
        last_name='Dalive',
        password='password104',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    holly_wood = User(
        username='filmstar',
        email='movies@la.io',
        first_name='Holly',
        last_name='Wood',
        password='password105',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    chris_pbacon = User(
        username='morningmeal',
        email='breakfast@meal.io',
        first_name='Chris',
        last_name='PBacon',
        password='password106',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    terry_bull = User(
        username='notsogood',
        email='warning@caution.io',
        first_name='Terry',
        last_name='Bull',
        password='password107',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    anita_bath = User(
        username='cleanclean',
        email='hygiene@wash.io',
        first_name='Anita',
        last_name='Bath',
        password='password108',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    carmen_getit = User(
        username='quickshopper',
        email='fast@buy.io',
        first_name='Carmen',
        last_name='Getit',
        password='password109',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    walter_fall = User(
        username='naturelover',
        email='scenic@hike.io',
        first_name='Walter',
        last_name='Fall',
        password='password110',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    willie_makeit = User(
        username='determined',
        email='goals@achieve.io',
        first_name='Willie',
        last_name='Makeit',
        password='password111',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    al_igator = User(
        username='swampguy',
        email='reptile@bayou.io',
        first_name='Al',
        last_name='Igator',
        password='password112',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ella_phant = User(
        username='bigandgentle',
        email='safari@zoo.io',
        first_name='Ella',
        last_name='Phant',
        password='password113',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ian_flatable = User(
        username='airfilled',
        email='balloons@party.io',
        first_name='Ian',
        last_name='Flatable',
        password='password114',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    norm_al = User(
        username='averagejoe',
        email='regular@everyday.io',
        first_name='Norm',
        last_name='Al',
        password='password115',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    catie_pillar = User(
        username='slowmover',
        email='nature@bugs.io',
        first_name='Catie',
        last_name='Pillar',
        password='password116',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rob_ank = User(
        username='bankerguy',
        email='money@savings.io',
        first_name='Rob',
        last_name='Ank',
        password='password117',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    joy_stick = User(
        username='gamerpro',
        email='games@console.io',
        first_name='Joy',
        last_name='Stick',
        password='password118',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    mary_go = User(
        username='funpark',
        email='roundandround@play.io',
        first_name='Mary',
        last_name='Go',
        password='password119',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    tina_bopper = User(
        username='dancefloor',
        email='music@party.io',
        first_name='Tina',
        last_name='Bopper',
        password='password120',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ian_tense = User(
        username='seriousguy',
        email='focus@work.io',
        first_name='Ian',
        last_name='Tense',
        password='password121',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.session.add_all([user1, user2, user3, user4, user5, tobe_ornottobe, stu_dent, ali_bye, sandy_shore, phil_up, barry_dalive, holly_wood, chris_pbacon, terry_bull,
    anita_bath, carmen_getit, walter_fall, willie_makeit, al_igator,
    ella_phant, ian_flatable, norm_al, catie_pillar, rob_ank, joy_stick,
    mary_go, tina_bopper, ian_tense])
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
