-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema
.tables
.schema crime_scene_reports
select description from crime_scene_reports;   -- report no. 7 from below is the case of missing duck


-- DESCRIPTION: Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time
-- each of their interview transcripts mentions the bakery.


select id from crime_scene_reports;   -- id of the case is 295
select year from crime_scene_reports where id = 295;   -- year: 2021
select month from crime_scene_reports where id = 295;   -- month: 7
select day from crime_scene_reports where id = 295;   -- day: 28
select street from crime_scene_reports where id = 295;   -- street: Humphrey Street

-- Investigating what happened on that day in the bakery.
select activity from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and min <= 16;   -- exit
-- we see on 16th min someone left. and 15th min it was stolen let's see who left.
select id from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and min <= 16;
-- id is 260
select license_plate from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and min <= 16;
-- his license plate id is 5P2BI95
-- let's go into people to see whose car it was
.schema people
select name from people where license_plate = '5P2BI95'
-- HER name is Vanessa.
-- Let's see if she was mentioned in someway in the interviews
.schema interviews
select transcript from interviews where name = 'Vanessa';
-- THERE's no reference of Vanessa guess we need a different approach
-- Let's see if all those who entered left at that time.
select name from people
join bakery_security_logs on  bakery_security_logs.license_plate = people.license_plate
where year = 2021 and day = 28 and month = 7 and hour >= 9 and hour <= 10 and minute <= 25 and minute >= 15 and activity = 'exit';
-- according to the interviews the criminal is from these people lets now check if any of them made a withdrawal that day
select name from people
join bank_accounts on person_id = people.id
join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
where atm_location = 'Leggett Street' and day = 28 and month = 7 and year = 2021 and transaction_type = 'withdraw';
-- Here we go now we see progress the list of suspects have shortened down to 4 LUCA IMAN BRUCE DIANA.. Let's continue
-- Now let's see the 4 people's call logs
select distinct name from people
join phone_calls on people.phone_number = phone_calls.receiver
where phone_number in
(select receiver from phone_calls
join people on phone_calls.caller = people.phone_number
where duration <= 60 and year = 2021 and month = 7 and day = 28
and caller in(select phone_number from people where name in('Bruce', 'Iman', 'Diana', 'Luca')));
-- we can now see that there were two people who were called namely Robin and Philip. So, we know the helper is among these two guys.
-- GREAT Progress.
select passport_number from people where name = 'Robin' and name = 'Philip';

-- Umm something is fishy.. I can't seem to find the passport number for Robin.. SEEMS odd let's dive in more
-- Now let's check which flights are available on 29th as they were leaving tomorrow.
select id from flights where day = 29 and month = 7 and year = 2021 and origin_airport_id = 8;

-- Now we have the flights let's see the passangers.
select flight_id from passangers where passport_number = 3391710505;
-- We cannot see any ticket with his passport number.
-- Let's see which of the 4 suspects have a flight on that day.
select flight_id from passengers where passport_number in (select passport_number from people where name in ('Diana', 'Iman', 'Bruce', 'Luca'));
-- 18 23 36 43 53 These flights will be taking off on 29th with flight id 18 being earliest.
-- 11, 18, 24, 26, 36, 36, 48, 54. We can see two people with the same flight id.. WERE CLOSING IN..
select passport_number from passengers where passport_number in (select passport_number from people where name in ('Diana', 'Iman', 'Bruce', 'Luca')) and flight_id = 36;
-- BUSTED!
SELECT name from people where passport_number = 5773159633 or passport_number = 8496433585;
-- Luca along with Bruce.
-- Let's see where are they Going
select destination_airport_id from flights where id = 36;
SELECT city FROM airports WHERE id = 4;
-- HE is fleeing to New York City.


-- Wait a moment if accomplice is Robin there must be a single thief and one of Luca or Bruce not both.
-- All 4 of the suspects left the place in the 10 min. time frame
-- Let's see call logs of Luca and Bruce.
select receiver from phone_calls
join people on phone_calls.caller = people.phone_number
where name = 'Luca' and duration <= 60 and year = 2021 and month = 7 and day = 28;

-- We can see Luca has no call logs.. GOTCHA Bruce
select receiver from phone_calls
join people on phone_calls.caller = people.phone_number
where name = 'Bruce' and duration <= 60 and year = 2021 and month = 7 and day = 28;

-- HERE we get the receiver.. (375) 555-8161
-- Let's check if this is Robin.
select name from people where phone_number
in (select receiver from phone_calls join people on phone_calls.caller = people.phone_number
where name = 'Bruce' and duration <= 60 and year = 2021 and month = 7 and day = 28);


-- I GOT him this Time: That's it for you "Robin" and "Bruce".
-- Let's Test if I was right.