import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { CrudService } from '../crud.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {

  public input: any;
  readonly APIUrl = "http://127.0.0.1:8000/login";

  constructor(private router: Router, private backend: CrudService) {
    this.input = {
      "email": "",
      "password": ""
    }
  }

  public login() {
    if (this.input.email && this.input.password) {
      this.backend.login(this.input);
    } else {
      console.log("No data")
    }

    // The server should respond with the User object of the user logged in
    // or NULL. After the request from the server comes back this method should
    // set the global currentUser variable with the user object returned or throw
    // an error if the login was unsucessful
  }
  
  ngOnInit(): void {
  }

}
