INSERT INTO user(password, is_superuser, first_name, is_staff, is_active, date_joined, phone, last_name, gender, birth_day, email, username) VALUES ('qlalfqjsgh!', 0, 'dongwan', 0, 1, '2023-08-01 20:00:00', '010-1234-5678', 'yug', 'MA', '1995-03-06', 'yug6442@gmail.com', 'dongwan yug');

INSERT INTO addressbook(created_at, updated_at, profile, name, email, phone, company, memo, address, birthday, website, user_id, position) VALUES ('2023-08-01 20:00:00', '2023-08-01 20:00:00', 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', '홍길동', 'dwyug@gmail.com', '010-1263-4567', '가나다', '메모', '서울시 노원구', '1991-12-30', 'https://naver.com', 1, '주임');

INSERT INTO label(created_at, updated_at, name, user_id) VALUES ('2023-08-01 20:00:00', '2023-08-01 20:00:00', '대학교', 1);
INSERT INTO label(created_at, updated_at, name, user_id) VALUES ('2023-08-01 20:00:00', '2023-08-01 20:00:00', '중학교', 1);

INSERT INTO address_label(label_id, addressbook_id) VALUES (1, 1);
