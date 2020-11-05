import { Globals } from './../../../../Globals';
import { CrudService } from 'src/app/crud.service';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit, Input } from '@angular/core';
import { stringify } from 'querystring';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent implements OnInit {
  
  @Input() Comment;
  getIsDone: Boolean;

  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) { 
  }

  ngOnInit(): void {

  }

}
