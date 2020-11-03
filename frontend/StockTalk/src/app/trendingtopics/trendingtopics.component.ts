import { Globals } from './../Globals';
import { TopicComponent } from './topic/topic.component';
import { CrudService } from '../crud.service';
import { Topic } from '../Interfaces';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-trendingtopics',
  templateUrl: './trendingtopics.component.html',
  styleUrls: ['./trendingtopics.component.scss'],

})

export class TrendingtopicsComponent implements OnInit {
  title: string = "Here are all of the Trending Topics on StockTalk"
  topics: Array<Topic>;


  constructor(
    private backend: CrudService,
    private router: Router
  ) {
    this.backend.getAll<Topic>("/topic/2").subscribe(data => {
      console.log(data);
      this.topics = data;
    })
  }

  ngOnInit() {
    // this.backend.getAll<Topic>("/topic/").subscribe(val  => {console.log(val); this.topics = val});

  }

  sortAZ() {

  }

  sortCount() {

  }

}
