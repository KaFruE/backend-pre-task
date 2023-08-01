CREATE TABLE user
(
    id           BIGINT AUTO_INCREMENT NOT NULL,
    password     VARCHAR(128) NOT NULL,
    last_login   DATETIME(6),
    is_superuser TINYINT(1)   NOT NULL,
    first_name   VARCHAR(150) NOT NULL,
    is_staff     TINYINT(1)   NOT NULL,
    is_active    TINYINT(1)   NOT NULL,
    date_joined  DATETIME(6)  NOT NULL,
    phone        VARCHAR(20)  NOT NULL,
    last_name    VARCHAR(30)  NOT NULL,
    gender       VARCHAR(2)   NOT NULL,
    birth_day    DATE         NOT NULL,
    email        VARCHAR(254) NOT NULL,
    username     VARCHAR(50),
    PRIMARY KEY(id),
    CONSTRAINT email UNIQUE (email),
    CONSTRAINT phone UNIQUE (phone)
);

CREATE TABLE addressbook
(
    id         BIGINT AUTO_INCREMENT NOT NULL,
    created_at DATETIME(6)  NOT NULL,
    updated_at DATETIME(6)  NOT NULL,
    profile    VARCHAR(200),
    name       VARCHAR(50)  NOT NULL,
    email      VARCHAR(254) NOT NULL,
    phone      VARCHAR(20)  NOT NULL,
    company    VARCHAR(20),
    memo       VARCHAR(150),
    address    VARCHAR(50),
    birthday   DATE,
    website    VARCHAR(200),
    user_id    BIGINT       NOT NULL,
    position   VARCHAR(20),
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE label
(
    id         BIGINT AUTO_INCREMENT NOT NULL,
    created_at DATETIME(6) NOT NULL,
    updated_at DATETIME(6) NOT NULL,
    name       VARCHAR(50) NOT NULL,
    user_id    BIGINT      NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE address_label
(
    id             BIGINT AUTO_INCREMENT NOT NULL,
    label_id       BIGINT NOT NULL,
    addressbook_id BIGINT,
    PRIMARY KEY(id),
    UNIQUE (label_id, addressbook_id),
    FOREIGN KEY (addressbook_id) REFERENCES addressbook (id),
    FOREIGN KEY (label_id) REFERENCES label (id)
);