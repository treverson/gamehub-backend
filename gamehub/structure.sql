create table game (
	id integer auto_increment,
	description varchar(100),
	publicKey varchar(64),
	primary key (id)
);

create table score (
	id integer auto_increment,
	idGame integer,
	score decimal(10, 2),
	`timestamp` datetime,
	primary key (id)
);