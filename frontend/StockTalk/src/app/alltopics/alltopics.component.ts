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

  constructor(
    private backend: CrudService,
    private router: Router,
    private globals: Globals
  ) { 
    
    if (localStorage.getItem("sortAZ") == "true") {
      this.backend.getAll<Topic>("/topic/0").subscribe(data => {
        console.log(data);
        this.topics = data;
      })
    } else if (localStorage.getItem("sortCount") == "true") {
      this.backend.getAll<Topic>("/topic/1").subscribe(data => {
        console.log(data);
        this.topics = data;
      })
    } else {
      localStorage.setItem("sortCount", "true");
      this.backend.getAll<Topic>("/topic/0").subscribe(data => {
        console.log(data);
        this.topics = data;
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
    this.currentTopic += 100;
    if (this.currentTopic >= this.topics.length) {
      this.currentTopic = this.topics.length - 1;
    }
  }

  prev() {
    if (this.currentTopic != 0) {
    this.currentTopic -= 100;
    }
  }

  
}
