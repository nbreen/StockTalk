import { Component, Input, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { CrudService } from '../crud.service';
import { Globals } from '../Globals';
import { NgForm} from '@angular/forms';
import { User } from '../shared/user.model';
import bcrypt

import UserApp.views



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})

export class LoginComponent implements OnInit {

  constructor(private service: CrudService, private router: Router,
    private globals: Globals) { }

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

  temp_user: User;

  public login() {
    passwd = this.loginData.Password
    //salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    this.loginData.Password = str(hashed)
    if (this.loginData.Username && this.loginData.Password) {
      return this.service.validateUser(this.loginData).subscribe(res => {
        console.log(res);
        if (res.toString().match("User exists") == null) {
          alert("Username or password is incorrect");
        } else {

          this.service.getUser(this.loginData.Username).subscribe(res => {
            var user_data = JSON.stringify(res);
            user_data = user_data.substring(1, user_data.length-1);
            this.temp_user = JSON.parse(user_data);

            if (this.temp_user.Password == this.loginData.Password) {
            //if (bcrypt.checkpw(this.temp_user.Password, this.loginData.Password)) {
              alert("Welcome " + this.temp_user.Username);
              this.globals.isAuthenticated = true;
              this.globals.currentUsername = this.loginData.Username;
              localStorage.setItem("isAuthenticated", "true");
              localStorage.setItem("currentUsername", this.loginData.Username);
              this.router.navigate(["/profile/" + this.loginData.Username]);
            } else {
              alert("Username or password is incorrect");
              this.temp_user = null;
              return;
            }
          })
        }
      });
      
    } else {
      console.log("No data")
    }
  }
  
  ngOnInit(): void {
  }

}
