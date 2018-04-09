drop table if exists users;
create table users(
	user_id integer primary key,
	username text not null,
	password integer not null
);

drop table if exists trips;
create table trips(
	trip_id integer primary key,
	trip_name text not null,
	destination text not null,
	owner_id integer not null, 
	friend_id integer not null, 
	FOREIGN KEY(owner_id) REFERENCES users(user_id),
	FOREIGN KEY(friend_id) REFERENCES users(user_id)
);
