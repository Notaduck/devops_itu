
# The Team

The team is organized via Discord. We build a server to support all communication through that.
Here we meet up, discuss meetings, solutions, problems and more. We also created a Github webhook, so that everyone gets a notification on the Discord server, whenever there are made changes to the project.

We use discord servers to meet up every Monday during and after our lecture, we usually work on the given task most of that day. The work that we did not finish are usually completed in the weekend, because of very different time schedules during the week.

# CI/CD chain

## Git hook

### Pre commit
- pep8 
- something black
flake8

Github ()

## Travis 

- Make a new release

### Stages

- docker_build
- test
- deploy

# Repository

what, where, why
We have organized the project in one repository ...
We split logging into a separate repository because ...

# Branching strategy

Our branching strategy utilizes the Gitflow Workflow. Basically we will have 2 main branches and a number of feature branches:

- main branch - This is the main branch and contains the production code.
- developer branch - This is the development branch containing the development code. This code is merged and pushed into main at the end of each completed weekly assignment.
- feature branches - Used to develop specific features relating to a specific assignment and is merged and pushed into the development branch when it is completed.

Branches should always be branched from develop

Always pull the newest development branch before creating a feature branch

Experimenting is preferably done in branches. In some cases when working on a specific task it might make sense to further branch out from the feature branch eg.

# Development process

For this project we worked with an agile development process. Agile is all about moving fast, releasing often, and responding to the needs of your users, even if it goes against what’s in your initial plan. Every week we would plan a new implementation, work on the implementation in smaller bids, test it and release it for feedback session the next lecture. If we had any bugs or backlog from the last week we would split up and work on tasks in smaller groups. 

We used Github Projects to organize tasks in Kanban boards. We created 2 boards to separate tasks on the frontend and backend at the beginning of the project.

We later used Github issues to maintain a backlog over the tasks for the group to take on.

# Monitoring

We use the monitoring service Prometheus, to monitor our application...
To display the data that we get from Prometheus, we use the web-based multi-source graph interface, Grafana.

We split our monitoring into 2 Grafana dashboards; Business Monitoring (e.g. images/Business Monitoring), which displays our PostgreSQL Query data, and Infrastructure Monitoring (e.g. images/Infrastructure Monitoring), which displays our Prometheus metrics.

The Business Monitoring dashboard contains amount of: Users, Messages and Followers. We used these data to monitor the correctness of successful requests.

The Infrastructure Monitoring dashboard contains CPU Load percent, used for up-time calculation as well as strain on the system and HTTP Responses (Frontend / Backend), used to monitor system failure as well as performance in regards to correct response.

# Logging

...

# Security

...

# Scaling and load balancing

... 