-- Question 1:
SELECT cat_id FROM pet_shop.cats;

-- Quesion 2:
SELECT name, breed FROM pet_shop.cats;

-- Question 3:
SELECT name, age FROM pet_shop.cats WHERE breed = 'Tabby';

-- Question 4:
SELECT cat_id, age FROM pet_shop.cats WHERE age = cat_id;