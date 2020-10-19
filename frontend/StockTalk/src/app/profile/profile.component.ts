import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { CrudService } from '../crud.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})

export class ProfileComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend : CrudService
  ) { } 

  profile: Profile;
  currentUser: User;
  isUser: boolean;

  ngOnInit(): void {
    this.route.data.subscribe(
      (data: {user: User}) => {
        this.currentUser = data.user;
      }
    );
  }

  /*
  this.profileService.currentUser.subscribe(
    (userData: User) => {
      this.currentUser = userData;
      this.isUser = (this.currentUser.username === this.profile.username);
    }
  );*/

}
