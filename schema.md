Table Users {
  user_id int [pk, increment]
  username varchar
  email varchar [unique]
  password_hash varchar
  address varchar
  phone varchar
  profile_image varchar
  created_at datetime
  updated_at datetime
}

Table Dishes {
  dish_id int [pk, increment]
  name varchar
  description varchar
  image_url varchar
  price float
  category_id int [ref: > Categories.category_id]
  created_at datetime
  updated_at datetime
}

Table Categories {
  category_id int [pk, increment]
  name varchar
  description varchar
}

Table Orders {
  order_id int [pk, increment]
  user_id int [ref: > Users.user_id]
  total_price float
  order_date datetime
  delivery_address varchar
  status varchar
  created_at datetime
  updated_at datetime
}

Table OrderDetails {
  order_id int [ref: > Orders.order_id]
  dish_id int [ref: > Dishes.dish_id]
  quantity int
  subtotal_price float
  Primary Key (order_id, dish_id)
}

Table Reviews {
  review_id int [pk, increment]
  user_id int [ref: > Users.user_id]
  dish_id int [ref: > Dishes.dish_id]
  rating int
  comment varchar
  review_date datetime
  created_at datetime
  updated_at datetime
}

Table Admins {
  admin_id int [pk, increment]
  username varchar
  password_hash varchar
  created_at datetime
  updated_at datetime
}


![Alt text](image.png)
