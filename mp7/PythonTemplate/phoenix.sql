!outputformat tsv

CREATE VIEW IF NOT EXISTS "powers" (
    "pk" VARCHAR PRIMARY KEY,
    "personal"."hero" VARCHAR,
    "personal"."power" VARCHAR,
    "professional"."name" VARCHAR,
    "professional"."xp" VARCHAR,
    "custom"."color" VARCHAR
);

SELECT p1."name" AS "Name1",
       p2."name" AS "Name2",
       p1."power" AS "Power"
FROM "powers" p1 
INNER JOIN "powers" p2
ON p1."power" = p2."power"
WHERE p1."hero" = 'yes' AND p2."hero" = 'yes';