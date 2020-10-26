import { CrudService } from 'src/app/crud.service';
import { Post } from './../../Interfaces';
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

  constructor(private backend: CrudService) {
    this.TopicName = window.location.href.substring(28); // Change later, gets the TopicName from substringing the URL
    this.IsStock = true;
   }

  ngOnInit(): void {
    this.backend.getAll<Post>("/post/" + this.TopicName).subscribe(data => {
      console.log(data);
      this.Posts = data;
    })
  }

}
