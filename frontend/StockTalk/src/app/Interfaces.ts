export interface User {
    UserID ?: number
    Username : string;
    FullName : string;
    Email : string;
    Password : string;
    UserAge : number;
}

export interface Username {
    Username: string;
}

export interface Topic {
    TopicName : string;
    IsStock : boolean;
    isTrending : boolean;
    TrendingScore : number;
    NumberOfPosts : number;
    // TimeOfLastPost : number;
    // PreviousMA : number;
    // CurrentMA : number;
}

export interface Post {
    PostId : number;
    Username : string;
    TopicName : string;
    PostType : number;
    Post : string;
    PostDate : string;
    Downvotes : number;
    Upvotes : number;
    Anonymous : boolean;
    PostImage : string;
}

export interface Comment {
    CommentId : number;
    Username : string;
    PostId : number;
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