export interface User {
    UserID ?: Number
    Username : String;
    FullName : String;
    Email : String;
    Password : String;
    UserAge : Number;
    Bio ?: String;
    ProfileImage ?: String;
}

export interface Topic {
    TopicName : String;
    IsStock : Boolean;
}

export interface Post {
    PostID : Number;
    Username : String;
    TopicName : String;
    PostType : Number;
    Post : String;
    PostDate : Date;
    Anonymous : Boolean;
}

export interface Comment {
    CommentID : Number;
    Username : String;
    PostID : Number;
    Comment : String;
    CommentDate : Date;
}

export interface PostVotes {
    Username : String;
    PostID : Number;
    Vote : Number;
}

export interface CommentVotes {
    Username : String;
    CommentID : Number;
    Vote : Number;
}

export interface UserFollowsTopic {
    Username : String;
    TopicName : String;
}

export interface UserFollowsUser {
    DoingFollowing : String;
    BeingFollowed : String;
}

export interface UserSavesPost {
    Username : String;
    PostID : Number;
}

export interface Profile {
    Username: string;
    Bio: string;
    ProfileImage: string;
}