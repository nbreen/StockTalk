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

  ngOnInit() {
  }
  
  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) {
  
   }

}
