import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Router } from '@angular/router';
import { Post } from '../Interfaces';
import { User } from '../Interfaces';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend: CrudService,
    public globals: Globals,
    private router: Router
  ) { }

  Posts: Array<Post>;
  followingPostIds: Array<Number>;
  postCount: number;
  url_username: String;

  // following: Array<String>;
  // topics: Array<String>;

  load_data(): any {

    this.backend.getAll<Number>("/getFollowingPostId/" + this.globals.currentUsername).subscribe(data => {      

      this.followingPostIds = data;
      this.postCount = data.length;
      
      console.log(this.followingPostIds);
      this.backend.getAll<Post>("/getPost/ByArray/" + this.followingPostIds).subscribe(data => {
        this.Posts = data
      });
      
    })

  }

  // // Prev Load Data
  // load_data2(): any {

  //   this.postCount = 0;

  //   this.backend.getAll<String>("/following/" + this.url_username).subscribe(res => {
  //     this.following = res;
  //     //alert("1");
  //     this.backend.getAll<String>("/topicsFollowing/" + this.url_username).subscribe(res => {
  //       this.topics = res;
  //       //alert("2");

  //       for (var i = 0; i < this.following.length; i++) {
          
  //         var index = this.following[i].toString().indexOf(",");
  //         this.following[i] = this.following[i].toString().substring(index + 1);
  //         //alert("/getPost/ByUser/" + this.following[i]);
          
  //         this.backend.getAll<Post>("/getPost/ByUser/" + this.following[i]).subscribe(data => {
  //           //alert("3");
  //           this.Posts = data.concat(this.Posts);
  //           this.postCount += data.length;
  //         });
  //       }

  //       for (var i = 0; i < this.topics.length; i++) {

  //         var index = this.topics[i].toString().indexOf(",");
  //         this.topics[i] = this.topics[i].toString().substring(index + 1);

  //         this.backend.getAll<Post>("/getPost/ByTopic/" + this.topics[i]).subscribe(data => {
  //           //alert("4");
  //           this.Posts = data.concat(this.Posts);
  //           this.postCount += data.length;
  //         });

  //       }

  //       this.Posts.sort(function(a,b){
  //         // Turn your strings into dates, and then subtract them
  //         // to get a value that is either negative, positive, or zero.
  //         return <any>new Date(b.PostDate) - <any>new Date(a.PostDate);
  //       });

  //       this.Posts.reverse();

      
  //     });
  //   });

  // }

  ngOnInit(): void {

    this.url_username = this.route.snapshot.params["User"];
    
    if (this.globals.currentUsername != this.url_username) {
      this.router.navigate(["/"]);
    } 

    this.load_data();


  }

}
