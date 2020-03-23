# Problem 2

- I initially Select all the PersonId1 from friends and union all the PersonId2 from friends. I give this subquery a name called P.

- Then, I inner join people table and P table on the P's PersonId1 column and people's PersonId column

- Group by the name of people's table

- Select out the Name of people table and Count(PersonId1) as NumOfFriends

- Order the table in nonascending order based on the NumOfFriends column

The reason I use inner join is that I only want to join the intersection between the two tables.
For example, if there is a PersonId in the subquery table P and a matching PersonId in people, then I want to match the two.
