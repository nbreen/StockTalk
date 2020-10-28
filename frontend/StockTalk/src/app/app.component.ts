import { CrudService } from './crud.service';
import { Router } from '@angular/router';
import { Globals } from './Globals';
import { Component } from '@angular/core';
import { isConstructorDeclaration } from 'typescript';
import { ResourceLoader } from '@angular/compiler';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {

  title = 'StockTalk';

  constructor(private router: Router, private backend: CrudService, public globals: Globals) {
    localStorage.setItem("isAuthenticated", "false");
    //localStorage.setItem("currentUsername", "");
  }

  public reload() {
  }

  ngOnInit() {
    this.globals.currentUsername = localStorage.getItem("currentUsername");
    if (localStorage.getItem("isAuthenticated").match("false") === null) {
      // Current user is authenticated
      this.globals.isAuthenticated = false;
    } else {
      // Current user is NOT authenticated
      this.globals.isAuthenticated = true;
    }
  }
  

  public logout() {

    if (confirm("Are you sure you want to logout?")) {
      this.globals.isAuthenticated = false;
      this.globals.currentUser = null;
      this.globals.currentUsername = "";
      localStorage.setItem("isAuthenticated", "false");
      localStorage.setItem("currentUsername", "");
      this.router.navigate(["/"]);
    }

  }

}
