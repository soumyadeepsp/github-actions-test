This is the Datatools-GitHub-Standards GitHub Actions which are used to implement specific GitHub standards in all the Datatools teams' repositories.

Following are the 2 GitHub Actions in this repository - 
1. branch-name-alert: This GitHub Action sends a Slack message to the developer's team channel if he/she creates or pushes a branch with a name that does not follow the proper naming conventions. The Slack message is a warning that if the branch name is not changed within the next 48 hours, then it will get automatically deleted.

2. forty-eight-hour-cleanup: This GitHub Action runs once every 48 hours and deletes any branches that do not follow the proper naming conventions and were created in the past 48-72 hours.

The steps to incorporate the above GitHub Actions in this repository are given in the following Confluence document - https://confluence.expedia.biz/pages/viewpage.action?spaceKey=DAPS&title=Datatools-GitHub-Standards+GitHub+Actions
