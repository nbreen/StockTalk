export interface User {
    UserID ?: number
    Username : string;
    FullName : string;
    Email : string;
    Password : string;
    UserAge : number;
}

export interface Topic {
    TopicName : string;
    IsStock : boolean;
}

export interface Post {
    PostID : number;
    Username : string;
    TopicName : string;
    PostType : number;
    Post : string;
    PostDate : Date;
    Anonymous : boolean;
}

export interface Comment {
    CommentID : number;
    Username : string;
    PostID : number;
    Comment : string;
    CommentDate : Date;
}

export interface PostVotes {
    Username : string;
    PostID : number;
    Vote : number;
}

export interface CommentVotes {
    Username : string;
    CommentID : number;
    Vote : number;
}

export interface UserFollowsTopic {
    Username : string;
    TopicName : string;
}

export interface UserFollowsUser {
    DoingFollowing : string;
    BeingFollowed : string;
}

export interface UserSavesPost {
    Username : string;
    PostID : number;
}

export interface Profile {
    Username: string;
    Bio: string;
    ProfileImage: string;
}