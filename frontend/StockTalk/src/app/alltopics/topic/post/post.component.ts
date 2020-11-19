import { ActivatedRoute } from '@angular/router';
import { Globals } from './../../../Globals';
import { CrudService } from 'src/app/crud.service';
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
  voteCheckDone: Boolean;
  upvoted: Boolean;
  downvoted: Boolean;
  totalVotes: number;

  post_pic: Boolean;


  deletevote() {
    let info = "/deletevote/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info).subscribe(result => {
      if (this.upvoted == true) {
        this.totalVotes--;
      } else {
        this.totalVotes++; 
      }
      this.upvoted = false;
      this.downvoted = false;
    });
  }

  checkvotes() {
    let info2 = "/checkvotes/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info2).subscribe(res => {
      if (res.length == 0) {
        this.upvoted = false;
        this.downvoted = false;
      } else if (res[0][2] == 1) {
        this.upvoted = true;
      } else if (res[0][2] == -1) {
        this.downvoted = true;
      }
      this.voteCheckDone = true;
    });
  }

  upvote() {
    let info = "/upvote/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info).subscribe(result => {
      this.addVotes();
      this.upvoted = true;
      this.downvoted = false;
    });
  }

  downvote() {
    let info = "/downvote/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info).subscribe(result => {
      this.addVotes();
      this.upvoted = false;
      this.downvoted = true;
    });
  }

  addVotes() {
      // Gets total vote count
      let info3 = "/addvotes/" + this.Post.PostId;
      this.backend.getAll(info3).subscribe(res => {
        //console.log(res);
        if (res[0][0] == null) {
          this.totalVotes = 0;
        } else {
          this.totalVotes = res[0][0];
        }
      });
  }

  checksavedpost() {
    let info1 = "/checksavedpost/" + this.globals.currentUsername + "/" + this.Post.PostId;
    //console.log(info1);
    this.backend.getAll(info1).subscribe(res => {
      //console.log(res);
      if (res.length == 0) {
        this.saved = false;
      } else {
        this.saved = true;
      }
      this.getIsDone = true;
    });
  }

  saveButton() {
    // Post
    let info = "/savepost/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info).subscribe(result => {
      //console.log("save success")
      this.saved = true;

    });
  }

  unsaveButton() {
    // Delete
    let info = "/unsavepost/" + this.globals.currentUsername + "/" + this.Post.PostId;
    this.backend.getAll(info).subscribe(result => {
      //console.log("unsave success")
      this.saved = false;
    });
  }
  
  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) {
  
   }



   ngOnInit() {
    // Check if User has saved post
    this.checksavedpost();

    // Check if User has voted on post, if so is it a downvote or upvote?
    this.checkvotes();

    // Adds up votes
    this.addVotes();

    this.post_pic = (this.Post.PostImage != "placeholder");

  }


}
