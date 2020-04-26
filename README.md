# "Important!"
Docker-Compose procedure:
1.Clone your repository
2.cd into to the directory of the repository
3.Build the docker image (docker-compose build)
4.Create and run a docker containers (docker-compose up --detach)
5.Open a browser and navigate to http://localhost:<local_port> (We’ll read your docker-compose.yml to find your local port)

Please run "docker-compose run web python manage.py migrate" after step 4 and before step 5.

# CSE312 "CHATME!"

ChatMe is a project that we built for CSE312. We developed website by utilizing various framworks and protocals that allows our client to "chat","Follow","Share" with other users.

## Group Member

* [GuangXin Huang]- The Project Manager
* [XuanHua Zhang] - Software Engineer



### User Accounts


```
* Every user have account where they can login and take actions that are associated with their account

* New Client Can register a new account to store informations such as friends and Chat History
```



### Live sharing of multimedia content between users


```
1)Users can upload some form of multimedia content that is displayed in real-time to other users

2)Users can "vote" AND "comment" on user-submitted content

```

### Users can friend or follow other users


```
  Users can Add/Remove friends with other users
```

### Users can send direct messages to other users

```
  After 2 users are mutual friends with eachother, a private chat (only visible to two users) can be initiated
```



