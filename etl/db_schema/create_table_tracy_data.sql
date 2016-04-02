CREATE TABLE "public"."tracy_data" (
	"key_key" varchar(40) NOT NULL,
	"company" varchar(255),
	"team" varchar(255),
	"num_female_eng" int8,
	"num_eng" int8,
	"percent_female_eng" float8,
	"last_updated" date,
	"created_at" timestamp,
	"term_at" timestamp,
	"sha_commit" varchar(255),
	PRIMARY KEY ("key_key")
);