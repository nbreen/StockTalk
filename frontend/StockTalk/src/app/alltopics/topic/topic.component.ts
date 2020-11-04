import { Globals } from './../../Globals';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from 'src/app/crud.service';
import { Post, User } from './../../Interfaces';
import { CommentComponent } from './post/comment/comment.component';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.scss']
})
export class TopicComponent implements OnInit {
  
  TopicName: string;
  IsStock: boolean;
  Posts: Array<Post>;
  following: boolean;
  getIsDone: boolean;


  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals
    ) {
    this.TopicName = window.location.href.substring(28); // Change later, gets the TopicName from substringing the URL
    this.IsStock = true;
   }



   followButton() {
    // Post
    let info = "/followtopic/" + this.globals.currentUsername + "/" + this.TopicName;
    this.backend.getAll(info).subscribe(result => {
      console.log("follow success")
      this.following = true;

    });
  }

  unfollowButton() {
    // Delete
    let info = "/unfollowtopic/" + this.globals.currentUsername + "/" + this.TopicName;
    this.backend.getAll(info).subscribe(result => {
      console.log("unfollow success")
      this.following = false;
    });
  }

  ngOnInit(): void {
    
    let info = "/checkfollowtopic/" + this.globals.currentUsername + "/" + this.TopicName;
    console.log(info);
    this.backend.getAll(info).subscribe(res => {
      console.log(res);
      if (res.length == 0) {
        this.following = false;
      } else {
        this.following = true;
      }
      this.getIsDone = true;
    });
    
    this.backend.getAll<Post>("/post/" + this.TopicName).subscribe(data => {
      console.log(data);
      this.Posts = data;
    })

  }

}
