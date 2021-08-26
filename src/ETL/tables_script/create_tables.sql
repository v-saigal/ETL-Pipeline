/*
Product side
*/

CREATE TABLE IF NOT EXISTS product_name(
    product_name_id SERIAL NOT NULL,
    product_name VARCHAR UNIQUE NOT NULL,
    PRIMARY KEY(product_name_id)
);

CREATE TABLE IF NOT EXISTS size(
    size_id SERIAL NOT NULL,
    size_name VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY(size_id)
);

CREATE TABLE IF NOT EXISTS product_detail (
    product_detail_id SERIAL NOT NULL,
    size_id INT references size(size_id) NOT NULL,
    product_name_id INT references product_name(product_name_id) NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY(product_detail_id)
);

/*
Transaction side
*/

CREATE TABLE IF NOT EXISTS payment_type(
    payment_type_id SERIAL NOT NULL,
    method VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY(payment_type_id)
);

CREATE TABLE IF NOT EXISTS branch(
    branch_id SERIAL NOT NULL,
    location VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY(branch_id)
);

CREATE TABLE IF NOT EXISTS card_type(
    card_type_id SERIAL NOT NULL,
    type VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY(card_type_id)
);

CREATE TABLE IF NOT EXISTS transaction(
    transaction_id SERIAL NOT NULL,
    payment_type_id INT references payment_type(payment_type_id) NOT NULL,
    branch_id INT references branch(branch_id) NOT NULL,
    card_type_id INT references card_type(card_type_id) NOT NULL,
    time_stamp  TIMESTAMP ,
    total_price FLOAT NOT NULL,
    PRIMARY KEY(transaction_id)
);

/*
Transaction side
*/

CREATE TABLE IF NOT EXISTS basket(
    transaction_id INT references transaction(transaction_id) NOT NULL,
    product_detail_id INT references product_detail(product_detail_id) NOT NULL,
    quantity INT NOT NULL
);