import { TopicComponent } from './topic/topic.component';
import { CrudService } from '../crud.service';
import { Topic } from '../Interfaces';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-trendingtopics',
  templateUrl: './trendingtopics.component.html',
  styleUrls: ['./trendingtopics.component.scss'],

})

export class TrendingtopicsComponent implements OnInit {
  title: string = "Here are all of the Trending Topics on StockTalk"
  topics: Array<Topic>;

  constructor(
    private backend: CrudService
  ) { }

  ngOnInit() {

    this.backend.getAll<Topic>("/topic/").subscribe(data => {
      console.log(data);
      this.topics = data;
    })
  }
}
