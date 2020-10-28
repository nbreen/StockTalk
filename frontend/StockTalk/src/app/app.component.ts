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

  constructor(private router: Router, private backend: CrudService, public globals: Globals) {
     
  }

  public logout() {
    this.globals.isAuthenticated = false;
    this.globals.currentUser = null;
    this.globals.currentUsername = "";
    this.router.navigate(["/"]);
  }

}
