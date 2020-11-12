import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';

@Component({
  selector: 'app-suggestions',
  templateUrl: './suggestions.component.html',
  styleUrls: ['./suggestions.component.scss']
})
export class SuggestionsComponent implements OnInit {

  constructor(private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals) { }
    topics: Array<string>;
    users: Array<string>;
    username: string;

  ngOnInit(): void {

    this.username = this.globals.currentUsername;
    console.log(this.username)

    this.backend.getAll<string>("/suggested-topics/" + this.username).subscribe(res => {
      this.topics = res;
    });

    this.backend.getAll<string>("/suggested-users/" + this.username).subscribe(res => {
      this.users = res;
    });

  }

}
