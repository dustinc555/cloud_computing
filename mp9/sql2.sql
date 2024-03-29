SELECT f1.airline AS Airline,
       f1.origin_airport AS Origin_Airport,
       f1.destination_airport AS Stopover_Airport,
       f2.destination_airport AS Destination_Airport,
       f1.departure_delay AS Origin_Departure_Delay,
       f2.arrival_delay AS Stopover_Arrival_Delay,
       f2.departure_delay AS Stopover_Departure_Delay,
       f2.arrival_delay AS Destination_Arrival_Delay
FROM "AwsDataCatalog"."mp9-database"."gluejob2" f1
JOIN "AwsDataCatalog"."mp9-database"."gluejob2" f2 
    ON f1.destination_airport = f2.origin_airport
    AND f1.airline = f2.airline
WHERE ((f2.day * 24 * 60 + (f2.scheduled_departure / 100) * 60 + (f2.scheduled_departure % 100) + f2.departure_delay) - 
       (f1.day * 24 * 60 + (f1.scheduled_departure / 100) * 60 + (f1.scheduled_departure % 100) + f1.departure_delay + f1.elapsed_time + f1.time_zone_difference)) BETWEEN 60 AND 180
    AND f1.origin_airport = 'SFO'
    AND f2.destination_airport = 'JFK';
