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
  postCount: Number = -1;
  savedPostIds: Array<Number>;
  savedPostCount: number;


  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) { 
    
  }

  ngOnInit(): void {
    
    this.backend.getAll<Number>("/getPost/BySaved/" + this.globals.currentUsername).subscribe(data => {      

      this.savedPostIds = data;
      this.savedPostCount = data.length;
      this.postCount = this.savedPostCount;
      
      console.log(this.savedPostIds);
      this.backend.getAll<Post>("/getPost/ByArray/" + this.savedPostIds).subscribe(data => {
        this.Posts = data
      });
      
    })
    

  }

}
