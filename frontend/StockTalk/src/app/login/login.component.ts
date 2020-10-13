import { Component, OnInit } from '@angular/core';
import { Http, Headers, RequestOptions } from "@angular/http";
import { Router } from "@angular/router";



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {

  public input: any;
  readonly APIUrl = "http://127.0.0.1:8000/login";

  constructor(private http: Http, private router: Router) {
    this.input = {
      "email": "",
      "password": ""
    }
  }

  public login() {
    if (this.input.email && this.input.password) {
      let headers = new Headers({ "content-type": "applications/json" });
      let options = new RequestOptions({ headers: headers});
      this.http.post(this.APIUrl, JSON.stringify(this.input), options)
        .subscribe(result => {
          this.router.navigate(["/profile"], { "queryParams": result});
        })
    }
  }
  

  ngOnInit(): void {
  }

}
