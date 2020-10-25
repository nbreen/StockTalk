import { CrudService } from './crud.service';
import { Router } from '@angular/router';
import { Globals } from './Globals';
import { Component } from '@angular/core';
import { isConstructorDeclaration } from 'typescript';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {
  title = 'StockTalk';
  // currentUsername: String;

  // constructor(private router: Router, private backend: CrudService, private globals: Globals) {
  //   this.currentUsername = this.globals.currentUsername;
  // }
}
