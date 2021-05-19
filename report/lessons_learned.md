
# Lesson Learned

## Communications

The team had a pretty rough start going into the project. We didn't know each other, our schedules, skills or experience levels. It turned out to be quite a roadblock throughout the entire course. We experienced a lot of miscommunication and times with no communication at all, which would result in tasks being completed twice, tasks not being met at all and group members working alone on a big task.

Because of the lack of communication, we created quite a backlog throughout the course. We did, at one point, create a technical debt on the API, which meant that a group member had to work on the CI/CD and docker alone.

We should have started by getting to know each other and match our expectations for the project. We had many different backgrounds; three were writing their bachelor, and four had a job taking up time. It meant that we should have focused a lot more time discussing schedules and meetings, not meeting odd hours every week. By focusing more time on this, we could have gone into the project with a better foundation and possibly a better end product. It would probably have been a good idea to give each group member a role and a responsibility and then actively use a kanban board, so everybody knows what is going on and what is missing.


## Tool Choice

With the lack of communication came some bad choices. We chose to go with a framework that only one group member knew, which meant that the rest of the group had to use a lot of time getting to know the structure and functionalities.

Django is an extensive scale framework. It has a large amount of implemented functionality; easy database management, easy implementation of views and pages, authentications tools and security features. It is all beneficial when you use it as a large scale API framework. We ran into the problem here because our project didn't take advantage of these features the way it was meant. Django turned out to be unmanageable for inexperienced users due to the high complexity of the innate features.

We should have started discussing several choices, including prices in the long run, for the whole tech stack and the team members prior work with these.

## Technical Debt

The team didn't use enough time going through and testing the individual pull request, which meant that we spent a lot of time looking into minor errors that ...

When the simulator started, we already had a backlog, resulting in our product not being ready for the simulator. It meant that some register request already failed the first day, resulting in a future error on message and follow request. The team should have focused a lot more time on getting the project ready for the simulator and avoiding future mistakes. 

Later in the project, we decided to try and implement docker swarm. It took a lot of time and looking back. We probably shouldn't have chosen the more complex implementation when we already had quite a significant backlog. We did learn a lot from working with docker swarm, and in the end, it was worth it to get it up and run for the learning experience.

Our technical debt included a couple of errors from former tasks. It took a lot of time to find these and fix them. We should have focused more time on getting the logging system up and running so that we had a tool to help us in these cases.

## Database 

So a significant roadblock has been to migrate the database two times to a new host with minimal downtime and minimal data loss. We could have made a dump of the minitwit database with `pg_dump`; however, then we would manually have to download the dump, transfer it to a new host, write the `INSERT and UPDATE` queries and so on, which would be time-consuming and result in a more extensive loss of data. But we ended up using the (postgres_fwd)[https://www.postgresql.org/docs/9.5/postgres-fdw.html], which is a foreign-data wrapper that can make a real-time/live connection to another database. The only problem was that we had to write an `INSERT` query that would get the data and make sure that the relationship between the entities in the different tables wouldn't be broken. To do so, we took every id from the "old" database and made them negative, so when a new entity is created in the "new" database, the id will not conflict with the "old" id's.

However, this created a new issue when we had to migrate the database once again. We could not use the same strategy again. We could probably just have done it with the same strategy and added the length of the table to the ID, but that is a hacky fix that would hit us hard in the future. After a lot of thinking, we decided to take a snapshot of the droplet and recreating it in another droplet which was by far t easiest solution, and we lost some data since the DB was down for about 40 minutes. With that knowledge now, we would have chosen to use Digital Ocean's Managed Database Cluster, saving us **a lot** of trouble in this project.
