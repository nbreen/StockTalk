import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile-settings',
  templateUrl: './profile-settings.component.html',
  styleUrls: ['./profile-settings.component.scss']
})
export class ProfileSettingsComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals,
    private router: Router
  ) { } 

  
  profile: Profile;
  user: User;
  profilePhotoPath: string;


  ngOnInit(): void {
    var url_username = this.route.snapshot.params["User"];

    if (this.globals.currentUsername != url_username) {
      this.router.navigate(["/"]);
    } 

    this.backend.getProfile(this.globals.currentUsername).subscribe(res => {
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
    
  }

}
