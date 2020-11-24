import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { UserFollowsUser } from '../Interfaces';
import { map } from 'rxjs/operators'
import { Observable } from 'rxjs';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { Post } from '../Interfaces';
import { Router } from '@angular/router';


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})

export class ProfileComponent implements OnInit {
  posts: Array<Post>;

  constructor(
    private route: ActivatedRoute,
    private backend: CrudService,
    public globals: Globals,
    private router: Router
  ) {

  }

  profile: Profile;
  profilePhotoPath: string;
  settingsURL: string;

  user: User;
  isUser: boolean;

  currProfile: string;
  following: boolean;
  getIsDone: boolean;

  Posts: Array<Post>;
  postCount: number = -1;


  showSettings() {
    if (this.isUser && this.globals.isAuthenticated) {
      return true;
    } else {
      return false;
    }
  }

  followButton() {
    // Post
    let info = "/followuser/" + this.globals.currentUsername + "/" + this.currProfile;
    this.backend.getAll(info).subscribe(result => {
      console.log("follow success")
      this.following = true;

    });
  }

  routeMakePost() {
    this.router.navigate(["/makepost/" + this.globals.currentUsername]);
  }

  unfollowButton() {
    // Delete
    let info = "/unfollowuser/" + this.globals.currentUsername + "/" + this.currProfile;
    this.backend.getAll(info).subscribe(result => {
      console.log("unfollow success")
      this.following = false;
    });
  }

  ngOnInit(): void {
  
    var url_username = this.route.snapshot.params["User"];
    this.currProfile = url_username;

    if (this.globals.currentUsername == url_username) {
      this.isUser = true;
    } else {
      this.isUser = false;
    }

    if (this.isUser) {
      this.settingsURL = "/settings/" + this.globals.currentUsername;
    }

    // this.backend.getProfile(this.globals.currentUsername).subscribe(res => {
    this.backend.getProfile(this.currProfile).subscribe(res => {
      var profile_data = JSON.stringify(res);
      profile_data = profile_data.substring(1, profile_data.length-1);
      this.profile = JSON.parse(profile_data);
      this.profilePhotoPath = this.backend.PhotoUrl + this.profile.ProfileImage;
    });

    this.backend.getUser(this.globals.currentUsername).subscribe(res => {
      var user_data = JSON.stringify(res);
      user_data = user_data.substring(1, user_data.length-1);
      this.user = JSON.parse(user_data);
    });

    let info = "/checkfollowuser/" + this.globals.currentUsername + "/" + this.currProfile;
    console.log(info);
    this.backend.getAll(info).subscribe(res => {
      console.log(res);
      if (res.length == 0) {
        this.following = false;
      } else if (res[0] == "same") {
        this.following = false;
        this.isUser = true;
      } else {
        this.following = true;
      }
      console.log(res);
      this.getIsDone = true;
    });

    this.backend.getAll<Post>("/getPost/ByUser/" + this.currProfile).subscribe(data => {
      this.Posts = data;
      console.log(this.Posts);
      this.postCount = data.length;
      this.Posts = this.Posts.reverse();
    })


  }

}
