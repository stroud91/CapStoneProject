from app.models import db, Dish, Business, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_dishes():

    # Dishes for "Rita's Italian Ice & Frozen Custard"
    dish1 = Dish(
        business_id=1,
        name="Vanilla Italian Ice",
        description="Smooth and creamy classic vanilla flavor.",
        image_id=None,
        price=4.50,
        category_id=None,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    dish2 = Dish(
        business_id=1,
        name="Chocolate Frozen Custard",
        description="Rich and indulgent frozen custard with deep chocolate flavor.",
        image_id=None,
        price=5.00,
        category_id=None,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    # Dishes for "Bella's Bagels"
    dish3 = Dish(
        business_id=2,
        name="Classic Plain Bagel",
        description="A classic plain bagel, crispy on the outside and soft on the inside.",
        image_id=None,
        price=1.50,
        category_id=None,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    dish4 = Dish(
        business_id=2,
        name="Bagel with Cream Cheese",
        description="A delicious bagel slathered with creamy cheese.",
        image_id=None,
        price=2.50,
        category_id=None,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    # Dishes for "Gaspare's Pizza House & Italian Restaurant"
    dish5 = Dish(
        business_id=3,
        name="Margherita Pizza",
        description="Classic pizza with fresh tomatoes, mozzarella, and basil.",
        image_id=None,
        price=14.99,
        category_id=None,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    dish6 = Dish(
        business_id=3,
        name="Spaghetti Carbonara",
        description="Classic Italian pasta dish with bacon, egg, and cheese.",
        image_id=None,
        price=13.99,
        category_id=None,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    # Dishes for "Roma Antica"
    dish7 = Dish(
    business_id=4,
    name="Penne Arrabbiata",
    description="Penne pasta in a spicy tomato sauce with garlic and chili peppers.",
    image_id=None,
    price=12.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish8 = Dish(
    business_id=4,
    name="Fettuccine Alfredo",
    description="Creamy pasta dish made with fettuccine and rich alfredo sauce.",
    image_id=None,
    price=14.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "The Italian Homemade Company"
    dish9 = Dish(
    business_id=5,
    name="Tiramisu",
    description="Classic Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cheese.",
    image_id=None,
    price=6.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish10 = Dish(
    business_id=5,
    name="Ravioli",
    description="Homemade pasta filled with ricotta cheese and spinach, served with tomato sauce.",
    image_id=None,
    price=15.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Fiorella - Sunset"
    dish11 = Dish(
    business_id=6,
    name="Quattro Formaggi Pizza",
    description="Four cheese pizza with mozzarella, gorgonzola, parmesan, and ricotta.",
    image_id=None,
    price=16.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish12 = Dish(
    business_id=6,
    name="Calzone",
    description="Folded pizza filled with cheese, ham, and mushrooms.",
    image_id=None,
    price=14.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Cielito Lindo"
    dish13 = Dish(
    business_id=7,
    name="Taco Al Pastor",
    description="Tacos filled with marinated pork, pineapple, and cilantro.",
    image_id=None,
    price=3.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish14 = Dish(
    business_id=7,
    name="Guacamole",
    description="Freshly made guacamole with ripe avocados, tomatoes, onions, and cilantro.",
    image_id=None,
    price=5.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Sunset Cantina"
    dish15 = Dish(
    business_id=8,
    name="Chicken Enchiladas",
    description="Tortillas filled with seasoned chicken and topped with red chili sauce and cheese.",
    image_id=None,
    price=12.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish16 = Dish(
    business_id=8,
    name="Churros",
    description="Deep-fried dough pastries, dusted with sugar and served with chocolate dipping sauce.",
    image_id=None,
    price=5.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    # Dishes for "Otra"
    dish17 = Dish(
    business_id=9,
    name="Taco de Chorizo",
    description="Soft tortillas filled with spicy Mexican sausage, topped with onions and cilantro.",
    image_id=None,
    price=3.25,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish18 = Dish(
    business_id=9,
    name="Ceviche Tostada",
    description="Fresh seafood marinated in citrus juices, mixed with tomatoes, onions, and cilantro. Served on a crispy tostada.",
    image_id=None,
    price=9.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Santeria"
    dish19 = Dish(
    business_id=10,
    name="Mole Enchiladas",
    description="Chicken-filled tortillas smothered in rich mole sauce, topped with sesame seeds.",
    image_id=None,
    price=12.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish20 = Dish(
    business_id=10,
    name="Tamales",
    description="Steamed corn dough filled with seasoned pork, served with salsa on the side.",
    image_id=None,
    price=10.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "El Farolito"
    dish21 = Dish(
    business_id=11,
    name="Super Burrito",
    description="Large flour tortilla filled with rice, beans, cheese, guacamole, and choice of meat.",
    image_id=None,
    price=9.75,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish22 = Dish(
    business_id=11,
    name="Quesadilla Suiza",
    description="Large grilled tortilla filled with melted cheese, meat, and served with guacamole and sour cream.",
    image_id=None,
    price=8.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Caliente Bistro Kitchen"
    dish23 = Dish(
    business_id=12,
    name="Chili Relleno",
    description="Fried poblano pepper stuffed with cheese, served in tomato sauce.",
    image_id=None,
    price=10.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish24 = Dish(
    business_id=12,
    name="Sopa de Tortilla",
    description="Traditional Mexican tortilla soup with chicken, tomatoes, and avocado.",
    image_id=None,
    price=7.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish25 = Dish(
    business_id=12,
    name="Nachos Supreme",
    description="Tortilla chips topped with cheese, beans, jalapenos, sour cream, guacamole, and choice of meat.",
    image_id=None,
    price=9.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish26 = Dish(
    business_id=12,
    name="Carnitas Tacos",
    description="Soft tacos filled with slow-cooked pork, onions, and cilantro.",
    image_id=None,
    price=8.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    # Dishes for "Mazra"
    dish27 = Dish(
    business_id=13,
    name="Shawarma Platter",
    description="Grilled spiced meat, served with rice, pita, and a side of tahini sauce.",
    image_id=None,
    price=14.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish28 = Dish(
    business_id=13,
    name="Hummus Bowl",
    description="Creamy chickpea spread, topped with olive oil and served with pita bread.",
    image_id=None,
    price=7.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Beit Rima"
    dish29 = Dish(
    business_id=14,
    name="Falafel Plate",
    description="Crispy chickpea balls, served with salad, pickles, and tahini sauce.",
    image_id=None,
    price=12.75,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish30 = Dish(
    business_id=14,
    name="Mujaddara",
    description="A mix of lentils, rice, and caramelized onions, served with a side of yogurt.",
    image_id=None,
    price=10.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Abu Salim Middle Eastern Grill"
    dish31 = Dish(
    business_id=15,
    name="Kebab Combo",
    description="A combination of chicken and beef skewers, grilled to perfection, served with rice and salad.",
    image_id=None,
    price=15.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish32 = Dish(
    business_id=15,
    name="Baba Ganoush",
    description="Smoky roasted eggplant spread, blended with tahini and spices, served with pita.",
    image_id=None,
    price=8.25,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Beit Rima (86 Carl St)"
    dish33 = Dish(
    business_id=16,
    name="Stuffed Grape Leaves",
    description="Grape leaves filled with rice and herbs, served with yogurt dip.",
    image_id=None,
    price=9.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish34 = Dish(
    business_id=16,
    name="Za'atar Manakeesh",
    description="Flatbread topped with za'atar spice blend and olive oil, baked until crispy.",
    image_id=None,
    price=7.75,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish35 = Dish(
    business_id=16,
    name="Fattoush Salad",
    description="Mixed salad with tomatoes, cucumbers, onions, and crispy pita chips, dressed in lemon and olive oil.",
    image_id=None,
    price=8.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    # Dishes for "Reems"
    dish36 = Dish(
    business_id=17,
    name="Spinach Fatayer",
    description="Savory pastry filled with a mix of spinach, onions, and sumac.",
    image_id=None,
    price=5.25,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish37 = Dish(
    business_id=17,
    name="Ka'ak Bread",
    description="Traditional street bread, topped with sesame seeds, perfect for sandwiches or dips.",
    image_id=None,
    price=3.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Old Jerusalem Restaurant"
    dish38 = Dish(
    business_id=18,
    name="Chicken Shawarma Plate",
    description="Marinated and grilled chicken, thinly sliced, served with rice, hummus, and salad.",
    image_id=None,
    price=14.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish39 = Dish(
    business_id=18,
    name="Mansaf",
    description="Traditional dish made with lamb cooked in a yogurt sauce, served over rice.",
    image_id=None,
    price=16.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Shoshin Sushi"
    dish40 = Dish(
    business_id=19,
    name="Nigiri Platter",
    description="Assorted fish over pressed rice. Chef's selection.",
    image_id=None,
    price=21.00,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish41 = Dish(
    business_id=19,
    name="Dragon Roll",
    description="Eel, cucumber, and avocado roll topped with thin slices of avocado.",
    image_id=None,
    price=13.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Yuji"
    dish42 = Dish(
    business_id=20,
    name="Udon Soup",
    description="Thick noodles in a flavorful broth, topped with green onions and tempura bits.",
    image_id=None,
    price=10.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish43 = Dish(
    business_id=20,
    name="Teriyaki Chicken Bowl",
    description="Grilled chicken glazed with teriyaki sauce, served over rice with steamed vegetables.",
    image_id=None,
    price=12.75,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish44 = Dish(
    business_id=20,
    name="Tempura Platter",
    description="Assortment of deep-fried vegetables and shrimp, served with a dipping sauce.",
    image_id=None,
    price=14.25,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)


    # Dishes for "Japateam Sushi"
    dish45 = Dish(
    business_id=21,
    name="Salmon Sashimi",
    description="Fresh slices of raw salmon, served with wasabi and soy sauce.",
    image_id=None,
    price=12.00,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish46 = Dish(
    business_id=21,
    name="Miso Ramen",
    description="Noodle soup with a miso-flavored broth, topped with pork slices, bamboo shoots, and egg.",
    image_id=None,
    price=14.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Bento Peak"
    dish47 = Dish(
    business_id=22,
    name="Chicken Katsu Bento",
    description="Crispy breaded chicken cutlet served with rice, salad, and pickled vegetables.",
    image_id=None,
    price=13.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish48 = Dish(
    business_id=22,
    name="Tempura Udon",
    description="Thick noodles in a clear broth, served with shrimp and vegetable tempura on the side.",
    image_id=None,
    price=12.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Nara Restaurant & Sake Bar"
    dish49 = Dish(
    business_id=23,
    name="Tuna Tataki",
    description="Lightly seared tuna slices with a citrusy ponzu sauce.",
    image_id=None,
    price=14.00,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish50 = Dish(
    business_id=23,
    name="Nara Special Roll",
    description="Sushi roll with crab, avocado, and cucumber, topped with seared salmon and a special sauce.",
    image_id=None,
    price=16.00,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Izakaya Mayumi"
    dish51 = Dish(
    business_id=24,
    name="Grilled Skewers Platter",
    description="Assorted skewers of meat and vegetables, grilled to perfection.",
    image_id=None,
    price=18.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish52 = Dish(
    business_id=24,
    name="Sake-steamed Clams",
    description="Fresh clams steamed in sake, infused with the flavors of garlic and herbs.",
    image_id=None,
    price=15.25,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)


    # More dishes for "Izakaya Mayumi"
    dish53 = Dish(
    business_id=24,
    name="Shoyu Ramen",
    description="Soy sauce based broth with pork belly, egg, and bamboo shoots.",
    image_id=None,
    price=14.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish54 = Dish(
    business_id=24,
    name="Spicy Tuna Roll",
    description="Sushi roll with spicy tuna mixture, cucumber, and topped with sesame seeds.",
    image_id=None,
    price=9.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Hard Rock Cafe"
    dish55 = Dish(
    business_id=25,
    name="Classic Cheeseburger",
    description="Juicy beef patty with cheddar cheese, lettuce, and tomato on a toasted bun.",
    image_id=None,
    price=13.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish56 = Dish(
    business_id=25,
    name="Veggie Burger",
    description="Plant-based patty with lettuce, tomato, and a vegan mayo dressing.",
    image_id=None,
    price=12.00,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "The Garden Club"
    dish57 = Dish(
    business_id=26,
    name="Grilled Chicken Salad",
    description="Grilled chicken breast on a bed of fresh greens with vinaigrette.",
    image_id=None,
    price=10.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish58 = Dish(
    business_id=26,
    name="Pancake Stack",
    description="Fluffy pancakes served with maple syrup and butter.",
    image_id=None,
    price=8.99,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "The Snug"
    dish59 = Dish(
    business_id=27,
    name="Lobster Roll",
    description="Fresh lobster meat in a creamy mayo dressing on a toasted bun.",
    image_id=None,
    price=19.50,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish60 = Dish(
    business_id=27,
    name="Truffle Fries",
    description="Crispy fries seasoned with truffle oil and parmesan.",
    image_id=None,
    price=7.00,
    category_id=None,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)


    db.session.add_all([
    dish1, dish2, dish3, dish4, dish5, dish6,
    dish7, dish8, dish9, dish10, dish11, dish12,
    dish13, dish14, dish15, dish16, dish17, dish18,
    dish19, dish20, dish21, dish22, dish23, dish24,
    dish25, dish26, dish27, dish28, dish29, dish30,
    dish31, dish32, dish33, dish34, dish35, dish36,
    dish37, dish38, dish39, dish40, dish41, dish42,
    dish43, dish44, dish45, dish46, dish47, dish48,
    dish49, dish50, dish51, dish52, dish53, dish54,
    dish55, dish56, dish57, dish58, dish59, dish60
    ])

    db.session.commit()

def undo_dishes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.dishes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM dishes"))

    db.session.commit()
