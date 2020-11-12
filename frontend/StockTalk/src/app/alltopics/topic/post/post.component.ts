import { Topic } from './../../../Interfaces';
import { ActivatedRoute } from '@angular/router';
import { Globals } from './../../../Globals';
import { CrudService } from 'src/app/crud.service';
import { Post } from './../../../shared/post.model';
import { CommentComponent } from './comment/comment.component';
import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {

  @Input() Post;

  saved: Boolean;
  getIsDone: Boolean;
  upvoted: Boolean;
  downvoted: Boolean;


  saveButton() {
    // Post
    let info = "/savepost/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info).subscribe(result => {
      console.log("save success")
      this.saved = true;

    });
  }

  deleteVote() {
    // let info = "/savepost/" + this.globals.currentUsername + "/" + this.Post.PostId;
    // this.backend.getAll(info).subscribe(result => {
    //   console.log("save success")
    //   this.saved = true;

    // });
  }

  upvote() {

    if (localStorage.getItem(this.Post.TopicName + "_upvoted") == "true") {
      --this.Post.Upvotes;
      localStorage.setItem(this.Post.TopicName + "_upvoted", "false");
    } else {
      ++this.Post.Upvotes;
      localStorage.setItem(this.Post.TopicName + "_upvoted", "true");
      return;
    }

    this.backend.updatePost(this.Post).subscribe(result => {
      console.log("save success")
      this.saved = true;
    });
  }

  downvote() {

    if (localStorage.getItem(this.Post.TopicName + "_downvoted") == "true") {
      --this.Post.Downvotes;
      localStorage.setItem(this.Post.TopicName + "_downvoted", "false");
    } else {
      ++this.Post.Downvotes;
      localStorage.setItem(this.Post.TopicName + "_downvoted", "true");
      return;
    }
   
    this.backend.updatePost(this.Post).subscribe(result => {
      console.log("save success")
      this.saved = true;
    });
  }

  unsaveButton() {
    // Delete
    let info = "/unsavepost/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info).subscribe(result => {
      console.log("unsave success")
      this.saved = false;
    });
  }
  
  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) {
  
   }

   ngOnInit() {
    let info = "/checksavedpost/" + this.globals.currentUsername + "/" + this.Post.PostId;
    console.log(info);
    this.backend.getAll(info).subscribe(res => {
      console.log(res);
      if (res.length == 0) {
        this.saved = false;
      } else {
        this.saved = true;
      }
      this.getIsDone = true;
    });
  }


}
