import { toInteger } from '@ng-bootstrap/ng-bootstrap/util/util';
import { Globals } from './../Globals';
import { TopicComponent } from './topic/topic.component';
import { CrudService } from '../crud.service';
import { Topic } from '../Interfaces';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-alltopics',
  templateUrl: './alltopics.component.html',
  styleUrls: ['./alltopics.component.scss'],

})

export class AlltopicsComponent implements OnInit {
  title: string = "explore all topics on StockTalk"
  topics: Array<Topic> = null;

  currentTopic: number = 0;
  postsPerPage: number = 50;
  pageNumber: number = 1;
  maxPage: number = -1;

  constructor(
    private backend: CrudService,
    private router: Router,
    private globals: Globals
  ) { 
    
    if (localStorage.getItem("sortAZ") == "true") {
      this.backend.getAll<Topic>("/topic/0").subscribe(data => {
        console.log(data);
        this.topics = data;
        this.maxPage = Math.ceil(this.topics.length / this.postsPerPage)
      })
    } else if (localStorage.getItem("sortCount") == "true") {
      this.backend.getAll<Topic>("/topic/1").subscribe(data => {
        console.log(data);
        this.topics = data;
        this.maxPage = Math.ceil(this.topics.length / this.postsPerPage)
      })
    } else {
      localStorage.setItem("sortCount", "true");
      this.backend.getAll<Topic>("/topic/0").subscribe(data => {
        console.log(data);
        this.topics = data;
        this.maxPage = Math.ceil(this.topics.length / this.postsPerPage)
      })
    }
  }

  ngOnInit() {
  }

  sortAZ() {
    localStorage.setItem("sortAZ", "true");
    localStorage.setItem("sortCount", "false");
    window.location.reload();
  }

  sortCount() {
    localStorage.setItem("sortAZ", "false");
    localStorage.setItem("sortCount", "true");
    window.location.reload(); 
  }

  next() {
    if (this.pageNumber == this.maxPage) {
      return;
    } 
    if (this.currentTopic < this.topics.length) {
      this.currentTopic += this.postsPerPage;
      this.pageNumber++;
    }
  }

  prev() {
    if (this.pageNumber != 0) {
      this.currentTopic -= this.postsPerPage;
      this.pageNumber--;
    }
  }

  jump() {
    let pageRequested: number = parseInt((<HTMLInputElement>document.getElementById("page")).value)
    if (pageRequested < 1 || pageRequested> this.maxPage ) {
      alert(`Page number is invalid! Please enter a page between 1 and ${this.maxPage}`);
    } else {
      this.pageNumber = pageRequested;
      this.currentTopic = (this.pageNumber - 1) * this.postsPerPage;
    }
  }

  
}
