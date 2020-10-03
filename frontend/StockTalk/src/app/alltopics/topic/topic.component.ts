import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.scss']
})
export class TopicComponent implements OnInit {
  
  name: string;
  popularity: number;
  is_trending: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
