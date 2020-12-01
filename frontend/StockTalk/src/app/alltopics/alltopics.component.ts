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
  title: string = "Here are all of the Topics on StockTalk"
  topics: Array<Topic> = null;
  timer: number = -1;
  topicCount: number = -1;
  warningOne: string = null;
  warningTwo: string = null;

  constructor(
    private backend: CrudService,
    private router: Router,
    private globals: Globals
  ) { 

    this.getTime();
    
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
    // this.backend.getAll<Topic>("/topic/").subscribe(val  => {console.log(val); this.topics = val});
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

  getTime() {
    this.backend.getAll<number>("/getTopicCount/").subscribe(data => {
      console.log(data)
      this.topicCount = data[0];
      let timePerTopic = 0.000875;
      this.timer = timePerTopic * this.topicCount;
      // let variability = Math.random() / 3;
      // this.timer += variability;
      this.timer = Math.round(10 * this.timer) / 10;
      addWarningOne();
      addWarningTwo();

    })

    function addWarningOne() {
      setTimeout(function () {
          this.warningOne = "This page is taking longer than usual to load. Thank you for your patience.";
      }, this.timer * 1000);
    }

    function addWarningTwo() {
      setTimeout(function () {
          this.warningTwo = "Error: Please try again later.";
      }, 3 * this.timer * 3000);
    }

    
  }
  
}