import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { Router } from '@angular/router';
import { NgForm} from '@angular/forms';

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
  bio_change: boolean;
  password_change: boolean;

  @Input() new_password: string = "";
  @Input() current_password: string = "";
  @Input() new_bio: string = "";

  directProfile() {
    this.router.navigate(["/profile/" + this.globals.currentUsername]);
  }


  submitChanges() {

    if (this.new_password != "" && this.current_password != "") {
      this.password_change = true;
    }

    if (this.new_bio != "") {
      this.bio_change = true;
    }

    if (this.new_password != "") {
      if (this.current_password != this.user.Password) {
        alert("Password is incorrect.");
        this.new_password = "";
        this.current_password = "";
        this.new_bio = "";
        return;
      }
    }

    if (this.new_bio.length > 256 && this.new_bio != "") {
      alert("Bio must be less than 256 characters.");
        this.new_password = "";
        this.current_password = "";
        this.new_bio = "";
        return;

    }

    this.user.Password = this.new_password;
    this.profile.Bio = this.new_bio;

    if (this.password_change) {
      this.backend.updateUser(JSON.stringify(this.user)).subscribe(res => {
        if (res.toString() != "User updated successfully") {
          alert("Something went wrong, please check your input again.");
          return;
        }
      });
    }

    if (this.bio_change) {
      this.backend.updateProfile(JSON.stringify(this.profile)).subscribe(res => {
        if (res.toString() != "Profile updated successfully") {
          alert("Something went wrong, please check your input again.");
          return;
        }
      });
    }

    alert("Profile settings updated successfully.");
    this.router.navigate(["/profile/" + this.user.Username]);
    
  }


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

  uploadProfilePic(event){
    var file=event.target.files[0];
    const formData:FormData=new FormData();
    formData.append('uploadedFile',file,file.name);

    this.backend.uploadProfilePic(formData).subscribe((data:any)=>{
      var photoFileName=data.toString();
      this.profilePhotoPath=this.backend.PhotoUrl + photoFileName;
    })
  }

}
