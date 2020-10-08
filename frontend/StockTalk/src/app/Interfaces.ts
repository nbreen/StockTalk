export interface User {
    UserID : Number
    Username : String;
    FullName : String;
    Email : String;
    Password : String;
    UserAge : Number;
    Bio : String;
    ProfileImage : String;
    Type : "/user/";
}

export interface Topic {
    TopicName : String;
    IsStock : Boolean;
    Type : "/topic/";
}

export interface Post {
    PostID : Number;
    Username : String;
    TopicName : String;
    PostType : Number;
    Post : String;
    PostDate : Date;
    Anonymous : Boolean;
    Type : "/post/";
}

export interface Comment {
    CommentID : Number;
    Username : String;
    PostID : Number;
    Comment : String;
    CommentDate : Date;
    Type : "/comment/";
}

export interface PostVotes {
    Username : String;
    PostID : Number;
    Vote : Number;
    Type : "/postVotes/";
}

export interface CommentVotes {
    Username : String;
    CommentID : Number;
    Vote : Number;
    Type : "/commentVotes/";
}

export interface UserFollowsTopic {
    Username : String;
    TopicName : String;
    Type : "/userFollowsTopic/";
}

export interface UserFollowsUser {
    DoingFollowing : String;
    BeingFollowed : String;
    Type : "/userFollowsUser/";
}

export interface UserSavesPost {
    Username : String;
    PostID : Number;
    Type : "/userSavesPost/";
}