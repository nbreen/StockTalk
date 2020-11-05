import { Globals } from './../Globals';
import { Component, OnInit } from '@angular/core';
import { Topic, Post } from './../Interfaces';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from 'src/app/crud.service';
import { Input } from '@angular/core'; 

@Component({
  selector: 'app-view-single-post',
  templateUrl: './view-single-post.component.html',
  styleUrls: ['./view-single-post.component.scss']
})
export class ViewSinglePostComponent implements OnInit {


  Posts: Array<Post>;
  SinglePostId: string;

  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) { }
    

  ngOnInit(): void {
    let arr = (window.location.href).split("/");
    this.SinglePostId = arr[4];
    console.log(this.SinglePostId);

    this.backend.getAll<Post>("/getPost/ById/" + this.SinglePostId).subscribe(data => {
      this.Posts = data;
      console.log(this.Posts);
    })

    
  }

}
