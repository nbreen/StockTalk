import { CommentComponent } from './post/comment/comment.component';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.scss']
})
export class TopicComponent implements OnInit {
  
  name: string;
  popularity: number;
  is_trending: boolean;
  is_stock: boolean;

  constructor() {
    this.name = "NoNameTopic"
    this.popularity = -1;
    this.is_trending = false;
    this.is_stock = false;
   }

  ngOnInit(): void {
  }

}
