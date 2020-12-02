import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-manage-verification',
  templateUrl: './manage-verification.component.html',
  styleUrls: ['./manage-verification.component.scss']
})
export class ManageVerificationComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals,
    private router: Router
  ) { }

  requests: Array<String>;
  @Input() user_request: string = "";

  directProfile() {
    this.router.navigate(["/profile/" + this.globals.currentUsername]);
  }

  acceptVerification() {
    localStorage.setItem("verified_" + this.user_request, "true");

    const index =this.requests.indexOf(this.user_request, 0);
    if (index > -1) {
      this.requests.splice(index, 1);
    }

    localStorage.setItem("verification_requests", JSON.stringify(this.requests));

    alert("User: " + this.user_request + " has been verified.");
    this.router.navigate(["/profile/" + this.globals.currentUsername]);
  }

  
  ngOnInit(): void {
    this.requests = JSON.parse(localStorage.getItem("verification_requests"));
    //alert(this.requests);
  }

}
