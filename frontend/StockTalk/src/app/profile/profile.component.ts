import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { User, Profile, UserFollowsUser } from '../Interfaces';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})

export class ProfileComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals
  ) {this.currentUsername = this.globals.currentUsername } 

  profile: Profile;
  currentUsername: String;
  isUser: boolean;

  ngOnInit(): void {
    /*this.route.data.subscribe(
      (data: {user: User}) => {
        this.currentUser = data.user;
      }
    );*/
    
    /*
    this.backend.getUserProfile(this.currentUser.Username)
    .subscribe(res => this.profile)
    console.log("Got profile", this.profile);
    */
    
  }

  /*
  this.profileService.currentUser.subscribe(
    (userData: User) => {
      this.currentUser = userData;
      this.isUser = (this.currentUser.username === this.profile.username);
    }
  );*/

}
