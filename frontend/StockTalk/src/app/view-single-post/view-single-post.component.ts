import { Globals } from './../Globals';
import { Component, OnInit } from '@angular/core';
import { Topic, Post, Comment } from './../Interfaces';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from 'src/app/crud.service';
import { Input } from '@angular/core';
import {NgbActiveModal, NgbModal} from "@ng-bootstrap/ng-bootstrap"; 
import { MakeCommentComponent } from '../make-comment/make-comment.component';
import { toInteger } from '@ng-bootstrap/ng-bootstrap/util/util';

@Component({
  selector: 'app-view-single-post',
  templateUrl: './view-single-post.component.html',
  styleUrls: ['./view-single-post.component.scss']
})
export class ViewSinglePostComponent implements OnInit {


  Posts: Array<Post>;
  SinglePostId: string;
  Comments: Array<Comment>; 

  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals,
    private modalService: NgbModal) { }
    

  ngOnInit(): void {
    let arr = (window.location.href).split("/");
    this.SinglePostId = arr[4];
    console.log(this.SinglePostId);

    this.backend.getAll<Post>("/getPost/ById/" + this.SinglePostId).subscribe(data => {
      this.Posts = data;
      console.log(this.Posts);
    })

    this.backend.getAll<Comment>("/getComments/" + this.SinglePostId).subscribe(data => {
      this.Comments = data;
      this.Comments.forEach(function (value) {
        value.CommentDate = new Date(value.CommentDate);
      })
      this.Comments = this.Comments.sort((a, b) => {
        return <any>new Date(b.CommentDate) - <any>new Date(a.CommentDate);});
      console.log(this.Comments);
    })
  }

  open() {
    const modalRef = this.modalService.open(MakeCommentComponent);
    modalRef.componentInstance.parentPostId = Number(this.SinglePostId);
  }

}
