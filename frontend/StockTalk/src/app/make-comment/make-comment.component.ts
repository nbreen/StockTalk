import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Comment } from "../Interfaces";
import { Globals } from "../Globals"
import { CrudService } from "../crud.service"

@Component({
  selector: 'app-make-comment',
  templateUrl: './make-comment.component.html',
  styleUrls: ['./make-comment.component.scss']
})
export class MakeCommentComponent implements OnInit {

  @Input() parentPostId: number;
    new_comment: Comment = {
      CommentId : 0,
      Username : this.appGlobals.currentUsername,
      PostId : 0,
      Comment : "",
      CommentDate: new Date()
    };

  constructor(public activeModal: NgbActiveModal,
              public appGlobals: Globals,
              public backend: CrudService) {}

  ngOnInit(): void {
  }

  submitComment() {
    this.activeModal.close();
    this.new_comment.PostId = this.parentPostId;
    console.log(JSON.stringify(this.new_comment));
    this.backend.addComment(this.new_comment);
  }
}
