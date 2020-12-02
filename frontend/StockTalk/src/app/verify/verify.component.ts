
import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-verify',
  templateUrl: './verify.component.html',
  styleUrls: ['./verify.component.scss']
})
export class VerifyComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals,
    private router: Router
  ) { }

  user: User;


  directProfile() {
    this.router.navigate(["/profile/" + this.globals.currentUsername]);
  }

  submitVerification() {


    var storedRequests = JSON.parse(localStorage.getItem("verification_requests"));

    var requests = [];
    requests[0] = this.user.Username;
    if (storedRequests != null) {
      requests.concat(storedRequests);
    } 
    
    localStorage.setItem("verification_requests", JSON.stringify(requests));



    alert("A verification request has been sent.");
    this.router.navigate(["/profile/" + this.globals.currentUsername]);

  }

  ngOnInit(): void {

    var url_username = this.route.snapshot.params["User"];

    if (this.globals.currentUsername != url_username) {
      this.router.navigate(["/"]);
    } 

    this.backend.getUser(this.globals.currentUsername).subscribe(res => {
      var user_data = JSON.stringify(res);
      user_data = user_data.substring(1, user_data.length-1);
      this.user = JSON.parse(user_data);
    });

  }

}
