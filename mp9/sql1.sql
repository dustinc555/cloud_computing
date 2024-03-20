SELECT Airline, Origin_Airport, Destination_Airport
FROM "AwsDataCatalog"."mp9-database"."gluejob2"
WHERE month = 12
    AND day = 25
    AND scheduled_departure >= 800
    AND scheduled_departure < 1200
    AND origin_airport = 'ORD';