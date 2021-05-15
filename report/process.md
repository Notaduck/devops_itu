
# The Team

The team is organized via Discord. We build a server to support all communication through that.
Here we meet up, discuss meetings, solutions, problems and more. We also created a Github webhook, so that everyone gets a notification on the Discord server, whenever there are made changes to the project.

We use discord servers to meet up every Monday during and after our lecture, we usually work on the given task most of that day. The work that we did not finish are usually completed in the weekend, because of very different time schedules during the week.

# CI/CD pipeline

Our CI/CD chain is run everytime we commit to any branch.

![CI/CD pipeline](images/CICD.png "CI/CD pipeline"){ width=50% }

## Git hook

### Pre commit

Before commiting, we have a git hook that runs **Flake8** to enforce style consistency across our Python project.

## Github

The developer code is then pushed to Github...

## Static code analysis

We use 3 static analysis tools as software quality gates into your CI/CD pipeline.

We use **SonarQube** for continuous inspection of code quality. It performs automatic reviews with static analysis of the code to detect bugs, code smells, and security vulnerabilities in our project. We use **Code Climate** for test coverage, 

We use **Better Code Hub** for quality improvements?

## Travis 

Our Travis setup consist of 3 jobs; build, test, deploy.

### Docker build

The first job in our Travis setup is build. But, before we build we start out with getting acess to Travis by using our ssh keys. Afterwards, this job has 3 stages; login to docker, build the 3 docker images web, api and proxy and lastly push the 3 images.

### Test

The second job is testing. Here we start out by migrating. Migrations are Django’s way of propagating changes we make to our models (adding a field, deleting a model, etc.) into our database schema. 

We only test frontend...

### Deploy

The third job is deploy and we only deploy when we commit to the main branch, which is how we make a new release.
Before deploying we set up the git user and tag the commit. The final step is pulling the images and deplying to the swarm.

- deploy token?

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
To display the data that we get from Prometheus, we use the web-based graph interface, Grafana.

We split our monitoring into 2 Grafana dashboards; Business Monitoring (e.g. images/Business Monitoring), which displays our PostgreSQL Query data, and Infrastructure Monitoring (e.g. images/Infrastructure Monitoring), which displays our Prometheus metrics.

The Business Monitoring dashboard contains amount of: Users, Messages and Followers. We used these data to monitor the correctness of successful requests.

The Infrastructure Monitoring dashboard contains CPU Load percent, used for up-time calculation as well as strain on the system and HTTP Responses (Frontend / Backend), used to monitor system failure as well as performance in regards to correct response.

# Logging

Our EFK stack is set up to report each transaction's user, IP address, request type, content, page redirect, and response status. This data is collected by Filebeat when Django invokes its middleware. They are logged as soon as the API/web response is ready to be sent back to the user.
When Filebeat logs the data, it is sent to the Elastic Search database that is hosted on a separate droplet, so that is accessible on Kibana.

# Security

Brief results of the security assessment.

# Scaling and load balancing

Our scaling and load balancing is done through a single Docker Swarm that holds all of Minitwit's non-database services. 