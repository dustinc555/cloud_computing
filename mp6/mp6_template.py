import json
import sys
import logging
import redis
import pymysql

DB_HOST = (
    "auroradb-instance-1.cng2ee2uu1yg.us-east-1.rds.amazonaws.com"  # Add DB end point
)
DB_USER = "admin"  # Add your database user
DB_PASS = "19191919"  # Add your database password
DB_NAME = "mp6database"  # Add your database name
DB_TABLE = "mp6table"  # Add your table name
REDIS_URL = "mp6-redis-cluser-ro.ginmqt.ng.0001.use1.cache.amazonaws.com"  # Add redis end point "redis://<end point>"

TTL = 60


class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)

        self.mysql = pymysql.connect(**params)

    def query(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def record(self, sql, values):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql, values)
            return cursor.fetchone()

    def get_idx(self, table_name):
        with self.mysql.cursor() as cursor:
            cursor.execute(f"SELECT MAX(id) as id FROM {table_name}")
            idx = str(cursor.fetchone()["id"] + 1)
            return idx

    def insert(self, idx, data, table_name):
        with self.mysql.cursor() as cursor:
            hero = data["hero"]
            power = data["power"]
            name = data["name"]
            xp = data["xp"]
            color = data["color"]

            sql = f"INSERT INTO {table_name} (`id`, `hero`, `power`, `name`, `xp`, `color`) VALUES ('{idx}', '{hero}', '{power}', '{name}', '{xp}', '{color}')"
            cursor.execute(sql)
            self.mysql.commit()


# TODO 2
def read(use_cache, xps, Database, Cache):
    result = []

    if use_cache:  # Use cache
        for xp in xps:
            cached_result = Cache.get(xp)
            if cached_result:
                result.append(json.loads(cached_result.decode("utf-8")))
            else:
                db_result = Database.query(
                    f"SELECT * FROM {DB_TABLE} WHERE xp = '{xp}'"
                )
                if db_result:
                    result.append(db_result[0])
                    Cache.setex(xp, TTL, json.dumps(db_result[0]))
    else:  # Do not use cache
        for xp in xps:
            db_result = Database.query(f"SELECT * FROM {DB_TABLE} WHERE xp = '{xp}'")
            if db_result:
                result.append(db_result[0])

    return result


# TODO 3
def write(use_cache, sqls, Database, Cache):
    if use_cache:  # Use cache
        for sql in sqls:
            idx = Database.get_idx(DB_TABLE)
            data = json.loads(sql)
            Database.insert(idx, data, DB_TABLE)
            Cache.setex(data["xp"], TTL, sql)
    else:  # Do not use cache
        for sql in sqls:
            idx = Database.get_idx(DB_TABLE)
            data = json.loads(sql)
            Database.insert(idx, data, DB_TABLE)


def lambda_handler(event, context):

    USE_CACHE = event["USE_CACHE"] == "True"
    REQUEST = event["REQUEST"]

    # Initialize database
    try:
        Database = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()

    # Initialize cache
    Cache = redis.Redis.from_url(REDIS_URL)

    result = []
    if REQUEST == "read":
        # event["SQLS"] is a list of all xps for which you have to query the database or redis.
        result = read(USE_CACHE, event["SQLS"], Database, Cache)

    elif REQUEST == "write":
        # event["SQLS"] should be a list of jsons. You have to write these rows to the database.
        write(USE_CACHE, event["SQLS"], Database, Cache)
        result = "write success"

    return {"statusCode": 200, "body": result}
