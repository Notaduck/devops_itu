
# Lesson learned

## Commications

The team had a pretty rough start going into the project. We didn't know each other, our schedules, skills or experience levels. It turned out to be quite a roadblock throughout the entire course. We experienced a lot of miscommunication and times with no communication at all, which would result in tasks being completed twice, tasks not being met at all and group members working alone on a big task.

Because of the lack of communication, we created quite a backlog throughout the course. We did, at one point, create a technical debt on the API, which meant that a group member had to work on the CI/CD and docker alone.

We should have started by getting to know each other and match our expectations for the project. We had a lot of different backgrounds; three were writing their bachelor, and four had a job taking up time. It meant that we should have focused a lot more time discussing schedules and meetings, not meeting odd hours every week. By focusing more time on this, we could have gone into the project with a better foundation and possibly a better end product. It would probably have been a good idea to give each group member a role and a responsability and then activily use a kanban board so everybody know what is going on and what is missing.


## Tool choice

With the lack of communication came some bad choices. We chose to go with a framework that only one group member knew, which meant that the rest of the group had to use a lot of time getting to know the structure and functionalities.

Django is a large scale framework. It has a large amount of implemented functionality; easy database management, easy implementation of views and pages, authentications tools and security features. This is all very usefull when you use it as a large scale API framework, the problem we ran into here was that our project didn't take advantage of these features the way it was meant to. Django turned out to be unmanageable for inexperienced users due to the high complexity of the innate features.

We should have started out discussing several choices including prices on the long run, for the whole tech stack as well as the teammembers prior work with these.

## Technical debt

The team didn't use enough time going through and testing the individual pull request, which meant that we spent a lot of time looking into small errors that ...

When the simulator started, we already had a backlog resulting in our product not being ready for the simulator. This meant that some register request already failed the first day, resulting in future error on message and follow request. The team should have focused a lot more time into getting the project ready for the simulator together and thus avoiding future errors. 

Later in the project, we decided to try and implement docker swarm. This took a lot of time and looking back, we probably should'nt have chosen the harder implementation when we already had quite a big backlog. We did learn a lot from working with docker swarm and in the end it was really worth it to get it up and running for the learning experience.

Our technical debt included a couple of errors from former tasks. It took a lot of time to find these and fix them. We should have focused more time into getting the loggin system up and running for use, so that we actually had a tool to help us in these cases.

## Database 

So a big roadblock has been to migrate the database two times to a new host with minimal downtime and minimal data loss. We could simply have made a dump of the minitwit database with `pg_dump` however then we would manually have to download the dump, transfer it to a new host, write the `INSERT and UPDATE` queries and so on which would be time consuming and result in a larger loss of data. But we ended up using the (postgres_fwd)[https://www.postgresql.org/docs/9.5/postgres-fdw.html] which is a foreign data wrapper that can make a real-time/live connection to another database. The only problem was that we had to write a `INSERT` query which would get the data and make sure that the relationship between the eneities in the different tables wouldnt be broken. To do so we took every id from the "old" database and made them negative so when a new entity is created in the "new" database the id would not conflict with the "old" id's.  
However, this created a new issue when we had to migrate the database once again, we could not use the same strategy again. We could probably just have done it with the same strategy and added the length of the table to the ID, but that is a hacky fix which would hit us hard in the future. After a lot of thinking we simply decided to take a snapshop of the droplet and recreating it in another droplet which was by far t easiest solution and we lost some data since the DB was down for about 40 minutes. With that knowlegde now we would have choosen to use Digital Oceans Managed Database Cluster which would have saved us **a lot** of trouble in this project.

