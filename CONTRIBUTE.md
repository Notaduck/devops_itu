# Welcome to the DevOps_ITU wiki!

## Info about the repository

- This repository currently a mono repository since we django allows us to work with [database models](https://docs.djangoproject.com/en/3.1/topics/db/models/) which is tightly incorporated into the framework.

- We are currently using the feature branching model since the project is fairly small and it is easier for the team to keep it simple. The workflow is shown in the figure below

![](https://datsoftlyngby.github.io/dat2sem2018Spring/Modul5/Week1-GitBranches/img/gitFeatureBranch.png)

- The way the workflow is distributed currently is working is that the team will create a set of tasks in the project management tool git provides, once that is done will the team members distribute the tasks between each team member. Once a task is a completed a PR has to be made and once it has gone throw a review process will it get merged into the `dev` branch. When all tasks for a given week has been completed will a new PR be made in order to merge the current stage of the `dev` branch into the `main` branch and a new release should be created with an appropriate dectrion of the new changes.

- Every single team member is responsible for integration and reviews. It is up to the group to and to the idividual team member to decide if he or she has the competence to do the review or integration of a new feature.
