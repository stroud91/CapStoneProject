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
    jill_out = User(
        username='relaxer',
        email='chill@relax.io',
        first_name='Jill',
        last_name='Out',
        password='password122',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    art_ist = User(
        username='paintsbrushes',
        email='canvas@studio.io',
        first_name='Art',
        last_name='Ist',
        password='password123',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rob_inhood = User(
        username='sherwood',
        email='arrow@archer.io',
        first_name='Rob',
        last_name='Inhood',
        password='password124',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ella_vate = User(
        username='upanddown',
        email='lift@elevator.io',
        first_name='Ella',
        last_name='Vate',
        password='password125',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    andy_gravity = User(
        username='flyhigh',
        email='space@nasa.io',
        first_name='Andy',
        last_name='Gravity',
        password='password126',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    anne_tenna = User(
        username='signalboost',
        email='radio@broadcast.io',
        first_name='Anne',
        last_name='Tenna',
        password='password127',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    will_power = User(
        username='determination',
        email='motivation@success.io',
        first_name='Will',
        last_name='Power',
        password='password128',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    luke_out = User(
        username='looker',
        email='vision@watch.io',
        first_name='Luke',
        last_name='Out',
        password='password129',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sue_perb = User(
        username='exceptional',
        email='quality@best.io',
        first_name='Sue',
        last_name='Perb',
        password='password130',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ivan_idea = User(
        username='thinktank',
        email='brain@innovate.io',
        first_name='Ivan',
        last_name='Idea',
        password='password131',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    drew_paper = User(
        username='sketchbook',
        email='art@draw.io',
        first_name='Drew',
        last_name='Paper',
        password='password132',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    justin_time = User(
        username='alwaysontime',
        email='clock@timely.io',
        first_name='Justin',
        last_name='Time',
        password='password133',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    pat_down = User(
        username='security',
        email='check@airport.io',
        first_name='Pat',
        last_name='Down',
        password='password134',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sonny_day = User(
        username='weatherman',
        email='forecast@shine.io',
        first_name='Sonny',
        last_name='Day',
        password='password135',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    neil_down = User(
        username='devotee',
        email='pray@temple.io',
        first_name='Neil',
        last_name='Down',
        password='password136',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    bill_board = User(
        username='signmaker',
        email='advertise@ads.io',
        first_name='Bill',
        last_name='Board',
        password='password137',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    may_flowers = User(
        username='gardener',
        email='bloom@spring.io',
        first_name='May',
        last_name='Flowers',
        password='password138',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    stan_dup = User(
        username='comedian',
        email='jokes@laugh.io',
        first_name='Stan',
        last_name='Dup',
        password='password139',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    dee_veloper = User(
    username='codegeek',
    email='dee@codebase.io',
    first_name='Dee',
    last_name='Veloper',
    password='password142',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    tim_ber = User(
    username='treehugger',
    email='tim@forest.io',
    first_name='Tim',
    last_name='Ber',
    password='password143',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    may_day = User(
    username='emergency',
    email='may@alert.io',
    first_name='May',
    last_name='Day',
    password='password144',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    glen_cove = User(
    username='naturalscenery',
    email='glen@landscape.io',
    first_name='Glen',
    last_name='Cove',
    password='password145',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    hal_lowed = User(
    username='holyman',
    email='hal@sanctuary.io',
    first_name='Hal',
    last_name='Lowed',
    password='password146',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    sam_wich = User(
    username='foodlover',
    email='sam@deli.io',
    first_name='Sam',
    last_name='Wich',
    password='password147',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    earl_ybird = User(
    username='morningperson',
    email='earl@sunrise.io',
    first_name='Earl',
    last_name='Ybird',
    password='password148',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    rose_bud = User(
    username='gardener',
    email='rose@floral.io',
    first_name='Rose',
    last_name='Bud',
    password='password149',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    ted_ebear = User(
    username='cuddlebuddy',
    email='ted@toys.io',
    first_name='Ted',
    last_name='Ebear',
    password='password150',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    ella_vate = User(
    username='lifter',
    email='ella@machines.io',
    first_name='Ella',
    last_name='Vate',
    password='password151',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    clara_net = User(
    username='musician',
    email='clara@band.io',
    first_name='Clara',
    last_name='Net',
    password='password152',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    violin_tunes = User(
    username='stringplayer',
    email='violin@orchestra.io',
    first_name='Viola',
    last_name='Tunes',
    password='password153',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    lee_der = User(
    username='headofthepack',
    email='lee@groups.io',
    first_name='Lee',
    last_name='Der',
    password='password154',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    crystal_ball = User(
    username='seer',
    email='crystal@future.io',
    first_name='Crystal',
    last_name='Ball',
    password='password155',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    jenny_rator = User(
    username='poweruser',
    email='jenny@energy.io',
    first_name='Jenny',
    last_name='Rator',
    password='password156',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    perry_odic = User(
    username='scientist',
    email='perry@elements.io',
    first_name='Perry',
    last_name='Odic',
    password='password157',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    sue_pernova = User(
    username='astronomer',
    email='sue@stars.io',
    first_name='Sue',
    last_name='Pernova',
    password='password158',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    anna_lytics = User(
    username='dataanalyst',
    email='anna@data.io',
    first_name='Anna',
    last_name='Lytics',
    password='password159',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)
    olive_branch = User(
        username='peacemaker',
        email='reconciliation@harmony.io',
        first_name='Olive',
        last_name='Branch',
        password='password140',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ella_ment = User(
        username='basic',
        email='foundations@roots.io',
        first_name='Ella',
        last_name='Ment',
        password='password141',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    earl_gray = User(
        username='tealover',
        email='brew@teapot.io',
        first_name='Earl',
        last_name='Gray',
        password='password142',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    jack_pot = User(
        username='luckyone',
        email='winner@casino.io',
        first_name='Jack',
        last_name='Pot',
        password='password143',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    moe_tion = User(
        username='onmove',
        email='dynamics@flow.io',
        first_name='Moe',
        last_name='Tion',
        password='password144',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    dale_ivery = User(
        username='fastservice',
        email='shipping@deliver.io',
        first_name='Dale',
        last_name='Ivery',
        password='password145',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    pat_riotic = User(
        username='proudlocal',
        email='pride@nation.io',
        first_name='Pat',
        last_name='Riotic',
        password='password146',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    jenny_rate = User(
        username='powerhouse',
        email='energy@produce.io',
        first_name='Jenny',
        last_name='Rate',
        password='password147',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rocky_road = User(
        username='icecreamlover',
        email='sweets@dessert.io',
        first_name='Rocky',
        last_name='Road',
        password='password148',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    steve_adore = User(
        username='entrancelover',
        email='welcome@doors.io',
        first_name='Steve',
        last_name='Adore',
        password='password149',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ty_tanic = User(
        username='bigship',
        email='ocean@vessel.io',
        first_name='Ty',
        last_name='Tanic',
        password='password150',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    liz_tening = User(
        username='goodlistener',
        email='hearing@conversations.io',
        first_name='Liz',
        last_name='Tening',
        password='password151',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    tom_orrow = User(
        username='planner',
        email='future@scheduled.io',
        first_name='Tom',
        last_name='Orrow',
        password='password152',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ann_chovy = User(
        username='pizzaaddict',
        email='toppings@pizza.io',
        first_name='Ann',
        last_name='Chovy',
        password='password153',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    frank_furter = User(
        username='hotdoglover',
        email='grill@bbq.io',
        first_name='Frank',
        last_name='Furter',
        password='password154',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ray_sing = User(
        username='trackstar',
        email='speed@racetrack.io',
        first_name='Ray',
        last_name='Sing',
        password='password155',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    daisy_chain = User(
        username='flowerfan',
        email='blossom@garden.io',
        first_name='Daisy',
        last_name='Chain',
        password='password156',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    brad_crumb = User(
        username='breadlover',
        email='baker@bakery.io',
        first_name='Brad',
        last_name='Crumb',
        password='password157',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rose_bush = User(
        username='gardeningpro',
        email='flowers@botany.io',
        first_name='Rose',
        last_name='Bush',
        password='password152',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    chip_munk = User(
        username='nutsforlife',
        email='acorns@forest.io',
        first_name='Chip',
        last_name='Munk',
        password='password153',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    cliff_hanger = User(
        username='suspenseking',
        email='stories@adventure.io',
        first_name='Cliff',
        last_name='Hanger',
        password='password154',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    wendy_wind = User(
        username='breezygirl',
        email='air@atmosphere.io',
        first_name='Wendy',
        last_name='Wind',
        password='password155',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    cole_dmine = User(
        username='deepdigger',
        email='ore@mine.io',
        first_name='Cole',
        last_name='Dmine',
        password='password156',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rocky_shore = User(
        username='oceanicman',
        email='waves@beach.io',
        first_name='Rocky',
        last_name='Shore',
        password='password157',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    crystal_ball = User(
        username='fortuneteller',
        email='future@predict.io',
        first_name='Crystal',
        last_name='Ball',
        password='password158',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sandy_beach = User(
        username='sunandsea',
        email='tides@ocean.io',
        first_name='Sandy',
        last_name='Beach',
        password='password159',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    bill_folds = User(
        username='walletman',
        email='cash@money.io',
        first_name='Bill',
        last_name='Folds',
        password='password160',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    terri_bull = User(
        username='monstermovies',
        email='horror@cinema.io',
        first_name='Terri',
        last_name='Bull',
        password='password161',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    barbie_cue = User(
        username='grillmaster',
        email='cooking@bbq.io',
        first_name='Barbie',
        last_name='Cue',
        password='password162',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ty_tan = User(
        username='giantfan',
        email='legends@myth.io',
        first_name='Ty',
        last_name='Tan',
        password='password163',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    lou_minate = User(
        username='shinebright',
        email='lights@glow.io',
        first_name='Lou',
        last_name='Minate',
        password='password164',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    holly_day = User(
        username='festivegirl',
        email='celebrate@events.io',
        first_name='Holly',
        last_name='Day',
        password='password165',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    phil_ter = User(
        username='cleanwater',
        email='purify@eco.io',
        first_name='Phil',
        last_name='Ter',
        password='password166',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.session.add_all([user1, user2, user3, user4, user5,
    tobe_ornottobe, stu_dent, ali_bye, sandy_shore,
    phil_up, barry_dalive, holly_wood, chris_pbacon,
    terry_bull, anita_bath, carmen_getit, walter_fall,
    willie_makeit, al_igator, ella_phant, ian_flatable,
    norm_al, catie_pillar, rob_ank, joy_stick, mary_go,
    tina_bopper, ian_tense, dee_veloper, tim_ber, may_day,
    glen_cove, hal_lowed, sam_wich, earl_ybird, rose_bud,
    ted_ebear, ella_vate, clara_net, violin_tunes, lee_der,
    crystal_ball, jenny_rator, perry_odic, sue_pernova,
    anna_lytics,jill_out, art_ist, rob_inhood,
    ella_vate, andy_gravity, anne_tenna, will_power,
    luke_out, sue_perb, ivan_idea, drew_paper, justin_time,
    pat_down, sonny_day, neil_down, bill_board, may_flowers, stan_dup,
    olive_branch, ella_ment, earl_gray, jack_pot, moe_tion,
    dale_ivery, pat_riotic, jenny_rate, rocky_road, steve_adore,
    ty_tanic, liz_tening, tom_orrow, ann_chovy, frank_furter,
    ray_sing, daisy_chain, brad_crumb, rose_bush, chip_munk, cliff_hanger, wendy_wind, cole_dmine,
    rocky_shore, crystal_ball, sandy_beach, bill_folds,
    terri_bull, barbie_cue, ty_tan, lou_minate, holly_day, phil_ter])

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
