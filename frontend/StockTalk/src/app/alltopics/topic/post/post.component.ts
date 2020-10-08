import { CommentComponent } from './comment/comment.component';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {
  PostId: Number;
  Username: String;
  Name: String;
  TopicName: String;
  PostType: Number;
  Post: String;
  PostDate: Date;
  Anonymous: Boolean;
  comments: CommentComponent[];
  
  constructor() {
    this.PostId = -1;
    this.Username = "poster101";
    this.Name = "Poster Name"
    this.TopicName = "N/A";
    this.PostType = -1;
    this.Post = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.";
    this.PostDate = new Date();
    this.Anonymous = false;
    this.comments = new Array(3)
   }

  ngOnInit(): void {

  }

}
