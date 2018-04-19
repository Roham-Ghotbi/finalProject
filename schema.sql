drop table if exists users;
create table users(
	user_id integer primary key,
	email text not null,
	first_name text not null,
	last_name text not null,
	password text not null
);

drop table if exists projects;
create table projects(
	project_id integer primary key,
	project_name text not null,
	description text not null,
	due_date text,
	user_id integer not null, 
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

drop table if exists actions;
create table actions(
	action_id integer primary key,
	action_name text not null,
	description text,
	due_date text,
	project_id integer not null, 
	FOREIGN KEY(project_id) REFERENCES projects(project_id)
);