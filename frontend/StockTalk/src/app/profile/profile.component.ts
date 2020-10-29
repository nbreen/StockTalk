import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { User, Profile, UserFollowsUser } from '../Interfaces';
import { map } from 'rxjs/operators'
import { Observable } from 'rxjs';


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
  ) { this.currentUsername = this.globals.currentUsername; } 

  profile: Profile = {
    Username: "",
    Bio: "",
    ProfileImage: ""
  };
  currentUsername: any;
  isAuthenticated: boolean;
  User: any;
  isUser: boolean;

  ngOnInit(): void {

    this.currentUsername = localStorage.getItem("currentUsername");
    this.isAuthenticated = (localStorage.getItem("isAuthenticated") == "true");
    this.User = this.route.snapshot.params["User"];

    if (this.currentUsername == this.User) {
      this.isUser = true;
    } else {
      this.isUser = false;
    }

    this.backend.getUserProfile(this.currentUsername)
    .subscribe(result => {this.profile = {...result[0]}; console.log(this.profile)});
  }
}
