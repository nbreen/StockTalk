import { AlltopicsComponent } from './../alltopics/alltopics.component';
import { Post } from './../shared/post.model';
import { ActivatedRoute } from '@angular/router';
import { Globals } from './../Globals';
import { CrudService } from 'src/app/crud.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-view-saved-posts',
  templateUrl: './view-saved-posts.component.html',
  styleUrls: ['./view-saved-posts.component.scss']
})
export class ViewSavedPostsComponent implements OnInit {

  Posts: Array<Post>;
  postCountTotal: number = -1;
  postCount: number = 1;
  AllPosts: Array<Post>;
  savedPostIds: Array<Number>;
  savedPostCount: number;


  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) { 
    
  }

  ngOnInit(): void {

    var i;

    this.backend.getAll<Post>("/getAllPosts/" + this.globals.currentUsername).subscribe(data => {
      this.AllPosts = data;
      this.postCountTotal = data.length;

      this.Posts = this.AllPosts;
      this.postCount = this.postCountTotal;
    })
    
    this.backend.getAll<Number>("/getPost/BySaved/" + this.globals.currentUsername).subscribe(data => {      

      this.savedPostIds = data;
      this.savedPostCount = data.length;
    
    })

    

    

  }

}
