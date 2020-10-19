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
  }
  
  ngOnInit(): void {
  }

}
