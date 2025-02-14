CREATE TABLE `role` (
  `id` int PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `user` (
  `id` int PRIMARY KEY,
  `fullname` varchar(255),
  `email` varchar(255),
  `phone_number` varchar(255),
  `address` varchar(255),
  `role_id` int,
  `created_at` datetime,
  `updated_at` datetime
);

CREATE TABLE `category` (
  `id` int PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `court` (
  `id` int PRIMARY KEY,
  `category_id` int,
  `title` varchar(255),
  `price` int,
  `location` varchar(255),
  `discount` int,
  `thumbnail` varchar(255),
  `description` longtext,
  `created_at` datetime,
  `updated_at` datetime
);

CREATE TABLE `bookings` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `court_id` int,
  `booking_date` datetime,
  `duration` int
);

CREATE TABLE `feedback` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `court_id` int,
  `firstname` varchar(255),
  `lastname` varchar(255),
  `email` varchar(255),
  `phone_number` varchar(255),
  `subject_name` varchar(255),
  `note` varchar(255),
  `rating` int
);

CREATE TABLE `courtManager` (
  `id` int PRIMARY KEY,
  `court_id` int,
  `user_id` int,
  `fullname` varchar(255),
  `address` varchar(255),
  `email` varchar(255),
  `phone_number` varchar(255),
  `note` varchar(255),
  `order_date` datetime,
  `status` int
);

CREATE TABLE `courtstaff` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `court_id` int,
  `fullname` varchar(255),
  `email` varchar(255),
  `phone` varchar(255)
);

CREATE TABLE `payments` (
  `id` int PRIMARY KEY,
  `booking_id` int,
  `amount` varchar(255),
  `payment_date` datetime,
  `payment_method` enum,
  `payment_status` enum
);

ALTER TABLE `role` ADD FOREIGN KEY (`id`) REFERENCES `user` (`role_id`);

ALTER TABLE `category` ADD FOREIGN KEY (`id`) REFERENCES `court` (`category_id`);

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `bookings` (`user_id`);

ALTER TABLE `court` ADD FOREIGN KEY (`id`) REFERENCES `bookings` (`court_id`);

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `feedback` (`user_id`);

ALTER TABLE `court` ADD FOREIGN KEY (`id`) REFERENCES `feedback` (`court_id`);

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `courtstaff` (`user_id`);

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `courtManager` (`user_id`);

ALTER TABLE `bookings` ADD FOREIGN KEY (`id`) REFERENCES `payments` (`booking_id`);
