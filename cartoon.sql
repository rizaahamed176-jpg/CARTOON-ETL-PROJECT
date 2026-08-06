use testdb;
--testing all the data from cartoons--
select* from cartoons

--top 5 cartoons--
select top 5* from cartoons;

--top 10 highest cartoons-- 
select top 10 name,rating from cartoons 
order by rating desc

--how many high and average show cartoons 

select rating_category,count(*) as total_shows
from cartoons group by rating_category

--all the average show--
select name,rating_category from cartoons where 
rating_category='average'

--high rating show with dense_rank window function--
SELECT name,rating_category,DENSE_RANK() OVER(partition  BY rating_category order by name) AS rank_value
FROM cartoons
WHERE rating_category = 'high';

--top 3 least rated show--
select top 3 name,rating_category as least_performance from cartoons 
where rating_category='average'

--top 1 highest rating show--
select top 1 * from cartoons where rating > 9;

--top 1 lowest rating show--
select top 1 * from cartoons 
where rating in (select top 1 rating from cartoons order by rating asc)




