import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { UserFollowsUser } from '../Interfaces';
import { map } from 'rxjs/operators'
import { Observable } from 'rxjs';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';

@Component({
  selector: 'app-followers',
  templateUrl: './followers.component.html',
  styleUrls: ['./followers.component.scss']
})
export class FollowersComponent implements OnInit {

  constructor(   private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) { }

  followers: Array<string>;
  following: Array<string>;
  url_username: string;

  ngOnInit(): void {
    this.url_username = this.route.snapshot.params["User"];
    // console.log(url_username);

    this.backend.getAll<string>("/followers/" + this.url_username).subscribe(res => {
      this.followers = res;
      console.log(this.followers);
    });

    this.backend.getAll<string>("/following/" + this.url_username).subscribe(res => {
      this.following = res;
      console.log(this.following);
    });
  }

}
