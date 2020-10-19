import { TopicComponent } from './topic/topic.component';
import { CrudService } from '../crud.service';
import { Topic } from '../Interfaces';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-alltopics',
  templateUrl: './alltopics.component.html',
  styleUrls: ['./alltopics.component.scss'],
  
})
export class AlltopicsComponent implements OnInit {

  title: string = "Here are all of the Topics on StockTalk"
  topics: TopicComponent[] = new Array();
  //topics: Topic[] = [];

  constructor(
    private backend: CrudService
  ) { }

  ngOnInit(): void {
    let topic1:TopicComponent = new TopicComponent;
    let topic2:TopicComponent = new TopicComponent;
    let topic3:TopicComponent = new TopicComponent;
    this.topics = new Array(topic1, topic2, topic3);
    //this.backend.getAll<Topic>("/topic/").subscribe(val  => {console.log(val); this.topics = val});
  }

}
