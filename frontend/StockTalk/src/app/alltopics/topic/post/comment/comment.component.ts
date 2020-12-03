import { Globals } from './../../../../Globals';
import { CrudService } from 'src/app/crud.service';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit, Input } from '@angular/core';
import { stringify } from 'querystring';
//import { runInThisContext } from 'vm';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent implements OnInit {
  
  @Input() Comment;
  getIsDone: Boolean;
  isVerified: Boolean;
  verifiedPath: String;

  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) { 
  }

  ngOnInit(): void {
    this.verifiedPath = "http://127.0.0.1:8000/media/verified.png";
    if (localStorage.getItem("verified_" + this.Comment.Username) == "true") {
      this.isVerified = true;
    }

  }

}
