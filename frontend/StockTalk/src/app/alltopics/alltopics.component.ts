import { TopicComponent } from './topic/topic.component';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-alltopics',
  templateUrl: './alltopics.component.html',
  styleUrls: ['./alltopics.component.scss'],
  
})
export class AlltopicsComponent implements OnInit {

  title: string = "Here are all of the Topics on StockTalk"
  topics: TopicComponent;

  constructor() { }

  ngOnInit(): void {
  }

}
