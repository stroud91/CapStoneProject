from app.models import db, BusinessImage, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_b_images():
    italian_one_previmage = BusinessImage(
        image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783348.jpg",
        alt_text="Italian Food",
        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    italian_two_previmage = BusinessImage(
        image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783349.jpg",
        alt_text="Italian Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    italian_three_previmage = BusinessImage(
        image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783347.jpg",
        alt_text="Italian Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    italian_four_previmage = BusinessImage(
        image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783346.jpg",
        alt_text="Italian Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    italian_five_previmage = BusinessImage(
        image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783345.jpg",
        alt_text="Italian Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    italian_six_previmage = BusinessImage(
        image_url="https://www.foodrepublic.com/img/gallery/100-italian-fooddrink-words-and-phrases/l-intro-1684783340.jpg",
        alt_text="Italian Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    mexican_one_previmage = BusinessImage(
        image_url="https://media.timeout.com/images/100292153/750/562/image.jpg",
        alt_text="Mexican Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    mexican_two_previmage = BusinessImage(
        image_url="https://media.timeout.com/images/100292153/750/563/image.jpg",
        alt_text="Mexican Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    mexican_three_previmage = BusinessImage(
        image_url="https://media.timeout.com/images/100292153/750/564/image.jpg",
        alt_text="Mexican Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    mexican_four_previmage = BusinessImage(
        image_url="https://media.timeout.com/images/100292153/750/561/image.jpg",
        alt_text="Mexican Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    mexican_five_previmage = BusinessImage(
        image_url="https://media.timeout.com/images/100292153/750/560/image.jpg",
        alt_text="Mexican Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    mexican_six_previmage = BusinessImage(
        image_url="https://media.timeout.com/images/100292153/750/565/image.jpg",
        alt_text="Mexican Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    mexican_seven_previmage = BusinessImage(
        image_url="https://media.timeout.com/images/100292153/750/567/image.jpg",
        alt_text="Mexican Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    middleast_one_previmage = BusinessImage(
        image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361114.jpeg",
        alt_text="Middle Eastern Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    middleast_two_previmage = BusinessImage(
        image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361115.jpeg",
        alt_text="Middle Eastern Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    middleast_three_previmage = BusinessImage(
        image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361116.jpeg",
        alt_text="Middle Eastern Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    middleast_four_previmage = BusinessImage(
        image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361117.jpeg",
        alt_text="Middle Eastern Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    middleast_five_previmage = BusinessImage(
        image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361118.jpeg",
        alt_text="Middle Eastern Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    middleast_six_previmage = BusinessImage(
        image_url="https://shef.com/homemade-food/wp-content/uploads/lebanese-mezze-middle-eastern-food-scaled-e1662414361119.jpeg",
        alt_text="Middle Eastern Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    jap_one_previmage = BusinessImage(
        image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan.jpg",
        alt_text="Japanese Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    jap_two_previmage = BusinessImage(
        image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan1.jpg",
        alt_text="Japanese Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    jap_three_previmage = BusinessImage(
        image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan2.jpg",
        alt_text="Japanese Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    jap_four_previmage = BusinessImage(
        image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan3.jpg",
        alt_text="Japanese Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    jap_five_previmage = BusinessImage(
        image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan4.jpg",
        alt_text="Japanese Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    jap_six_previmage = BusinessImage(
        image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan5.jpg",
        alt_text="Japanese Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    jap_seven_previmage = BusinessImage(
        image_url="https://www.swedishnomad.com/wp-content/images/2018/09/yakitori-Classic-food-Japan6.jpg",
        alt_text="Japanese Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    american_one_previmage = BusinessImage(
        image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca8.jpg",
        alt_text="American Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    american_two_previmage = BusinessImage(
        image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca7.jpg",
        alt_text="American Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    american_three_previmage = BusinessImage(
        image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca88.jpg",
        alt_text="American Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    american_four_previmage = BusinessImage(
        image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca9.jpg",
        alt_text="American Food",
        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    american_five_previmage = BusinessImage(
        image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca10.jpg",
        alt_text="American Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    american_six_previmage = BusinessImage(
        image_url="https://www.tasteatlas.com/images/toplistarticles/08c818739e4b48ce96d319c16f4cc0ca77.jpg",
        alt_text="American Food",


        created_at=datetime.datetime.now(),
        uploaded_at=datetime.datetime.now()
    )

    # Add to session and commit
    db.session.add_all([
        italian_one_previmage, italian_two_previmage, italian_three_previmage,
        italian_four_previmage, italian_five_previmage, italian_six_previmage,
        mexican_one_previmage, mexican_two_previmage, mexican_three_previmage,
        mexican_four_previmage, mexican_five_previmage, mexican_six_previmage, mexican_seven_previmage,
        middleast_one_previmage, middleast_two_previmage, middleast_three_previmage,
        middleast_four_previmage, middleast_five_previmage, middleast_six_previmage,
        jap_one_previmage,  jap_two_previmage, jap_three_previmage, jap_four_previmage, jap_five_previmage,
        jap_six_previmage, jap_seven_previmage, american_one_previmage,
        american_two_previmage, american_three_previmage, american_four_previmage, american_five_previmage, american_six_previmage
    ])
    db.session.commit()

# For undoing
def undo_b_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.businessimages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM businessimages"))
    db.session.commit()
