
import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { Post } from '../shared/post.model';
import { Router } from '@angular/router';
import { NgForm} from '@angular/forms';

@Component({
  selector: 'app-make-post',
  templateUrl: './make-post.component.html',
  styleUrls: ['./make-post.component.scss']
})
export class MakePostComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals,
    private router: Router
  ) { }

  profile: Profile;
  user: User;

  @Input() new_post: Post = {
    Username: "",
    Text: "",
    Image: "",
    Topic: "",
    Upvotes: 0,
    Downvotes: 0
  }

  submitPost() {

  }

  directProfile() {
    this.router.navigate(["/profile/" + this.globals.currentUsername]);
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
    });

    this.backend.getUser(this.globals.currentUsername).subscribe(res => {
      var user_data = JSON.stringify(res);
      user_data = user_data.substring(1, user_data.length-1);
      this.user = JSON.parse(user_data);
    });

  }

}
