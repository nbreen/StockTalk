import { Component, OnInit } from '@angular/core';
import { stringify } from 'querystring';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent implements OnInit {
  CommentId : number;
  Comment: string;
  Username: string;
  Name: string;
  Date : Date;
  PostId: number;

  constructor() { 
    this.CommentId = -1;
    this.Comment = "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
    this.Username = "nulluser";
    this.Name = "No Name";
    this.Date = new Date();
    this.PostId = -1;
  }

  ngOnInit(): void {

  }

}
