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
  topics: Array<Topic>;

  constructor(
    private backend: CrudService,
    private router: Router
  ) { 
    this.backend.getAll<Topic>("/topic/").subscribe(data => {
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
