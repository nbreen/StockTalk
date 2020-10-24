import { Component, Input, OnInit } from '@angular/core';
import { RequestOptions } from '@angular/http';
import { Router } from "@angular/router";
import { CrudService } from '../crud.service';
import { Http } from '@angular/http';
import { Headers } from '@angular/http';
import { map } from 'rxjs/operators';
import { NgForm} from '@angular/forms';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {

  constructor(private service: CrudService, private router: Router) { }

  @Input() loginData: any = {
    Username: "",
    Password: ""
  };
  
  resetForm(form?:NgForm) {
    if (form != null) {
      form.reset();
    }

    this.loginData.Username = "";
    this.loginData.Password = "";
  }

  public login() {
    if (this.loginData.Username && this.loginData.Password) {
      return this.service.validateUser(this.loginData).subscribe(result => {
        result.json();
        //this.router.navigate(["/profile/"])
      });
      
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
