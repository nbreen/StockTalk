import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Router } from '@angular/router';
import { Post } from '../Interfaces';
import { User } from '../Interfaces';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend: CrudService,
    public globals: Globals,
    private router: Router
  ) { }

  Posts: Array<Post>;
  followingPostIds: Array<Number>;
  postCount: number;
  url_username: String;


  load_data(): any {

    this.backend.getAll<Number>("/getFollowingPostId/" + this.globals.currentUsername).subscribe(data => {      

      this.followingPostIds = data;
      this.postCount = data.length;
      
      console.log(this.followingPostIds);
      this.backend.getAll<Post>("/getPost/ByArray/" + this.followingPostIds).subscribe(data => {
        this.Posts = data
      });
      
    })

  }


  ngOnInit(): void {

    this.url_username = this.route.snapshot.params["User"];
    
    if (this.globals.currentUsername != this.url_username) {
      this.router.navigate(["/"]);
    } 

    this.load_data();


  }

}
